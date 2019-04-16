"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

from .views import home
from rango import views


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/accounts/add_profile'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('rango/', include('rango.urls')),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/add_profile/', views.register_profile, name='add_profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/users/<int:user_id>/', views.user_info, name='user_info'),
    path('accounts/users/', views.users, name='users'),
    path('accounts/', include('registration.backends.simple.urls')),
]
# Целесообразно ли использование settings.DEBUG?
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

