from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

class PostView(View):
    '''Vivod Zapisi'''
    def get(self,request):
        posts = Post.objects.all()
        return render(request, 'testapp/test.html', {'post_list': posts})

class PostDetail(View):
    ''' otdelniy post'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'testapp/test_detail.html', {'post': post})

