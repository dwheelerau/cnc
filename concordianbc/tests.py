from django.test import TestCase
from django.core.urlresolvers import resolve
from concordianbc.views import home_page
from django.http import HttpRequest
# from django.template.loader import render_to_string


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_url(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(
            '<title>Welcome to Concordia netball!</title>',
            response.content.decode())
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_has_three_navigaton_links(self):
        # test home, results, about links
        # <a href>
        request = HttpRequest()
        response = home_page(request)
        # home_page_string = render_to_string('home.html')
        self.assertIn('<a href="">Home</a>', response.content.decode())
        self.assertIn('<a href="">Results</a>', response.content.decode())
        self.assertIn('<a href="">About</a>', response.content.decode())
