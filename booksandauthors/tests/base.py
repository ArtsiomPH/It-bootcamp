from typing import Type, Union

from django.test import TestCase
from django.urls import reverse
from django.db import models

from booksandauthors.models import Author, Book


class TestViewsBase(TestCase):
    basename: str
    model: Type[models.Model]
    view_name_suffix: str
    template_name: str

    def view_url_exists_at_desired_location(self, args: Union[str, int] = None) -> None:
        if args:
            response = self.client.get(f"/{self.basename}/{args}")
        else:
            response = self.client.get(f"/{self.basename}/")
        self.assertEqual(response.status_code, 200)

    def view_url_accessible_by_name(self, kwargs: dict = None) -> None:
        response = self.client.get(
            reverse(f"{self.basename}-{self.view_name_suffix}", kwargs=kwargs)
        )
        self.assertEqual(response.status_code, 200)

    def view_uses_correct_template(self, kwargs: dict = None) -> None:
        response = self.client.get(
            reverse(f"{self.basename}-{self.view_name_suffix}", kwargs=kwargs)
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, f"{self.template_name}")


class ListViews(TestViewsBase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        number_of_objects = 25

        for object_id in range(number_of_objects):
            cls.model.objects.create(
                first_name=f"Peter {object_id}",
                second_name=f"Parker {object_id}",
            ) if cls.model == Author else cls.model.objects.create(title=f"{object_id}")

    def pagination_is_twenty(self) -> None:
        response = self.client.get(reverse(f"{self.basename}-{self.view_name_suffix}"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["object_list"]), 20)

    def lists_all_objects(self, key: dict[str, int]) -> None:
        response = self.client.get(
            reverse(f"{self.basename}-{self.view_name_suffix}"), key
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["object_list"]), 5)


class DetailViews(TestViewsBase):
    attributes: dict

    @classmethod
    def setUpTestData(cls) -> None:
        cls.obj = cls.model.objects.create(**cls.attributes)

    def check_exist_obj(self) -> None:
        response = self.client.get(
            reverse(
                f"{self.basename}-{self.view_name_suffix}", kwargs={"pk": self.obj.id}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.obj)

    def check_nonexist_obj(self) -> None:
        response = self.client.get(
            reverse(f"{self.basename}-{self.view_name_suffix}", args=[100])
        )
        self.assertEqual(response.status_code, 404)


class CreateViews(TestViewsBase):
    attributes: dict

    @classmethod
    def setUpTestData(cls):
        if cls.model == Book:
            author = Author.objects.create(first_name='test', second_name='test')
            cls.attributes.update({"author": author.id})

    def create_object(self) -> Type[models.Model]:
        response = self.client.post(reverse(f"{self.basename}-{self.view_name_suffix}"), data=self.attributes)
        print(response)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(f"{self.basename}s-list"))
        obj = self.model.objects.last()
        return obj

    def created_object_has_attributes(self) -> None:
        obj = self.create_object()
        if hasattr(obj, "second_name"):
            self.assertEqual(self.attributes["second_name"], obj.second_name)
        else:
            self.assertEqual(self.attributes["title"], obj.title)

    def created_object_single_in_db(self) -> None:
        self.create_object()
        self.assertEqual(self.model.objects.count(), 1)

    def check_object_accessible_in_detail(self) -> None:
        obj = self.create_object()
        response = self.client.get(reverse(f"{self.basename}-detail", kwargs={"pk": obj.id}))
        self.assertEqual(response.status_code, 200)


