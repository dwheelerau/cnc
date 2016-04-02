from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# the django test class
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_user_hits_homepage(self):
        # a new user types in the url and finds the homepage
        self.browser.get(self.live_server_url)
        # title = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('Welcome to Concordia netball!', title)
        self.assertIn('Welcome', self.browser.title)

    def test_user_can_navigate_site(self):
        # the visitor sees two links at the top of the page
        # these are: home, results, about
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(5)

        home_link = self.browser.find_element_by_link_text('Home')
        self.assertIn('Home', home_link.text)

        results_link = self.browser.find_element_by_link_text('Results')
        self.assertIn('Results', results_link.text)

        about_link = self.browser.find_element_by_link_text('About')
        self.assertIn('About', about_link.text)
        # about_link.click()

        # she clicks on results and gets taken onto a new page
        about_link.click()
        # self.assertIn('Results', self.browser.title)
        # the results page also has these three links
        results_url = self.browser.current_url
        self.assertRegex(results_url, '/results/.+')

        # so she now clicks on the about
        # she gets taken to a new page
        # this new page also has the three links
        self.fail('Finish the tests')
