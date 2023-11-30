from app import app, db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    mobile_phone = db.Column(db.String(255), nullable=False)
    job = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), default='default.jpg', nullable=False)
    company_name = db.Column(db.Integer, db.ForeignKey('company.name'))

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), default='default.jpg', nullable=False)
    tags = db.relationship('Tag', backref='company', lazy=True)
    employees = db.relationship('Employee', backref='company', lazy=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

with app.app_context():
    db.create_all()
