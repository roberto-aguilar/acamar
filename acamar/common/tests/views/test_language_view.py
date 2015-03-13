from django.test import TestCase
from django.core.urlresolvers import reverse


class TestLanguageView(TestCase):

    def test_language_view_redirect(self):
        language_url = reverse('common:language')
        response = self.client.get(language_url)
        self.assertTemplateUsed(
            response=response, template_name='common/language.html')
        self.assertIn('redirect_to_url', response.context,
            'Expected redirect_to_url key to be in response context')
        index_url = reverse('common:index')
        self.assertEqual(index_url, response.context['redirect_to_url'],
            'Expected index url to be equal to redirect_to_url in context')
