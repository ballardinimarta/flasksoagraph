from flask import Flask
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, DateTimeField

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'SHH!'
app.config["TEMPLATES_AUTO_RELOAD"] = True


now_time = datetime.now

class dateform(FlaskForm):
    start = DateTimeField(id = 'startpick', format = '%Y-%m-%d %H:%M',
                            default = now_time() - timedelta(hours=24))
    stop =DateTimeField(id = 'stoppick', format = '%Y-%m-%d %H:%M',
                            default = datetime.now)
    submit = SubmitField('Submit')




@app.route("/", methods=['POST', 'GET'])
def home():
    error = None
    date_form = dateform()
    if not date_form.validate_on_submit():
        get_plot(now_time() - timedelta(hours=48), now_time())
    if date_form.validate_on_submit():
        if date_form.start.data == date_form.stop.data:
            error ='starttime and stoptime cannot be the same time'
        elif date_form.start.data > date_form.stop.data:
            error ='the stoptime has to be later than the starttime'
        elif date_form.stop.data > now_time():
            error ='stoptime cannot be later than the current date and time'
        elif date_form.stop.data-date_form.start.data>timedelta(hours=50):
            error ='the measurement cannot be larger than 50 hours'
        else:
            get_plot(date_form.start.data, date_form.stop.data)


    return render_template('index.html', date_form=date_form, error=error)

from soa_chart_24.func import get_plot

if __name__ == "__main__":
    app.run(debug=False)
