from typing import Type, Union

from django.test import TestCase
from django.urls import reverse
from django.db import models

from booksandauthors.models import Author


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
