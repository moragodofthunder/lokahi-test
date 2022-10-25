"""CRUD operations."""
from model import db, User, Trip, Place, Activity, connect_to_db

def get_user_by_email(email):
    return User.query.filter(User.email == email).first()

def create_user(email, password, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname)

    return user  

def check_email_and_pass(email, password):
    return User.query.filter(User.password == password, 
                            User.email == email).first()

def get_user_id(email):
    if User.query.filter(User.email).first() == email:
        return User.query.filter(User.user_id).first()


if __name__ == '__main__':
    from lokahi_server import app
    connect_to_db(app)