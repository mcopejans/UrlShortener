
import flask
import flask_cors
import logging

from coding_challenge.url_shortener import url_shortener, url_validator

app = flask.Flask(__name__)
app.config["DEBUG"] = False
flask_cors.CORS(app)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

url_shortener_instance = url_shortener.URLShortener()

@app.route('/shorten', methods=['GET'])
def shorten_url():
    request_args = flask.request.args
    if not 'long_url' in request_args:
        return "Error, required to add search key \"long_url\", optionally add \"custom_url\"", 404

    long_url = request_args['long_url']
    custom_url = None
    if 'custom_url' in request_args:
        logger.info("Custom URL specified.")
        custom_url = request_args['custom_url']

    logger.info("Url to shorten: %s", long_url)
    try:
        valid = url_validator.UrlValidator.validate(long_url)
    except AttributeError as ex:
        return "Invalid URL given", 404

    if valid:
        short_url = url_shortener_instance.shorten_url(long_url, custom_url=custom_url)
        logger.info("Created short url: %s" + short_url);
    else:
        return "Error, received invalid long url", 404

    return flask.jsonify(short_url)

@app.route('/enlarge', methods=['GET'])
def enlarge_url():
    request_args = flask.request.args
    if not 'short_url' in request_args:
        return "Error, required to add search key \"short_url\"", 404

    short_url = request_args['short_url']
    logger.info("Url to enlarge: %s", short_url)
    try:
        valid = url_validator.UrlValidator.validate(short_url)
    except AttributeError as ex:
        return "Invalid URL given", 404
    if valid:
        unique_id = short_url.split('/')[-1]
        try:
            long_url = url_shortener_instance.get_long_url_from_id(unique_id)
        except KeyError:
            return "Error, short URL not found in repository"
        logger.info("Recreated long url: %s" + long_url);
    else:
        return "Error, received invalid short url", 404

    return flask.jsonify(long_url)

@app.route('/')
def main():
    return 'This is the URL shortener backend based on Python Flask.'


app.run(host='0.0.0.0', port=3001)