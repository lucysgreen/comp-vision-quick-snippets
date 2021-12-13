from flask import Blueprint, make_response, jsonify, request
from flask import current_app as app

import json

from .redact import *

###############################
### Blueprint Configuration ###
###############################

redact_bp = Blueprint(
    "sentiment_bp", __name__
)

##############
### Routes ###
##############

@redact_bp.route("/redact", methods=["POST"])
def redact_route():
    """This route handles our main redact function."""
    request_data = request.get_json() 
    return redact(request_data["Text To Redact"], request_data["Redaction Criteria"])

