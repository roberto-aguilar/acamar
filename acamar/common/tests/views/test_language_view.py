from django.test import TestCase
from django.core.urlresolvers import reverse


class TestLanguageView(TestCase):

    def test_language_view_redirect(self):
        language_url = reverse('common:language')
        index_url = reverse('common:index')
        response = self.client.get(language_url)
        self.assertRedirects(response, expected_url=index_url,
            msg_prefix='Expected redirect to index view')
