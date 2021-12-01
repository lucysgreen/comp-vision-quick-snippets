from flask import Blueprint, make_response, jsonify, request
from flask import current_app as app

import json

from .sentiment import *

###############################
### Blueprint Configuration ###
###############################

sentiment_bp = Blueprint(
    "sentiment_bp", __name__
)

##############
### Routes ###
##############

@sentiment_bp.route("/analyse", methods=["POST"])
def analyse_route():
    """This route handles our main sentiment analyse function."""
    return analyse_sentiment(request.get_json())

