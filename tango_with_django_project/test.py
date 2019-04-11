# -*- coding: utf-8 -*-
from django.test import TestCase
from django.urls import reverse


class TestHomePage(TestCase):

    def test_uses_index_template(self):
        response = self.client.get(reverse("rango:index"))
        self.assertTemplateUsed(response, "rango/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("rango:index"))
        self.assertTemplateUsed(response, "base.html")
