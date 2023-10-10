from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.String(50), nullable=False)   
    location = db.Column(db.String(100), nullable=True)
    company = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"Job(title='{self.title}', category='{self.category}')"
