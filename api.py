# api.py
from flask import Blueprint, request, jsonify
from urllib.parse import quote, unquote
import base64, re
from datetime import datetime
import pytz

api = Blueprint('api', __name__)

@api.route('/quote', methods=['POST'])
def quote_string():
    return jsonify({"result": quote(request.json.get("text", ""))})

@api.route('/unquote', methods=['POST'])
def unquote_string():
    return jsonify({"result": unquote(request.json.get("text", ""))})

@api.route('/remove-extra-spaces', methods=['POST'])
def remove_extra_spaces():
    text = request.json.get("text", "")
    return jsonify({"result": re.sub(r'\s+', ' ', text).strip()})

@api.route('/remove-whitespace', methods=['POST'])
def remove_whitespace():
    return jsonify({"result": ''.join(request.json.get("text", "").split())})

@api.route('/base64-encode', methods=['POST'])
def base64_encode():
    return jsonify({"result": base64.b64encode(request.json.get("text", "").encode()).decode()})

@api.route('/base64-decode', methods=['POST'])
def base64_decode():
    try:
        decoded = base64.b64decode(request.json.get("text", "").encode()).decode()
        return jsonify({"result": decoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api.route('/url-encode', methods=['POST'])
def url_encode():
    return jsonify({"result": quote(request.json.get("text", ""))})

@api.route('/url-decode', methods=['POST'])
def url_decode():
    return jsonify({"result": unquote(request.json.get("text", ""))})

@api.route('/unix-to-mst', methods=['POST'])
def unix_to_mst():
    ts = int(request.json.get("timestamp", 0))
    mst = pytz.timezone('US/Mountain')
    dt = datetime.fromtimestamp(ts, tz=mst)
    return jsonify({"result": dt.strftime('%Y-%m-%d %H:%M:%S')})

@api.route('/mst-to-unix', methods=['POST'])
def mst_to_unix():
    dt_str = request.json.get("datetime", "")
    mst = pytz.timezone('US/Mountain')
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    return jsonify({"result": int(mst.localize(dt).timestamp())})

