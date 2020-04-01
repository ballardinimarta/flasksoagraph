from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import Form
from wtforms.fields import DateTimeField, SubmitField
from soa_chart_24.func import get_plot

now_time = datetime.now()
defstarttime = datetime.now() - timedelta(hours=24)


class dateform(Form):
    start = DateTimeField(id = 'startpick', format='%m/%d/%Y %H:%M %p')
    stop =DateTimeField(id = 'stoppick', format='%m/%d/%Y %H:%M %p')
    submit = SubmitField('Submit')

class defaultform(Form):
    default = SubmitField('Default')


@app.route("/", methods=['POST', 'GET'])
def home():
    error = None
    date_form = dateform()
    default_form = defaultform()
    if date_form.validate_on_submit():
        if date_form.start.data == date_form.stop.data:
            error ='starttime and stoptime cannot be the same time'
        elif date_form.start.data > date_form.stop.data:
            error ='the stoptime has to be later than the starttime'
        elif date_form.stop.data > now_time:
            error ='stoptime cannot be later than the current date and time'
        else:
            get_plot(date_form.start.data, date_form.stop.data)
            return redirect(url_for('soa'))
    if default_form.validate_on_submit():
        if default_form.default.data:
            get_plot(defstarttime, now_time)
            return redirect(url_for('soa'))

    return render_template('index.html', date_form=date_form, default_form=default_form, error=error)


@app.route("/soa")
def soa():
    return render_template('soa.html')
