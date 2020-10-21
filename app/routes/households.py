from flask_login import login_required
from flask_restful import Resource
from ..models import Household
from ..schemas import (household_schema, households_schema)


class HouseholdsApi(Resource):

    # get all households
    def get(self):
        # get all the households
        households = Household.query.all()
        # serialize the list of households as json using marshmallow schema
        return households_schema.dump(households)

    # create a new household
    # def post(self):
    #     return {"hello": "world"}


class HouseholdApi(Resource):

    # get a household
    def get(self, household_id):
        # get household; if it doesn't exist, throw 404
        household = Household.query.get_or_404(household_id)
        return household_schema.dump(household)

    # update a household
    # def patch(self, id):
    #     return {"hello": "world"}

    # delete a household
    # def delete(self, id):
    #     return {"hello": "world"}


