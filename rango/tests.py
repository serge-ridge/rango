from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from datetime import timedelta
from rango.models import Category, Page


class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        """
                ensure_views_are_positive should results True for
                categories where views are zero or positive
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a category
        an appropriate slug line is created
        i.e. "Random Category String" -> "random-category-string"
        """
        cat = Category()
        cat.name = 'Random Category String'
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def add_cat(self, name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views = views
        c.likes = likes
        c.save()
        return c

    def test_index_view_with_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        self.add_cat('test', 1, 1)
        self.add_cat('temp', 1, 1)
        self.add_cat('tmp', 1, 1)
        self.add_cat('tmp test temp', 1, 1)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)


class PageMethodTests(TestCase):

    def test_page_visits_arent_in_future(self):
        cat = Category(name='test')
        cat.save()
        page = Page()
        page.category = cat
        page.title = "Test page"
        page.url = "http://test.com"
        future_time = now() + timedelta(days=1)
        page.first_visit = future_time
        page.last_visit = future_time
        page.save()
        self.assertLessEqual(page.first_visit, now())
        self.assertLessEqual(page.last_visit, now())
