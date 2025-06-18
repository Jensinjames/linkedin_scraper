import unittest
from linkedin_scraper import Person

class TestPersonScraper(unittest.TestCase):

    def test_rick_fox_profile(self):
        profile_url = "https://www.linkedin.com/in/rifox?trk=pub-pbmap"
        person = Person(profile_url)
        self.assertIsNotNone(person)
        # Optionally, check for expected attributes if available
        # self.assertEqual(person.name, "Expected Name")

    def test_iggy_profile(self):
        profile_url = "https://www.linkedin.com/in/andre-iguodala-65b48ab5"
        person = Person(profile_url)
        self.assertIsNotNone(person)

    def test_anirudra_profile(self):
        profile_url = "https://in.linkedin.com/in/anirudra-choudhury-109635b1"
        person = Person(profile_url)
        self.assertIsNotNone(person)

if __name__ == "__main__":
    unittest.main()
