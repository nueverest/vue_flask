# builtins
from unittest import TestCase, main

# flask app
from vue_flask import is_production, select_url_for


class TestVueFlask(TestCase):
    def test_is_production(self):
        pass

    def test_select_url_for(self):
        pass
        # expected = 'static/favicon.ico'
        # actual = select_url_for('static', filename='favicon.ico')
        # self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()