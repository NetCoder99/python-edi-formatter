import json
from typing import Dict
from enum import Enum

#-------------------------------------------------------------------------------------------
# Used by the search web pages to manage the response from search functions
#-------------------------------------------------------------------------------------------
class ResponseType(Enum):
    SUCCESS = 'success'
    ERROR   = 'error'
    INFO    = 'info'

class SearchResponse:
    search_args      : Dict = {}
    response_type    : ResponseType = ResponseType.INFO
    response_message : str
    response_data    : Dict = {}

    def __init__(self, search_args):
        self.search_args = search_args

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)