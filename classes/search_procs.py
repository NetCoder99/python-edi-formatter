import json
from typing import Dict

from models.search_response import SearchResponse


def searchClaims(request_form_args: Dict, url_path: str):
    try:
        search_response = SearchResponse(request_form_args)
        if request_form_args['search_string'] is None or request_form_args['search_string'] == '':
            search_response.response_error = "Please enter a search string!"
            return {
                'response_type'    : "error",
                'response_message' : f"No search string was entered for the {url_path} page!",
            }

        return {
            'response_type'    : "success",
            'response_message' : f"The {url_path} page is searching for that string value..."}

    except Exception as ex:
        raise ex

def fetchClaimsFromDB():
    return {}