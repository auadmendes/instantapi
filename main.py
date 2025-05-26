import ssl
import urllib3



# Disable SSL verification globally (use with caution)
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import os

# Environment variables to disable SSL verification and configure verbosity
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "info"
os.environ["HF_ENDPOINT"] = "https://huggingface.co"

from routes.ask import ask_bp
from routes.comment import comment_only_bp
from routes.upload import upload_bp
from routes.summary import summary_bp

import requests
requests.packages.urllib3.disable_warnings()

from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(upload_bp)
app.register_blueprint(ask_bp)
app.register_blueprint(comment_only_bp)
app.register_blueprint(summary_bp)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
