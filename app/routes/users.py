from flask_login import login_required
from flask_restful import Resource
from ..models import User, Household
from ..schemas import (user_schema, users_schema)


class HouseholdUsersApi(Resource):

    def get(self, household_id):
        users = Household.query.get_or_404(household_id).users
        return users_schema.dump(users)


class UsersApi(Resource):

    def post(self):
        return {"create": "user"}


class UserApi(Resource):

    # get a user
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    # update a user
    # def patch(self, id):
    #     return {"hello": "world"}

    # delete a user
    # def delete(self, id):
    #     return {"hello": "world"}
