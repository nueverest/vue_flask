# builtins
from unittest import TestCase, main
import requests
from time import sleep

# plugins
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# application
from vue_flask import get_input_id, get_population_limit


class TestDeployedSiteWithRequests(TestCase):
    def setUp(self):
        self.site = 'https://kw4udfbos9.execute-api.us-west-2.amazonaws.com/production'

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
        self.input_id = get_input_id()
        self.creationform = self.input_id['creationform']
        self.firstname = self.input_id['firstname']
        self.lastname = self.input_id['lastname']
        self.dob = self.input_id['dob']
        self.zipcode = self.input_id['zipcode']
        self.submit = self.input_id['submit']
        self.population = self.input_id['population']

        self.population_limit = get_population_limit()

        for browser in self.browsers:
            self.addCleanup(browser.quit)

    def delete_person(self, browser):
        # Delete first person is list. First in First out.
        first_delete_icon = browser.find_element_by_id('0')
        first_delete_icon.click()

    def handle_population_limits(self, browser):
        """ The population value comes from firebase and is loading by vue. Both of these operations take time. A delay
        is required to ensure that the population value is correct since vue sometimes loads the value 0 then changes
        it once firebase returns.

        Steps:
        Wait for vue and firebase.
        Test that population is within limits.
        If population is at the max population limit decrement population.
        Return population value.
        """
        population_element = browser.find_element_by_id(self.population)
        sleep(1.5)    # Wait for vue and firebase lag.
        population = int(population_element.text)

        self.assertTrue(0 <= population <= self.population_limit, msg='Population out of bounds.')

        if population == self.population_limit:
            self.delete_person(browser)
            self.assertTrue(self.population_decremented(browser, population))
            return population - 1

        return population

    def population_changed(self, browser, population_expected):
        # Reference: http://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp#explicit-waits
        # https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/support/expected_conditions.py
        delay = 5   # in seconds
        try:
            WebDriverWait(browser, delay).until(
                expected_conditions.text_to_be_present_in_element((By.ID, self.population), population_expected)
            )
            return True
        except TimeoutException:
            return False

    def population_decremented(self, browser, population_before):
        population_expected = unicode(int(population_before) - 1)
        return self.population_changed(browser, population_expected)

    def population_incremented(self, browser, population_before):
        population_expected = unicode(int(population_before) + 1)
        return self.population_changed(browser, population_expected)

    def test_page_title(self):
        for browser in self.browsers:
            browser.get(self.site)
            self.assertIn('Person Creation Machine', browser.title)

    def test_population_exists(self):
        for browser in self.browsers:
            browser.get(self.site)
            population_element = browser.find_element_by_id(self.population)
            population = int(population_element.text)
            self.assertTrue(0 <= population <= self.population_limit)

    def test_create_a_person_form_valid_data(self):
        element_ids = [self.firstname, self.lastname, self.dob, self.zipcode, ]
        valid_input = ['Xython', 'Ber', '1999-09-09', '85000', ]

        for browser in self.browsers:
            browser.get(self.site)
            population_before = self.handle_population_limits(browser)

            for index, element_id in enumerate(element_ids):
                input_element = browser.find_element_by_id(element_id)
                input_element.send_keys(valid_input[index])

            submit_button = browser.find_element_by_id(self.submit)
            submit_button.click()
            self.assertTrue(self.population_incremented(browser, population_before))

    def test_button_disabled(self):
        submit = self.submit

        for browser in self.browsers:
            browser.get(self.site)
            submit_button = browser.find_element_by_id(submit)
            self.assertFalse(submit_button.is_enabled())

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