from flask import Blueprint, make_response, jsonify, request
from flask import current_app as app

import requests

###############################
### Blueprint Configuration ###
###############################

translate_bp = Blueprint(
    "translate_bp", __name__
)

##############
### Routes ###
##############

@translate_bp.route("/translate", methods=["GET", "POST"])
def translate_route():
    """This route handles our API response for the translate microservice."""

    if request.method == "GET":

        return make_response(
            jsonify(
                help_message = "Insert how to use this API route here."
            ), 200)


    if request.method == "POST":

        # Post request will send off to our translate microservice.

        # First, we check our response to see if it is in the correct format.

        # Limit string to 512 words.

        # Build the URL for our source-languages request.
        url = str(app.config['TRANSLATE_URL'] + "ENDPOINT HERE")

        return make_response(
            jsonify(
                message = "API Gateway is healthy."
            ), 200)


@translate_bp.route("/source-languages", methods=["GET", "POST"])
def translate_route():
    """This route handles our API response allowing users to get a list of the source languages installed."""

    if request.method == "GET":

        return make_response(
            jsonify(
                help_message = "Insert how to use this API route here."
            ), 200)


    if request.method == "POST":
        # Post request will send off to our translate microservice.

        # Build the URL for our source-languages request.
        url = str(app.config['TRANSLATE_URL'] + "ENDPOINT HERE")

        return requests.get(url)