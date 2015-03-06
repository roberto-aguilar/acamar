from django.test import TestCase
from django.core.urlresolvers import reverse


class TestLanguageView(TestCase):

    def test_language_view_redirect(self):
        language_url = reverse('common:language')
        HTTP_200_OK = 200
        response = self.client.get(language_url)
        self.assertEqual(response.status_code, HTTP_200_OK,
            'Expected response status code 200, received instead {status_code}'.format(
                status_code=response.status_code))
