from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# Create a model for RSVPs
class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


# Define routes and views
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        rsvp_entry = RSVP(name=name, email=email)
        db.session.add(rsvp_entry)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('rsvp.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
