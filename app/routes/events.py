from flask_login import login_required
from flask_restful import Resource
from ..models import Event, Household
from ..schemas import (event_schema, events_schema)


class HouseholdEventsApi(Resource):

    def get(self, household_id):
        events = Household.query.get_or_404(household_id).events
        return events_schema.dump(events)


class EventsApi(Resource):

    def post(self):
        # event = Event(
        #     employee_id=form.employees.data,
        #     table_id=form.tables.data,
        #     finished=False
        # )
        # db.session.add(order)
        # db.session.commit()
        return {"create": "event"}


class EventApi(Resource):

    # get a event
    def get(self, event_id):
        event = User.query.get_or_404(event_id)
        return event_schema.dump(event)

    # update a event
    # def patch(self, id):
    #     return {"hello": "world"}

    # delete a event
    # def delete(self, id):
    #     return {"hello": "world"}
