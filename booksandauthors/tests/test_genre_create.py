from booksandauthors.models import Genre
from base import CreateViews


class TestAuthorCreate(CreateViews):
    basename = "genre"
    model = Genre
    view_name_suffix = "create"
    template_name = "create.html"
    attributes = {"title": "Novel"}

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