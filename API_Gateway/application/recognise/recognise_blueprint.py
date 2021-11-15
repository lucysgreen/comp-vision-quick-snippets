from flask import Blueprint
from flask import current_app as app

###############################
### Blueprint Configuration ###
###############################

recognise_bp = Blueprint(
    "recognise_bp", __name__
)

##############
### Routes ###
##############

@recognise_bp.route("/recognise", methods=["GET", "POST"])
def example_route():
    """An example of a route which returns Hello World! as string on a GET request."""
    return "Hello World!"