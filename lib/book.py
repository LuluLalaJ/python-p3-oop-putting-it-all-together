#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0) -> None:
        self.title = title.title()
        self.page_count = page_count

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, num):
        if isinstance(num, int):
            self._page_count = num
        else:
            print("page_count must be an integer")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
