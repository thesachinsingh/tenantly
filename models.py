from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    username = db.Column(db.String, nullable = False, unique = True)
    pw = db.Column(db.String, nullable = False)

class Tenants(db.Model):
    tenant_id = db.Column(db.Integer, primary_key = True, nullable = False)
    tenant_name = db.Column(db.String, nullable = False, unique = True)
    tenant_room_no = db.Column(db.String, nullable = False, unique = True)
    tenant_rent = db.Column(db.Integer, nullable = False)
    tenant_electricity_rate = db.Column(db.Integer, default = 10)
    tenant_join_date = db.Column(db.DateTime)
    monthly_receipt = db.relationship("Generate", backref = "tenant_details")

    def __repr__(self):
        return '<Tenant %r>' % self.tenant_name



class TenantRecords(db.Model):
    __tablename__ = 'tenant_records'
    transaction_id = db.Column(db.Integer, primary_key = True, nullable = False)
    tenant_id = db.Column(db.integer, db.ForeignKey("tenants.tenant_id"), nulable = False)
    month = db.Column(db.String, nullable = False)
    prev_bal = db.Column(db.Integer, nullable = False)

    curr_month_charges = db.Column(db.Integer, db.ForeignKey("generate.bill"), nullable = False)
    
    money_recieved = db.Column(db.Integer, nullable = False)
    curr_bal = db.Column(db.Integer, nullable = False)
    tenant_details = db.relationship("Tenants", backref = "transactions")
    monthly_receipt = db.relationship("Generate", backref = "all_transactions")

    

class Generate(db.Model):
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.tenant_id"), nullable = False)
    generated_date = db.Column(db.DateTime, nullable = False)
    for_month = db.Column(db.String, nullable = False)
    #tenant_details relationship with Tenants table


