from flask import render_template, url_for, flash, redirect
from Reservation import app, db
from Reservation.forms import ReservationForm
from Reservation.models import Reserve

@app.route("/")
@app.route("/home")
def home():
    reservations = Reserve.query.all()
    return render_template('home.html', title = 'Home', reservations=reservations)


@app.route("/reserve", methods=['GET', 'POST'])
def reserve():
    form = ReservationForm()
    reservations = 0
    for i in  Reserve.query.all():
        reservations += 1
    if form.validate_on_submit():
        reservation = Reserve(name=form.name.data, phone=form.phone.data, guests=form.guests.data)
        if reservations < 5: # the maximum number of reservations is 5
            db.session.add(reservation)
            db.session.commit()
            flash('Your reservation has been created!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Capacity Exceeded', 'info')
            return redirect(url_for('home'))
    return render_template('reservation_page.html', title='reservation page', form=form)


@app.route("/<int:reservation_id>/delete", methods=['POST'])
def delete_reservation(reservation_id):
    reservation = Reserve.query.get_or_404(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    flash('Your reservation has been deleted', 'info')
    return redirect(url_for('home'))