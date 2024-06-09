import unittest

class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("Мастер и Маргарита")
        self.assertIn("Мастер и Маргарита", self.collector.get_books_genre())
        self.assertEqual(self.collector.get_books_genre()["Мастер и Маргарита"], "")

    def test_add_new_book_with_long_name(self):
        self.collector.add_new_book("Мастер и Маргарита" * 5)
        self.assertNotIn("Мастер и Маргарита" * 5, self.collector.get_books_genre())

    def test_set_book_genre(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("1984"), "Фантастика")

    def test_set_book_genre_invalid(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Роман")
        self.assertEqual(self.collector.get_book_genre("1984"), "")

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.collector.add_new_book("Зелёная Миля")
        self.collector.set_book_genre("Зелёная Миля", "Ужасы")
        self.assertEqual(self.collector.get_books_with_specific_genre("Фантастика"), ["1984"])

    def test_get_books_for_children(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.collector.add_new_book("Зелёная Миля")
        self.collector.set_book_genre("Зелёная Миля", "Ужасы")
        self.assertEqual(self.collector.get_books_for_children(), ["1984"])

    def test_add_book_in_favorites(self):
        self.collector.add_new_book("1984")
        self.collector.add_book_in_favorites("1984")
        self.assertIn("1984", self.collector.get_list_of_favorites_books())

    def test_add_book_in_favorites_not_in_books(self):
        self.collector.add_book_in_favorites("1984")
        self.assertNotIn("1984", self.collector.get_list_of_favorites_books())

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("1984")
        self.collector.add_book_in_favorites("1984")
        self.collector.delete_book_from_favorites("1984")
        self.assertNotIn("1984", self.collector.get_list_of_favorites_books())

if name == '__main__':
    unittest.main()