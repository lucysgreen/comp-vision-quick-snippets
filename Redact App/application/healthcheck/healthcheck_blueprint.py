from flask import Blueprint, make_response, jsonify
from flask import current_app as app

###############################
### Blueprint Configuration ###
###############################

healthcheck_bp = Blueprint(
    "healthcheck_bp", __name__
)

##############
### Routes ###
##############

@healthcheck_bp.route("/healthcheck", methods=["GET"])
def healthcheck_route():
    """This route returns 200 if the service is up and running."""
    return make_response(jsonify(message = "API Gateway is healthy."), 200)