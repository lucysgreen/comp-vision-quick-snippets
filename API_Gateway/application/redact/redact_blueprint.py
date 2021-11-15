from flask import Blueprint
from flask import current_app as app

###############################
### Blueprint Configuration ###
###############################

redact_bp = Blueprint(
    "redact_bp", __name__
)

##############
### Routes ###
##############

@redact_bp.route("/redact", methods=["GET", "POST"])
def example_route():
    """An example of a route which returns Hello World! as string on a GET request."""
    return "Hello World!"