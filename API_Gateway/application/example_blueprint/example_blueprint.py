from flask import Blueprint
from flask import current_app as app

###############################
### Blueprint Configuration ###
###############################

example_bp = Blueprint(
    "example_bp", __name__
)

##############
### Routes ###
##############

@example_bp.route("/example", methods=["GET"])
def example_route():
    """An example of a route which returns Hello World! as string on a GET request."""
    return "Hello World!"