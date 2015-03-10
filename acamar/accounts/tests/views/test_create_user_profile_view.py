from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCreateUserProfileView(TestCase):

    def setUp(self):
        self.register_url = reverse('accounts:register')

    def test_register_view_with_correct_data_provided(self):
        success_url = reverse('accounts:login')
        base64_image = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00'  # noqa
        form_data = {
            'username': 'test_username_view',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com',
            'image': SimpleUploadedFile(content=base64_image,
                name='profile-photo.png', content_type='image/jpeg')
        }
        response = self.client.post(self.register_url, form_data)
        self.assertRedirects(response, expected_url=success_url,
            msg_prefix='Expected redirect after correct data provided')
