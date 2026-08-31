from django.urls import path
from .import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("home/",views.home,name='home'),
    path("movie/add/", views.add_movie, name="add_movie"),
    path("movie/<int:id>/",views.movie_detail,name="movie_detail"),
    path("movie/<int:id>/edit",views.edit_movie,name="edit_movie"),
    path("movie/<int:id>/delete",views.delete_movie,name="delete_movie"),
    path("category/<int:id>/",views.category_movies,name="category_movies"),
    path("search/",views.search_movies,name="search_movies"),
    path("profile/",views.profile,name="profile"),
    path("profile/edit",views.edit_profile,name="edit_profile"),
]