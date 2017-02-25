# Flask
from flask import Flask, render_template, request
from flask import url_for as local_url_for
from flask_s3 import FlaskS3
from flask_s3 import url_for as s3_url_for


class CustomFlask(Flask):
    """
    Override Jinja2 default delimiters.  {{ }} --> {[ ]}
    Reference: https://gist.github.com/lost-theory/3925738
    """
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='{[',
        variable_end_string=']}',
        comment_start_string='{#',
        comment_end_string='#}',
    ))


app = CustomFlask(__name__)
app.config['DEBUG'] = True
app.config['FLASKS3_BUCKET_NAME'] = 'nueverest'
app.config['FLASKS3_USE_HTTPS'] = True
app.config['USE_S3_DEBUG'] = True

s3 = FlaskS3(app)


@app.route('/')
def index():
    favicon = select_url_for('static', filename='favicon.ico')
    foundationcss = select_url_for('static', filename='css/foundation.min.css')
    blowdrycss = select_url_for('static', filename='css/blowdry.min.css')
    maincss = select_url_for('static', filename='css/main.css')
    jquery = select_url_for('static', filename='js/vendor/jquery.js')
    whatinput = select_url_for('static', filename='js/vendor/what-input.js')
    foundationjs = select_url_for('static', filename='js/vendor/foundation.min.js')
    return render_template(
        'index.html',
        favicon=favicon,
        foundationcss=foundationcss,
        blowdrycss=blowdrycss,
        maincss=maincss,
        jquery=jquery,
        whatinput=whatinput,
        foundationjs=foundationjs
    )


def is_production():
    """ Determines if app is running on the production server or not.

    Get Current URI.
    Extract root location.
    Compare root location against developer server value 127.0.0.1:5000.
    :return: (bool) True if code is running on the production server, and False otherwise.
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url != developer_url


def select_url_for(endpoint, filename):
    """ Select the static media url based on the server url.

    :param endpoint: (string) Media folder
    :param filename: (string) Media filename including subpath if necessary e.g. 'css/main.css', 'flower.jpg'
    :return: (string) Local url sub-path or full S3 url for media.
    """
    if is_production():
        return s3_url_for(endpoint=endpoint, filename=filename)

    return local_url_for(endpoint=endpoint, filename=filename)


if __name__ == '__main__':
    app.run()
