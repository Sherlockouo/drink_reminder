from flask import Flask
from flask_cors import CORS
from router.gpt_router import gpt


app = Flask(__name__)
CORS(app)

app.register_blueprint(gpt)

 