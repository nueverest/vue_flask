# python 2
from __future__ import absolute_import, print_function, unicode_literals

# builtins
from io import StringIO
import gzip

# plugins
from flask import after_this_request, request
import functools


def gzipped(f):
    """" Custom view decorator that gzips the view if the server is capable.

    Background: AWS serverless architecture places the responsibility of gzipping a flask view on the application.
    Normally, the web server (nginx, apache, iis) would handle this task.
    Source: http://flask.pocoo.org/snippets/122/
    """
    @functools.wraps(f)
    def view_func(*args, **kwargs):
        @after_this_request
        def zipper(response):
            accept_encoding = request.headers.get('Accept-Encoding', '')

            if 'gzip' not in accept_encoding.lower():
                return response

            response.direct_passthrough = False

            if 200 > response.status_code >= 300 or 'Content-Encoding' in response.headers:
                return response

            gzip_buffer = StringIO()
            gzip_file = gzip.GzipFile(mode='wb', fileobj=gzip_buffer)
            gzip_file.write(response.data)
            gzip_file.close()

            response.data = gzip_buffer.getvalue()
            response.headers['Content-Encoding'] = 'gzip'
            response.headers['Vary'] = 'Accept-Encoding'
            response.headers['Content-Length'] = len(response.data)
            response.headers['Cache-Control'] = 'max-age=0'

            return response

        return f(*args, **kwargs)

    return view_func
