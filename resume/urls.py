from django.urls import path
from .import views

app_name = "resume"


urlpatterns = [
    path("resume/", views.PostListView.as_view(), name= 'posts' ),
    path("edit/", views.EditorView.as_view(), name= 'editor' ),

]
