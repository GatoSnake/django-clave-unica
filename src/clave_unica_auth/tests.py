from django.test import TestCase, Client
from django.urls import reverse

class ClaveUnicaTestCase(TestCase):
    def test_redirect_to_clave_unica(self):
        c = Client()
        response = c.get(reverse('clave_unica_auth-login'))
        self.assertEqual(response.status_code, 302)
