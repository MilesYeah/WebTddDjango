from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.views import home_page
from lists.models import Item

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
        # self.assertTrue(resp.content.startswith(b'<html>'))
        # self.assertIn(b"<title>To-Do</title>", resp.content)
        # self.assertTrue(resp.content.strip().endswith(b"</html>"))
        expeted_html = render_to_string("home.html")
        self.assertEqual(resp.content.decode(), expeted_html)

    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = "A new list item"

        response = home_page(request)
        self.assertIn("A new list item", response.content.decode())
        expected_html = render_to_string('home.html', {'new_item_text': "A new list item"})
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        s1 = "The first (ever) list item"
        s2 = "Item the second"

        first_item = Item()
        first_item.text = s1
        first_item.save()

        second_item = Item()
        second_item.text = s2
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, s1)
        self.assertEqual(second_saved_item.text, s2)


if __name__ == "__main__":
    pass
