import unittest
from app.models import Articles

class TestArticle(unittest.TestCase):
    def setUp(self):
        """
        create an article instance before every test is run
        """
        self.article = Articles('The Associated Press',
                           'Islamic State strikes from shadows in vulnerable Syria, Iraq',
                           'Islamic State group militants carried out two of their boldest attacks in years last week',
                           'https://abcnews.go.com/International/wireStory/islamic-state-strikes-shadows-vulnerable-syria-iraq-82561425',
                           'https://s.abcnews.com/images/International/WireAP_84511efe33ee472597318543d83925b4_16x9_992.jpg',
                           '2022-01-30T14:00:00Z',
                           'Islamic State group militants carried out two of their boldest attacks in years last week'
                           )

    def test_instance(self):
        """
        Method to test if the articles variable is an instance of Articles class
        """
        self.assertTrue(isinstance(self.article, Articles))        