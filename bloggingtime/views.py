from django.shortcuts import render, get_object_or_404
from .models import Blogging

# Create your views here.
def allblogs(request):
    blogs = Blogging.objects
    return render(request, 'bloggingtime/allblogs.html', {'blogs':blogs })

def detail(request, blog_id):
    detailblog= get_object_or_404(Blogging, pk=blog_id)
    return render(request, 'bloggingtime/detail.html', {'blog':detailblog})
