from flask import Flask
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, flash, request
from flask_wtf import Form
from wtforms.fields import DateTimeField, SubmitField

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'SHH!'

now_time = datetime.now()
defstarttime = datetime.now() - timedelta(hours=24)


class dateform(Form):
    start = DateTimeField(id = 'startpick',  format = '%Y-%m-%d %H:%M',
                            default = defstarttime)
    stop =DateTimeField(id = 'stoppick',  format = '%Y-%m-%d %H:%M',
                            default = datetime.now)
    submit = SubmitField('Submit')


@app.route("/", methods=['POST', 'GET'])
def home():
    error = None
    date_form = dateform()
    if date_form.validate_on_submit():
        if date_form.start.data == date_form.stop.data:
            error ='starttime and stoptime cannot be the same time'
        elif date_form.start.data > date_form.stop.data:
            error ='the stoptime has to be later than the starttime'
        elif date_form.stop.data > now_time:
            error ='stoptime cannot be later than the current date and time'
        elif date_form.stop.data-date_form.start.data>timedelta(hours=24):
            error ='the measurement cannot be larger than 24 hours'
        else:
            get_plot(date_form.start.data, date_form.stop.data)
            return redirect(url_for('soa'))

    return render_template('index.html', date_form=date_form, error=error)


@app.route("/soa")
def soa():
    return render_template('soa.html')

from soa_chart_24.func import get_plot

if __name__ == "__main__":
    app.run(debug=True)
