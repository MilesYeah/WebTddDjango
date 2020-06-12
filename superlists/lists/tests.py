from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.

# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1, 2)

#     def test_good_math(self):
#         self.assertEqual(1, 1)


class HomePageTest(TestCase):
    def test_root_url_resolver_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        req = HttpRequest()
        resp = home_page(req)
        self.assertTrue(resp.content.startswith(b'<html>'))
        self.assertIn(b"<title>To-Do</title>", resp.content)
        self.assertTrue(resp.content.endswith(b"</html>"))

