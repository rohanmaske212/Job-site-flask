from flask import Flask, render_template, request, redirect, url_for
from models import db, Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get(job_id)
    return render_template('job_detail.html', job=job)

@app.route('/category/<string:category>')
def job_category(category):
    jobs = Job.query.filter_by(category=category).all()
    return render_template('job_category.html', jobs=jobs, category=category)

@app.route('/employer', methods=['GET', 'POST'])
def employer():
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        description = request.form['description']
        salary = request.form['salary']
        current_city = request.form['currentCity']
        current_state = request.form['currentState']
        current_country = request.form['currentCountry']
        category = request.form['category']  

        # Perform category recommendation logic here based on title and description
        # You can use machine learning or a predefined category list for recommendations

        job = Job(
            title=title,
            company=company,
            description=description,
            salary=salary,
            location=f"{current_city}, {current_state}, {current_country}",
            category=category  
        )
        db.session.add(job)
        db.session.commit()
        return redirect('/')
    return render_template('employer.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
