from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class postListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class userPostListView(ListView):
    model=Post
    template_name = 'blog/user_blog.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        #now get the username from the url
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class postDetailView(DetailView):
    model = Post


class postCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # to link post with current user id
    def form_valid(self, form):
        # set up the link
        form.instance.author = self.request.user
        return super().form_valid(form)


class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # to link post with current user id
    def form_valid(self, form):
        # set up the link
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class postDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
