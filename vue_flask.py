# python 2
from __future__ import absolute_import, print_function, unicode_literals

# Flask
from flask import Flask, render_template, request
from flask import url_for as local_url_for
from flask_s3 import FlaskS3
from flask_s3 import url_for as s3_url_for

# custom
from gzipper import gzipped

# Ignore missing secrets file for Travis CI, and local development.
try:
    from secrets import is_production
except ImportError:
    def is_production():
        return False


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


# Configuration Options
class Config(object):
    DEBUG = False
    TESTING = False
    FLASKS3_BUCKET_NAME = 'nueverest'
    FLASKS3_USE_HTTPS = True
    USE_S3_DEBUG = False


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    USE_S3_DEBUG = True


class Testing(Config):
    TESTING = True


# Initialize Application
app = CustomFlask(__name__)
app.config.from_object(Production) if is_production() else app.config.from_object(Development)
s3 = FlaskS3(app)


@app.route('/')
@gzipped
def index():
    url_for = {
        'favicon': select_url_for('static', filename='favicon.ico'),
        'combinedcss': select_url_for('static', filename=get_css_filename()),
        'combinedjs': select_url_for('static', filename=get_js_filename()),
        # 'materialicons': 'https://fonts.googleapis.com/icon?family=Material+Icons',
        # 'vuejs': 'https://unpkg.com/vue@2.0.7/dist/vue.js',
        # 'firebase': 'https://www.gstatic.com/firebasejs/3.6.10/firebase.js',
        # 'vuefire': 'https://unpkg.com/vuefire@1.3.0/dist/vuefire.js',
    }

    input_id = get_input_id()
    name_max_length = 100
    zipcode_max_length = 10

    return render_template(
        'index.html',
        url_for=url_for,
        input_id=input_id,
        name_max_length=name_max_length,
        zipcode_max_length=zipcode_max_length,
        population_limit=get_population_limit(),
    )


def get_css_filename():
    return 'css/combined1.min.css.gz' if is_production() else 'css/processed/combined.min.css'


def get_js_filename():
    return 'js/vendor/production.js.gz' if is_production() else 'js/vendor/dev.js'


def get_input_id():
    return {
        'creationform': 'creationform',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'dob': 'dob',
        'zipcode': 'zipcode',
        'submit': 'submit',
        'population': 'population',
    }


def get_population_limit():
    return 18


def select_url_for(endpoint, filename):
    """ Select the static media url based on the server url.

    :param endpoint: (string) Media folder
    :param filename: (string) Media filename including subpath if necessary e.g. 'css/main.css', 'flower.jpg'
    :return: (string) Local url sub-path or full S3 url for media.
    """
    if is_production() or request.is_secure:
        return s3_url_for(endpoint=endpoint, filename=filename)

    return local_url_for(endpoint=endpoint, filename=filename)


if __name__ == '__main__':
    app.run()
