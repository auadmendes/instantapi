import ssl
import urllib3

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import os
os.environ['PYTHONHTTPSVERIFY'] = '0'

import requests
requests.packages.urllib3.disable_warnings()


from flask import Flask
from flask_cors import CORS

from routes.upload import upload_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


app.register_blueprint(upload_bp)

if __name__ == "__main__":
    # Run the app on port 5000, accessible from any network interface (0.0.0.0)
    app.run(port=5000, host="0.0.0.0", debug=True)



    #  personal code