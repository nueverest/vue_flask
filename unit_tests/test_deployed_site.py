# builtins
from unittest import TestCase, main
import requests

# plugins
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestDeployedSiteWithRequests(TestCase):
    def setUp(self):
        self.site = 'https://kw4udfbos9.execute-api.us-west-2.amazonaws.com/production'

    def tearDown(self):
        pass

    def test_server_is_up_and_running(self):
        request = requests.get(self.site)
        self.assertEqual(200, request.status_code)

    def test_server_content_type(self):
        request = requests.get(self.site)
        self.assertEqual('text/html; charset=utf-8', request.headers['Content-Type'], msg=request.headers)


class TestDeployedSiteWithSelenium(TestCase):
    def setUp(self):
        # Reference: http://seleniumhq.github.io/selenium/docs/api/py/
        self.site = 'https://kw4udfbos9.execute-api.us-west-2.amazonaws.com/production'
        self.browsers = [
            # webdriver.Chrome(),
            webdriver.Firefox(),
            # webdriver.Ie()
        ]

        for browser in self.browsers:
            self.addCleanup(browser.quit)

    def tearDown(self):
        pass

    def test_page_title(self):
        for browser in self.browsers:
            browser.get(self.site)
            self.assertIn('Person Creation Machine', browser.title)

    def test_create_a_person_form_valid_data(self):
        form_id = 'creationform'
        element_ids = ['firstname', 'lastname', 'dob', 'zipcode']
        valid_input = ['Xython', 'Ber', '9/9/1999', '85000']

        for browser in self.browsers:
            browser.get(self.site)

            for index, element_id in enumerate(element_ids):
                input_element = browser.find_element_by_id(element_id)
                input_element.send_keys(valid_input[index])

            form_element = browser.find_element_by_id(form_id)
            form_element.submit()


    # def test_create_a_person_form_input_length_exceeded(self):
    #     pass
    #
    # def test_create_a_person_form_future_birth_day(self):
    #     pass
    #
    # def test_create_a_person_form_invalid_zipcodes(self):
    #     pass
    #
    # def test_create_a_person_form(self):
    #     pass
    #
    # def test_create_a_person_button_disabled(self):
    #     pass
    #
    # def test_remove_person_top_table(self):
    #     pass
    #
    # def test_remove_person_bottom_table(self):
    #     pass
    #
    # def test_population_limit(self):
    #     pass
    #
    # def test_population_changed(self):
    #     pass




if __name__ == '__main__':
    main()