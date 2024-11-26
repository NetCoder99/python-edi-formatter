# ----------------------------------------------------------------------------------------------
# Demo project for managing EDI formatted claim data
# ----------------------------------------------------------------------------------------------
import json

from flask import Flask, request, redirect, url_for, render_template
from werkzeug.exceptions import HTTPException
from urllib.parse import urlparse

from classes.search_procs import searchClaims

app = Flask(__name__)

#-------------------------------------------------------------------------------------------
# Web page end points
#-------------------------------------------------------------------------------------------
@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    url_path = urlparse(request.referrer).path
    if request.method == 'POST':
        search_response = searchClaims(request.form, url_path)
        return render_template('home.html', search_response=search_response)
    else:
        return render_template('home.html',search_response={
            'response_type'    : "info",
            'response_message' : "Please enter a search string for the home page!"
        })

@app.route('/index', methods = ['GET', 'POST'])
def index():
    url_path = urlparse(request.referrer).path
    if request.method == 'POST':
        search_response = searchClaims(request.form, url_path)
        return render_template('index.html', search_response=search_response)
    else:
        return render_template('index.html',search_response={
            'response_type'    : "info",
            'response_message' : "Please enter a search string for the index page!"
        })

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    # response.data = json.dumps({
    #     "code": e.code,
    #     "name": e.name,
    #     "description": e.description,
    # })
    # response.content_type = "application/json"
    # return response
    print(f'error response: {response.data}')
    return render_template(
        'error.html',
        err_code = e.code,
        err_name = e.name,
        err_desc = e.description
    )

# #-------------------------------------------------------------------------------------------
# # Data / api end points
# #-------------------------------------------------------------------------------------------
# @app.route('/search', methods = ['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         search_response = search_claims(request.form)
#         return render_template('index.html', search_response=search_response)
#     else:
#         return render_template('index.html',search_response={
#             'response_type'    : "info",
#             'response_message' : "Please enter a search string for the home page!"
#         })
#
#     if request.method == 'POST':
#         search_response = search_claims(request.form)
#         url_path = urlparse(request.referrer).path
#         if url_path.endswith('index'):
#             return redirect(url_for('index', search_response=search_response))
#             #return render_template('index.html', search_response=search_response)
#         elif url_path.endswith('home'):
#             return render_template('home.html', search_response=search_response)
#         else:
#             return render_template(
#                 'error.html',
#                 err_code='400',
#                 err_name='Unknown referrer',
#                 err_desc='The referrer to the search function is unknown.'
#             )
#     else:
#         return render_template('index.html', search_response={})

#-------------------------------------------------------------------------------------------
# Run the app, set startup config, etc.
#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()

