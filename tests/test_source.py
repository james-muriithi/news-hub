import unittest
from ..app.models import Sources
from ..app.models import Sources


class TestSource(unittest.TestCase):

    def setUp(self):
        """
        create a source instance before every test is run
        """
        self.source = Sources('abc-news', "ABC News", "Your credible news source",
                         "https://bbc-news.com", "sports", "us")

    def test_instance(self):
        """
        Method to test if the source variable is an instance of Sources class
        """
        self.assertTrue(isinstance(self.source, Sources))

if __name__ == "__main__":
    unittest.main()        