from flask_marshmallow import Marshmallow
from app.models import Household, User, Event, Chore, Bill

ma = Marshmallow()


# create schema to serialize objects so they can be returned as json in routes
# use SQLAlchemyAutoSchema
class HouseholdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Household


# create schema object to use when serializing a single object in resource
household_schema = HouseholdSchema()
# create schema object to use when serializing a multiple objects in resource
households_schema = HouseholdSchema(many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event


event_schema = EventSchema()
events_schema = EventSchema(many=True)


class ChoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chore


chore_schema = ChoreSchema()
chores_schema = ChoreSchema(many=True)


class BillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bill


bill_schema = BillSchema()
bills_schema = BillSchema(many=True)
