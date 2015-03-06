from django.test import TestCase
from django.core.urlresolvers import reverse


class TestLanguageView(TestCase):

    def setUp(self):
        self.language_url = reverse('common:language')

    def test_language_view_with_http_referral_header(self):
        index_url = reverse('common:index')
        response = self.client.get(self.language_url, **{
            'HTTP_REFERER': index_url
        })
        self.assertEqual(response.context['redirect_to_url'], index_url,
            'Expected response context redirect url to be equal to HTTP_REFERER url')

    def test_language_view_without_http_referral_header(self):
        HTTP_200_OK = 200
        response = self.client.get(self.language_url)
        self.assertNotIn('HTTP_REFERER', response.request,
            'Expected HTTP_REFERER not to be in request')
        self.assertEqual(response.status_code, HTTP_200_OK,
            'Expected response status code 200, received instead {status_code}'.format(
                status_code=response.status_code))
