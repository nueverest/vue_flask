# builtins
from unittest import TestCase, main

# plugins
# import urllib2
import flask
# from flask_testing import LiveServerTestCase

# custom
import vue_flask


# Basic Functionality Test
class TestVueFlask(TestCase):
    def setUp(self):
        vue_flask.app.config['TESTING'] = True
        self.app = vue_flask.app

    def tearDown(self):
        pass

    def go(self, path):
        return self.app.test_client().get(path)

    def test_server_is_up_and_running(self):
        with self.app.test_request_context():
            home = '/'
            response = self.go(home)
            self.assertTrue(response.status_code == 200)
            self.assertTrue(flask.request.path == home)
            self.assertTrue('Person Creation Machine' in response.data, msg=response.data)

    def test_is_production(self):
        with self.app.test_request_context():
            self.assertFalse(vue_flask.is_production())

    def test_select_url_for_http(self):
        with self.app.test_request_context():
            expected = ['/static/favicon.ico', '/static/js/vendor/foundation.min.js']
            actual = [
                vue_flask.select_url_for('static', filename='favicon.ico'),
                vue_flask.select_url_for('static', filename='js/vendor/foundation.min.js')
            ]
            for index, expected_value in enumerate(expected):
                self.assertEqual(expected_value, actual[index])

    def test_select_url_for_https(self):
        # refenerence: http://stackoverflow.com/questions/42469831/how-to-test-https-in-flask/42470048#42470048
        with self.app.test_request_context(environ_overrides={'wsgi.url_scheme': 'https'}):
            expected = [
                'https://nueverest.s3.amazonaws.com/static/favicon.ico',
                'https://nueverest.s3.amazonaws.com/static/js/vendor/foundation.min.js'
            ]
            actual = [
                vue_flask.select_url_for('static', filename='favicon.ico'),
                vue_flask.select_url_for('static', filename='js/vendor/foundation.min.js')
            ]
            for index, expected_value in enumerate(expected):
                self.assertEqual(expected_value, actual[index])


if __name__ == '__main__':
    main()