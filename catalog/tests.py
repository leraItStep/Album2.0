from django.test import TestCase
from django.urls import reverse


class YourAppTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_app/home.html')

    def test_create_object(self):
        response = self.client.post(reverse('create_object'), data={'name': 'Test Object'})
        self.assertEqual(response.status_code, 302)

    def test_object_detail(self):
        object_id = 1  # replace with a valid object id
        response = self.client.get(reverse('object_detail', args=[object_id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Object')

    def test_delete_object(self):
        object_id = 1  # replace with a valid object id
        response = self.client.post(reverse('delete_object', args=[object_id]))
        self.assertEqual(response.status_code, 302)
