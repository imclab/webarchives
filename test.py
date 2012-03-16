from unittest import TestCase, main

from webarchives import backends, lookup

class TestLookup(TestCase):

    def test_lookup(self):
        results = lookup("http://nytimes.com")
        self.assertTrue(len(results) > 0)

    def test_internet_archive(self):
        results = backends.internet_archive.lookup('http://nytimes.com')
        self.assertTrue(len(results) > 0)

    def test_british_library(self):
        results = backends.british_library.lookup('http://bbc.co.uk')
        self.assertTrue(len(results) > 0)

    def test_archiefweb(self):
        results = backends.archiefweb.lookup('http://www.denhelder.nl/')
        self.assertTrue(len(results) > 0)

if __name__ == "__main__":
    main()