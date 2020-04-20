from flask import Flask
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta, date
from flask import render_template, redirect, url_for, flash, request, current_app
from flask_wtf import FlaskForm
from wtforms.widgets import html_params, HTMLString
from wtforms.fields import SubmitField, DateTimeField
import arrow

#Define app
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Config keys
app.secret_key = 'SHH!'
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TIMEZONE"] = 'local'

# Some time variables
now_time = arrow.now
today = date.today
offset = arrow.now('local').utcoffset()
dtnow = datetime.now

# The widget for the DateTimeLocalField from gist https://gist.github.com/tachyondecay/2c1462eed197f879f0bf
class DateTimeWidget:
    """Widget for DateTimeFields using separate date and time inputs."""
    def __call__(self, field, **kwargs):
        id = kwargs.pop('id', field.id)
        date = time = ''
        if field.data:
            dt = arrow.get(field.data).to(current_app.config['TIMEZONE'])
            date = dt.format('YYYY-MM-DD')
            time = dt.format('HH:mm')
        date_params = html_params(name=field.name, id=id + '-date', value=date, **kwargs)
        time_params = html_params(name=field.name, id=id + '-time', value=time, **kwargs)
        return HTMLString('<input type="date" {}/><input type="time" {}/>'.format(date_params, time_params))

# The custom field found from gist https://gist.github.com/tachyondecay/2c1462eed197f879f0bf
class DateTimeLocalField(DateTimeField):
    """
    DateTimeField that assumes input is in app-configured timezone and converts
    to UTC for further processing/storage.
    """
    widget = DateTimeWidget()

    def process_formdata(self, valuelist):
        current_app.logger.debug(valuelist)
        if valuelist:
            date_str = ' '.join(valuelist)
            try:
                self.data = arrow.get(date_str).replace(tzinfo=current_app.config['TIMEZONE']).to('UTC')
            except arrow.parser.ParserError as e:
                current_app.logger.warn('Invalid datetime value submitted: %s', e)
                raise ValueError('Not a valid datetime value. Looking for YYYY-MM-DD HH:mm.')

# Form for the inputs
class dateform(FlaskForm):
    start = DateTimeLocalField(id = 'startpick', default = now_time)
    stop =DateTimeLocalField(id = 'stoppick', default = now_time)
    submit = SubmitField('Submit')

# Route for Homepage
@app.route("/", methods=['POST', 'GET'])
def home():
    error = None
    date_form = dateform()
    if not date_form.validate_on_submit():
        get_plot(dtnow() - timedelta(hours=26), dtnow())
    if date_form.validate_on_submit():
        if date_form.start.data == date_form.stop.data:
            error ='starttime and stoptime cannot be the same time'
        elif date_form.start.data > date_form.stop.data:
            error ='the stoptime has to be later than the starttime'
        elif date_form.stop.data-date_form.start.data>timedelta(hours=50):
            error ='the measurement cannot be larger than 50 hours'
        else:
            get_plot(date_form.start.data, date_form.stop.data)


    return render_template('index.html', date_form=date_form, error=error)

# Import statement after route to avoid circular imports
from soa_chart_24.func import get_plot

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug=False)
