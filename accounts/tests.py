from django.test import TestCase
from django.urls import reverse
class SignUpPageTest(TestCase):
    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
    def test_signup_page_content(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Signup Page')

class LoginPageView(TestCase):
    def test_login_page_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
    def test_login_page_content(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Login Page')
