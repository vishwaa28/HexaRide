# -*- coding: utf-8 -*-

"""URL routes for the CarPool web application."""

from django.urls import re_path
from django.contrib import admin

from ui.views import (
    logout_view, my_commutes, new_commute, save_commute, search_commute, signin, signup, user_home,
    welcome, delete_commutes
)

admin.autodiscover()

urlpatterns = [
    re_path(r'^$', welcome, name='home_page'),
    re_path(r'^new_commute$', new_commute, name='new_commute'),
    re_path(r'^user_home$', user_home, name='user_home'),
    re_path(r'^signup', signup, name='signup'),
    re_path(r'^login', signin, name='login'),
    re_path(r'^save_commute$', save_commute, name='save_commute'),
    re_path(r'^logout$', logout_view, name='logout'),
    re_path(r'^search_commute$', search_commute, name='search_commute'),
    re_path(r'^my_commutes', my_commutes, name='my_commutes'),
    re_path(r'^delete_commutes', delete_commutes, name='delete_commutes'),
    re_path(r'^admin/', admin.site.urls),
]
