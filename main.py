from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    # Run the app on port 5000, accessible from any network interface (0.0.0.0)
    app.run(port=5000, host="0.0.0.0", debug=True)