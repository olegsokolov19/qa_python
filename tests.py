import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_two_same_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating_nonexistent_book(self):
        collector = BooksCollector()

        collector.set_book_rating('Кот хочет вас убить', 6)

        assert collector.get_book_rating('Кот хочет вас убить') is None

    def test_set_book_rating_set_rating_greater_ten(self):
        collector = BooksCollector()

        collector.set_book_rating('Кот хочет вас убить', 11)

        assert collector.get_book_rating('Кот хочет вас убить') is None

    def test_set_book_rating_set_rating_less_one(self):
        collector = BooksCollector()

        book_name = 'Кот хочет вас убить'

        collector.set_book_rating(book_name, 11)

        assert collector.get_book_rating(book_name) is None

    def test_get_book_rating_get_rating_nonexistent_book(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Кот хочет вас убить') is None

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()

        book_name = 'Кот хочет вас убить'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 1 and collector.get_list_of_favorites_books()[0] == book_name

    def test_add_book_in_favorites_when_book_not_in_books_rating(self):
        collector = BooksCollector()

        book_name = 'Кот хочет вас убить'

        collector.add_book_in_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_existing_book(self):
        collector = BooksCollector()

        book_name = 'Кот хочет вас убить'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0
