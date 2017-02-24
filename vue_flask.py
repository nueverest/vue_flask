from flask import Flask, render_template
from flask_s3 import FlaskS3, url_for


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
    favicon = url_for('static', filename='favicon.ico')
    return render_template('index.html', favicon=favicon)


if __name__ == '__main__':
    app.run()
