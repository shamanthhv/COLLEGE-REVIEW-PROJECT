from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from blog.models import college

urlpatterns = [ url(r'^$',ListView.as_view(queryset=college.objects.all().order_by("college_name")[:25],template_name="blog/blog.html")),
                url(r'^(?P<pk>\d+)$',DetailView.as_view(model=college,template_name='blog/post.html'))]
