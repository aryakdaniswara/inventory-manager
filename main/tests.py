from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_name_field(self):
        item = Item.objects.create(name='name')
        self.assertEqual(item.name, 'name')

    def test_name_max_length(self):
        item = Item.objects.create(name='KLqa8pXqtliI9wwUDG7ruYIFWjRDJZFsySpuabY12HEgWWnbvdywu2Zl8yGUiVZIbwhHEIiuCPfc8EnlRf6Okzbb3ocihi9pRaUmS3QpHeQoGctIV842FF2WUUKLIQ7LzVFQ1cdwrmz1lbuSg1DU0ActIsMdcSsWiyUOfOk1SsvYlFpZiP4UkGpWe3sHyiZxCzDZJLVVJoZIRhmYOTH1v4sHjoVNvFWqAhREiau4HQB2uC9faDZE17bRxI6Cc2h')
        self.assertEqual(item.name, 'KLqa8pXqtliI9wwUDG7ruYIFWjRDJZFsySpuabY12HEgWWnbvdywu2Zl8yGUiVZIbwhHEIiuCPfc8EnlRf6Okzbb3ocihi9pRaUmS3QpHeQoGctIV842FF2WUUKLIQ7LzVFQ1cdwrmz1lbuSg1DU0ActIsMdcSsWiyUOfOk1SsvYlFpZiP4UkGpWe3sHyiZxCzDZJLVVJoZIRhmYOTH1v4sHjoVNvFWqAhREiau4HQB2uC9faDZE17bRxI6Cc2h')