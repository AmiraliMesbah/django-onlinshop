from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class AboutUsPageTest(TestCase):
    def test_aboutus_page_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEquals(response.status_code, 200)

    def test_aboutus_page_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us Page')

    def test_aboutus_page_template_used(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')
