from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# create SQLAlchemy object
db = SQLAlchemy()


class Household(db.Model):
    # inherit from SQLAlchemy instance's model baseclass

    # explicitly specify table name instead of relying on Flask-SQLAlchemy
    __tablename__ = "households"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # has many
    # back_populates provides explicit instruction on which property a
    # relationship is mapped to; back_populates needs to be used in both
    # classes where relationship is defined
    users = db.relationship("User", back_populates="household")
    events = db.relationship("Event", back_populates="household")
    chores = db.relationship("Chore", back_populates="household")
    bills = db.relationship("Bill", back_populates="household")


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    household_id = db.Column(db.Integer, db.ForeignKey("households.id"))
    accepted_into_household = db.Column(db.Boolean, default=False)
    admin_privileges = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # belongs to
    household = db.relationship("Household", back_populates="users")

    # has many
    events = db.relationship("Event", back_populates="author")
    # need to specify foreign keys because there are multiple foreign
    # keys linking to the same table
    authored_chores = db.relationship(
        "Chore", back_populates="author", foreign_keys="Chore.author_id")
    assigned_chores = db.relationship(
        "Chore", back_populates="assigned_user", foreign_keys="Chore.assigned_user_id")
    bills = db.relationship("Bill", back_populates="user")

    # create password property
    @property
    def password(self):
        return self.hashed_password

    # create a password setter that generates a password hash and sets the
    # hashed password
    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    # check that the password is correct
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    all_day = db.Column(db.Boolean, default=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    household_id = db.Column(db.Integer, db.ForeignKey("households.id"))
    author_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # belongs to
    household = db.relationship("Household", back_populates="events")
    author = db.relationship("User", back_populates="events")


class Chore(db.Model):
    __tablename__ = "chores"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    household_id = db.Column(db.Integer, db.ForeignKey(
        "households.id"), nullable=False)
    author_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    assigned_user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), default=None)
    complete = db.Column(db.Boolean, default=False)
    difficulty = db.Column(db.Integer, default=1)
    recurring = db.Column(db.String(255), default="never")
    due_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # belongs to
    household = db.relationship("Household", back_populates="chores")
    # need to specify foreign keys because there are multiple foreign
    # keys linking to the same table
    author = db.relationship(
        "User", back_populates="authored_chores", foreign_keys="Chore.author_id")
    assigned_user = db.relationship(
        "User", back_populates="assigned_chores", foreign_keys="Chore.assigned_user_id")


class Bill(db.Model):
    __tablename__ = "bills"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    household_id = db.Column(db.Integer, db.ForeignKey(
        "households.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # belongs to
    household = db.relationship("Household", back_populates="bills")
    user = db.relationship("User", back_populates="bills")
