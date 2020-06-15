
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.views import home_page
from lists.models import Item


# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolver_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     req = HttpRequest()
    #     resp = home_page(req)
    #     # self.assertTrue(resp.content.startswith(b'<html>'))
    #     # self.assertIn(b"<title>To-Do</title>", resp.content)
    #     # self.assertTrue(resp.content.strip().endswith(b"</html>"))
    #
    #     html_expected = render_to_string("home.html")
    #     html_received = resp.content.decode()
    #
    #     # print("")
    #     # print(html_received)
    #     # print(html_expected)
    #
    #     self.assertEqual(html_expected, html_received)

    def test_home_page_can_save_a_post_request(self):
        s1 = "A new list item"

        self.client.post("/", data={'item_text': s1})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, s1)

    def test_home_page_redirects_after_POST(self):
        s1 = "A new list item"

        response = self.client.post("/", data={'item_text': s1})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_displays_all_list_items(self):
        s1 = "item1"
        s2 = "item2"
        Item.objects.create(text=s1)
        Item.objects.create(text=s2)

        request = HttpRequest()
        response = home_page(request)

        self.assertIn(s1, response.content.decode())
        self.assertIn(s2, response.content.decode())


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

    print("")
