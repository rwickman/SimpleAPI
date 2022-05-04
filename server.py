

from flask import Flask, request, session, jsonify
from server_state import *
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Create approvers
approvers = [Approver(MOBILE_USER_ID)]

# Create request manager
req_manager = RequestManager(approvers, ApproverAssigner())


@app.route('/request_file', methods=['POST'])
@cross_origin()
def request_file():
    content = request.get_json(force=True)
    if (content["user_id"], content["file_id"]) not in req_manager.requests:

        request_time = req_manager.create_request(
            content["user_id"],
            content["file_id"])
        return jsonify({"request_time": request_time})
    else:
        request_status = req_manager.check_request(
            content["user_id"],
            content["file_id"])
        return jsonify({"request_status": request_status})


@app.route('/get_request/<int:approver_id>', methods=['GET'])
@cross_origin()
def get_requests(approver_id):
    pending = req_manager.get_pending(approver_id)
    return jsonify(pending) 

@app.route('/request_response/<int:approver_id>', methods=['POST'])
@cross_origin()
def request_response(approver_id):
    content = request.get_json(force=True)
    req_manager.update_status(
        approver_id,
        content["user_id"],
        content["file_id"],
        content["request_response"])
    return "uh"




# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.run(host='0.0.0.0', port=5000)