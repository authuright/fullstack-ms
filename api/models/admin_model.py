from app.app import db
from sqlalchemy import DateTime,func

class AdminsModel(db.Model):
    __tablename__='admins'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(50),nullable=False)
    sname=db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    passwd=db.Column(db.String(100),nullable=False)
    rupdate=db.Column(db.DateTime,nullable=False,default=func.now())