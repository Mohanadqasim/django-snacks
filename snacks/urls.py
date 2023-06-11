from django.contrib import admin
from django.urls import path
from .views import Home_page_view, About_page_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Home_page_view.as_view(), name='home'),
    path('about/', About_page_view.as_view(), name='about')
]

