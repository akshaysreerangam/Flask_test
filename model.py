from db import db


class Leavereq(db.Model):
    __tablename__='Leaverequest'
    employee_id=db.Column(db.String(25),primary_key=True)
    start_date=db.Column(db.Date(),nullable=False)
    end_date=db.Column(db.Date(),nullable=False)
    leave_type=db.Column(db.String(20),nullable=False)
    reason=db.Column(db.String(50),nullable=False)


