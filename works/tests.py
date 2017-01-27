from django.test import TestCase

from .models import Work


def create_work(name):
    w = Work.objects.create(name=name)
    return w


class WorkMethodTests(TestCase):


    # Models
    def test_slug_save(self):
        art_work = create_work('new artwork')
        self.assertEqual(art_work.slug,"new-artwork")


    # Pages
    def test_homepage(self):
        response = self.client.get('/works/')
        self.assertEqual(response.status_code,200)
