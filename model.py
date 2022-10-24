"""Models for Lokahi web app."""

from socketserver import ThreadingTCPServer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User data"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True,
                        nullable= False)
    fname = db.Column(db.String(30), nullable= False)
    lname = db.Column(db.String(30), nullable= True)
    email = db.Column(db.String(50), nullable= False)
    password = db.Column(db.String, nullable= False)
    profile_img = db.Column(db.String, nullable= True)

    trips = db.relationship("Trip", back_populates="user")
    places = db.relationship("Place", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.fname}>"

class Trip(db.Model):
    """Trip data"""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True,
                        nullable= False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id")
                        nullable= False)
    trip_name = db.Column(db.String(50), nullable= False)
    trip_country = db.Column(db.String(30), nullable= False)
    trip_city = db.Column(db.String(30), nullable= False)
    start_date = db.Column(db.DateTime, nullable= False)
    end_date = db.Column(db.DateTime, nullable= False)
    trip_img = db.Column(db.String, nullable= True)

    user = db.relationship("User", back_populates="trips")
    places = db.relationship("Place", back_populates="trips")

    def __repr__(self):
        return f"<Trip trip_id={self.trip_id}>"

class Place(db.Model):
    """Saved place data"""

    __tablename__ = "places"

    place_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True,
                        nullable= False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id")
                        nullable= False)
    trip_id = db.Column(db.Integer,
                        db.ForeignKey("trips.trip_id")
                        nullable= False)
    place_name = db.Column(db.String(50), nullable= False)
    place_country = db.Column(db.String(30), nullable= False)
    place_city = db.Column(db.String(30), nullable= False)
    in_plan = db.Column(db.Boolean, nullable= False)
    category = db.Column(db.String(30), nullable= False)
    latitude = db.Column(db.Float, nullable= False)
    longitude = db.Column(db.Float, nullable= False)

    user = db.relationship("User", back_populates="places")
    trips = db.relationship("Trip", back_populates="places")
    plans = db.relationship("Plan", back_populates= "places")

    def __repr__(self):
        return f"<Place place_id={self.place_id}>"

class Plan(db.Model):
    """Itinerary data"""

    __tablename__ = "plans"

    plan_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True,
                        nullable= False)
    place_id = db.Column(db.Integer,
                        db.ForeignKey("places.place_id")
                        nullable= False)
    trip_id = db.Column(db.Integer,
                        db.ForeignKey("trips.trip_id")
                        nullable= False)
    activity_datetime = db.Column(db.DateTime)

    places = db.relationship("Place", back_populates="plans")
    trips = db.relationship("Trip", back_populates="plans")

    def __repr__(self):
        return f"<Plan plan_id={self.plan_id}>"






if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)