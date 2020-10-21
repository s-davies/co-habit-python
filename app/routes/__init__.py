from .households import HouseholdsApi, HouseholdApi
from .users import HouseholdUsersApi, UsersApi, UserApi


def initialize_routes(api):

    # add all resources to build backend routes
    api.add_resource(HouseholdsApi, "/households")
    # variable name must be same as parameter name in resource
    api.add_resource(HouseholdApi, "/households/<int:household_id>")

    # users
    api.add_resource(HouseholdUsersApi, "/households/<int:household_id>/users")
    api.add_resource(UsersApi, "/users")
    api.add_resource(UserApi, "/users/<int:user_id>")
