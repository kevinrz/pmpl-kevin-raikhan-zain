from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_template_using_home_page_html(self):
        found = self.client.get('/')
        self.assertTemplateUsed(found, 'homepage.html')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Kevin RZ</title>', html)
        self.assertIn('<span id="full_name">Kevin Raikhan Zain</span>', html)
        self.assertIn('<a href="mailto:kevinraikhan@gmail.com" id="email">kevinraikhan@gmail.com</a>', html)
        self.assertIn('<a href="https://linkedin.com/in/kevin-raikhan-zain/" id="linkedin">LinkedIn</a>', html)
        self.assertTrue(html.endswith('</html>'))
