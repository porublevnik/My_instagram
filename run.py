from flask import Flask
from main.views import main
from api.views import endpoints


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(main)
app.register_blueprint(endpoints)

@app.errorhandler(404)
def not_found_error(error):
    return 'page not found', 404

@app.errorhandler(500)
def not_found_error(error):
    return 'Internal server error', 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
