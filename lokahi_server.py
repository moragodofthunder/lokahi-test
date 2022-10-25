"""Server for Lokahi web app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """"Return render template to homepage.html"""

    return render_template('homepage.html')

@app.route('/login')
def show_login_page():
    """Shows log in and create account page"""

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    """Login to user account"""

    email = request.form.get("email")
    password = request.form.get("password")

    match = crud.check_email_and_pass(email, password)

    if not match:
        flash("This email doesn't match anything in our system.")
        return redirect("/login")
    else:
        session["user_email"]=match.email
        flash("Logged in!")
    
        return redirect("/user_profile/<user_id>")

@app.route('/user_profile/<user_id>')
def show_user_profile():
    """"Return render template to user_profile.html"""

    return render_template('user_profile.html')

@app.route('/user_profile', methods=['POST'])
def create_new_user():
    """Create new user account"""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("first-name")
    lname = request.form.get("last-name")

    user = crud.get_user_id(email)

    if user:
        flash("An account with this email already exists.")
    else:
        user = crud.create_user(email, password, fname, lname)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully. Please log in.")
    
        return render_template("user_profile.html", first_name=fname)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)