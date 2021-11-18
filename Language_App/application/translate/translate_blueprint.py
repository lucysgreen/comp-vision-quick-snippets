from flask import Blueprint, make_response, jsonify, request
from flask import current_app as app

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

    # First, get the request from our API gateway.

    request_data = request.data

    print(request_data)

    # First, we check our request to see if it is in the correct format.

    # Limit string to 512 words.

    return argos_translate_to_english(request_data)
    #return 'Hi!'


@translate_bp.route("/identify", methods=["POST"])
def identify_route():
    """This route is used to identify unknown languages."""

    # First, get our Text content from request by API gateway.

    request_data = request.args.get('Text')

    return glcd3_language_detector(request_data)

@translate_bp.route("/source-languages", methods=["GET"])
def source_languages_route():
    """This route allows users to get a list of the source languages installed on our app."""

    # First, get request from API gateway.

    request_data = request.data

    print(request_data)

    return make_response(jsonify(return_installed_argos_languages()), 200)
