from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_title>/", views.wiki_entry, name="wiki_entry"),
    path("search/", views.search, name="search"),
    path("new-page/", views.new_page, name="new_page"),
    path("edit-page/", views.edit_page, name="edit_page"),
    path("random/", views.random_page, name="random")
]
