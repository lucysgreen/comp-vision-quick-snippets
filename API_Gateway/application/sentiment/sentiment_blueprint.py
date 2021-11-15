from flask import Blueprint
from flask import current_app as app

###############################
### Blueprint Configuration ###
###############################

sentiment_bp = Blueprint(
    "sentiment_bp", __name__
)

##############
### Routes ###
##############

@sentiment_bp.route("/example", methods=["GET"])
def example_route():
    """An example of a route which returns Hello World! as string on a GET request."""
    return "Hello World!"