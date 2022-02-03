from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Post, Editor



class Home(TemplateView):

    template_name = "home.html"
    

class PostListView(ListView):
    model = Post
    http_method_names = ["get"]
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-id")[0:30]
    template_name = "posts.html"



class EditorView(TemplateView):
    model = Editor
    template_name = "editor.html"
    http_method_names = ["get"]
    