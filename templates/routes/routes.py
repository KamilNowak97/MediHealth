from app import app
from flask import render_template,request, redirect
from app import db
from templates.database.Database import Pressure,Medicine_schedule



#----------------------------------------HOME------------------------------------------
@app.route('/')
@app.route('/home')
def index():
        return render_template('index.html')

#----------------------------------------PRESSURE------------------------------------------
@app.route('/pressure/',methods=['POST', 'GET'])
def pressure():
    if request.method == 'POST':
        systolic_measurement = request.form['systolic']
        diastolic_measurement = request.form['diastolic']
        pulse_measurement = request.form['pulse']
        hour_measurement = request.form['hour']
        minute_measurement = request.form['minute']
        new_measurement = Pressure(
            systolic=systolic_measurement,
            diastolic=diastolic_measurement,
            pulse=pulse_measurement,
            hour=hour_measurement,
            minute=minute_measurement
        )

        try:

            db.session.add(new_measurement)
            db.session.commit()
            return redirect('/pressure/')
        except:

            return 'There was an issue adding your task'
    else:
        measurements = Pressure.query.order_by(Pressure.date_created).all()
        return render_template('pressure.html', measurements=measurements)

@app.route('/delete/<int:id>')
def delete(id):
    measurement_to_delete = Pressure.query.get_or_404(id)
    try:
        db.session.delete(measurement_to_delete)
        db.session.commit()
        return redirect('/pressure/')
    except:
        return 'There was problem!'

@app.route('/pressure/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    measurement = Pressure.query.get_or_404(id)
    if request.method == 'POST':
        measurement.systolic = request.form['systolic']
        measurement.diastolic = request.form['diastolic']
        measurement.pulse = request.form['pulse']
        measurement.hour = request.form['hour']
        measurement.minute = request.form['minute']
        try:
            db.session.commit()
            return redirect('/pressure/')
        except:
            return 'There was problem!'
    else:
        return render_template('update.html', measurement=measurement)

#----------------------------------------Medicines------------------------------------------
@app.route('/medicines',methods=['POST','GET'])
def medicines():
    if request.method == 'POST':
        name_medi = request.form['name_m']
        about_medi = request.form['about_m']
        amount_medi = request.form['amount_m']
        interval_medi = request.form['interval_m']
        recom_medi = request.form['recom_m']
        new_schedule = Medicine_schedule(
            name = name_medi,
            about = about_medi,
            amount = amount_medi,
            interval = interval_medi,
            recommendations = recom_medi)
        try:
            db.session.add(new_schedule)
            db.session.commit()
            return redirect('/medicines')
        except:
            return 'There was a problem!'
    else:
        schedules = Medicine_schedule.query.order_by(Medicine_schedule.id).all()
        return render_template('medicines.html',schedules = schedules)
