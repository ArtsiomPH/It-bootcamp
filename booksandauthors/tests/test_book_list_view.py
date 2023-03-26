from base import ListViews
from booksandauthors.models import Book


class TestBookList(ListViews):
    basename = "books"
    model = Book
    view_name_suffix = "list"
    template_name = "books_list.html"

    def test_view_url_exists_at_desired_location(self) -> None:
        self.view_url_exists_at_desired_location()

    def test_view_url_accessible_by_name(self) -> None:
        self.view_url_accessible_by_name()

    def test_view_uses_correct_template(self) -> None:
        self.view_uses_correct_template()

    def test_pagination_is_twenty(self) -> None:
        self.pagination_is_twenty()

    def test_lists_all_objects(self) -> None:
        self.lists_all_objects({"page": 2})
