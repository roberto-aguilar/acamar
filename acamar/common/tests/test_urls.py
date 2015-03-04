from django.test import TestCase
from django.core.urlresolvers import reverse, resolve


class UrlsTest(TestCase):

    def test_index_match_by_url(self):
        match = resolve('/')
        self.assertEqual(match.view_name, 'common:index',
            'Expected view name "common:index", received {view_name} instead.'.format(view_name=match.view_name))

    def test_index_url_by_view_name(self):
        url = reverse('common:index')
        self.assertEqual(url, '/',
            'Expected url "/", received {url} instead.'.format(url=url))