from datetime import datetime
from Reservation import db

class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.name}', '{self.phone}', '{self.guests}', '{self.date_posted}')"

    def reservation_termination(self):
        minutes = 1
        time = self.date_posted + datetime.timedelta(minutes)
        if time > datetime.datetime.now():
            reservation = Reserve.query.get_or_404(self.id)
            db.session.delete(reservation)
            db.session.commit()
        
