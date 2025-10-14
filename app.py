from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# ✅ Make sure instance folder exists
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

# ✅ Correct SQLite path (absolute)
db_path = os.path.join(app.root_path, 'instance', 'firstapp.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<Person {self.id} - {self.first_name}>'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form.get('first_name', '').strip()
        lname = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        if fname and lname and email:
            person = Person(first_name=fname, last_name=lname, email=email)
            db.session.add(person)
            db.session.commit()
        return redirect(url_for('index'))
    people = Person.query.all()
    return render_template('index.html', people=people)

@app.route('/delete/<int:id>')
def delete(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    person = Person.query.get_or_404(id)
    if request.method == 'POST':
        person.first_name = request.form.get('first_name', person.first_name).strip()
        person.last_name = request.form.get('last_name', person.last_name).strip()
        person.email = request.form.get('email', person.email).strip()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', person=person)

if __name__ == '__main__':
    app.run(debug=True)
