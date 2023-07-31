from base import DetailViews
from booksandauthors.models import Author


class TestAuthorDetail(DetailViews):
    basename = "author"
    model = Author
    view_name_suffix = "detail"
    template_name = "author_detail.html"
    attributes = {"first_name": "John", "second_name": "Dorian"}

    def test_view_url_exists_at_desired_location(self) -> None:
        self.view_url_exists_at_desired_location(self.obj.id)

    def test_view_url_accessible_by_name(self) -> None:
        self.view_url_accessible_by_name({"pk": self.obj.id})

    def test_view_uses_correct_template(self) -> None:
        self.view_uses_correct_template({"pk": self.obj.id})

    def test_exist_author(self) -> None:
        self.check_exist_obj()

    def test_nonexist_author(self) -> None:
        self.check_nonexist_obj()
