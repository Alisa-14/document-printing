import unittest

from main import Document, InkjetPrinter, LaserPrinter


class TestDocument(unittest.TestCase):
    def test_print_page_Inkjet(self):
        page = Document.print_document("InkjetPrinter")
        self.assertEqual(page, InkjetPrinter)

    def test_print_page_Laser(self):
        page = Document.print_document("LaserPrinter")
        self.assertEqual(page, LaserPrinter)

    def test_print_page_Error(self):
        with self.assertRaises(ValueError):
            Document.print_document("FalsePrinter")


if __name__ == '__main__':
    unittest.main()
