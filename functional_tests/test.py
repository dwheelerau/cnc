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
        title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to Concordia netball!', title)
