from utilities.manage_strava_api import get_strava_token
from flask import Flask, request, jsonify
from waitress import serve


def response_template(message,status,statusCode,label,result):
    response = {
        "message": message,
        "status": status,
        "statusCode": statusCode,
        "label": label,
        "result": result
    }
    return response

def configure_routes(app):
    @app.route('/redirect') 
    def strava_redirect():
        args = request.args
        code = args['code']
        token = get_strava_token(code)
        return jsonify(response_template('The Strava authentication flow has finished successfully!','Ok',200,'STRAVA_OAUTH_FLOW',''))
    
def init_rest_server(REDIRECT_PORT):
    app = Flask(__name__)
    # app.config["EXPLAIN_TEMPLATE_LOADING"] = True # for debug purpose
    configure_routes(app)
    serve(app, host='0.0.0.0', port=REDIRECT_PORT)
