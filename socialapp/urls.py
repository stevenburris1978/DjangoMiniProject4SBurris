from django.urls import path

from . import views
app_name = 'socialapp'
urlpatterns = [
    # ex: /socialapp/
    path("", views.index, name="index"),
    # ex: /socialapp/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /socialapp/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /socialapp/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
