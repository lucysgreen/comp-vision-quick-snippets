from flask import Blueprint, make_response, jsonify, request
from flask import current_app as app

import json

from .argos_language_translation import *

###############################
### Blueprint Configuration ###
###############################

translate_bp = Blueprint(
    "translate_bp", __name__
)

##############
### Routes ###
##############

@translate_bp.route("/translate", methods=["POST"])
def translate_route():
    """This route handles our main translation function."""

    return argos_translate_to_english(request.get_json())


@translate_bp.route("/identify", methods=["POST"])
def identify_route():
    """This route is used to identify unknown languages."""

    # First, get our Text content from request by API gateway.

    request_data = request.get_json()

    return glcd3_language_detector(request_data["Text"])

@translate_bp.route("/source-languages", methods=["GET"])
def source_languages_route():
    """This route allows users to get a list of the source languages installed on our app."""

    return make_response(jsonify(return_installed_argos_languages()), 200)
