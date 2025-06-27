from flask import Flask
from modules.documentation.documentation import documentation 
from modules.test_api.test_api import test_api
app = Flask(__name__)

# Correctly register the Blueprint
app.register_blueprint(documentation, url_prefix='/')
app.register_blueprint(test_api, url_prefix='/testApi')

if __name__ == "__main__":
    app.run(debug=True, port=8000)