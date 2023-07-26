from typing import Type

from django.test import TestCase
from django.urls import reverse
from django.db import models

from booksandauthors.models import Author


class ListViews(TestCase):
    basename: str
    model: Type[models.Model]
    view_name_suffix: str
    template_name: str

    @classmethod
    def setUpTestData(cls) -> None:
        number_of_objects = 23

        for object_id in range(number_of_objects):
            cls.model.objects.create(
                first_name=f"Peter {object_id}",
                second_name=f"Parker {object_id}",
            ) if cls.model == Author else cls.model.objects.create(
                title=f"{object_id}"
            )

    def view_url_exists_at_desired_location(self) -> None:
        response = self.client.get(f"/{self.basename}/")
        self.assertEqual(response.status_code, 200)

    def view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse(f"{self.basename}-{self.view_name_suffix}"))
        self.assertEqual(response.status_code, 200)

    def view_uses_correct_template(self) -> None:
        response = self.client.get(reverse(f"{self.basename}-{self.view_name_suffix}"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, f"{self.template_name}")

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
        self.assertEqual(len(response.context["object_list"]), 3)
