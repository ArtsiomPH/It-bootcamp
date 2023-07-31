from booksandauthors.models import Author
from base import CreateViews


class TestAuthorCreate(CreateViews):
    basename = "author"
    model = Author
    view_name_suffix = "create"
    template_name = "create.html"
    attributes = {"first_name": "John", "second_name": "Dorian"}

    def test_view_url_exists_at_desired_location(self) -> None:
        self.view_url_exists_at_desired_location('add/')

    def test_view_url_accessible_by_name(self) -> None:
        self.view_url_accessible_by_name()

    def test_view_uses_correct_template(self) -> None:
        self.view_uses_correct_template()

    def test_object_has_attribures(self) -> None:
        self.created_object_has_attributes()

    def test_object_single_in_db(self) -> None:
        self.created_object_single_in_db()

    def test_object_accessible_in_detail(self) -> None:
        self.check_object_accessible_in_detail()
