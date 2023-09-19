from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_name_field(self):
        item = Item.objects.create(name='name', amount=1, description='tes', price=1)
        self.assertEqual(item.name, 'name')

    def test_name_max_length(self):
        item = Item.objects.create(name='KLqa8pXqtliI9wwUDG7ruYIFWjRDJZFsySpuabY12HEgWWnbvdywu2Zl8yGUiVZIbwhHEIiuCPfc8EnlRf6Okzbb3ocihi9pRaUmS3QpHeQoGctIV842FF2WUUKLIQ7LzVFQ1cdwrmz1lbuSg1DU0ActIsMdcSsWiyUOfOk1SsvYlFpZiP4UkGpWe3sHyiZxCzDZJLVVJoZIRhmYOTH1v4sHjoVNvFWqAhREiau4HQB2uC9faDZE17bRxI6Cc2h', amount=1, description='tes', price=1)
        self.assertEqual(item.name, 'KLqa8pXqtliI9wwUDG7ruYIFWjRDJZFsySpuabY12HEgWWnbvdywu2Zl8yGUiVZIbwhHEIiuCPfc8EnlRf6Okzbb3ocihi9pRaUmS3QpHeQoGctIV842FF2WUUKLIQ7LzVFQ1cdwrmz1lbuSg1DU0ActIsMdcSsWiyUOfOk1SsvYlFpZiP4UkGpWe3sHyiZxCzDZJLVVJoZIRhmYOTH1v4sHjoVNvFWqAhREiau4HQB2uC9faDZE17bRxI6Cc2h')