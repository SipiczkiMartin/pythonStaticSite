import unittest

from pagegenerator import *
class TestPageGenerator(unittest.TestCase):

    def test_generate_page(self):
          generate_page(from_path="Hello",template_path="hi",dest_path="ho")


    if __name__ == "__main__":
            unittest.main()