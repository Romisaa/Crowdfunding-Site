from django import forms
from django.shortcuts import render, redirect
from .models import Post, Like, Category, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# choices = [('Education', 'Education'), ('Health', 'Health'), ('Others', 'Others')]
choices = Category.objects.all().values_list('category_name', 'category_name')

choice_list = []
for i in choices:
    choice_list.append(i)


def home(request):
    return render(request, 'main_page/home.html', {'title': 'Home'})


class PostListView(ListView):
    model = Post
    template_name = 'main_page/posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class CategoryView(ListView):
    model = Category
    template_name = 'main_page/add_category.html'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'content', 'donation_value', 'tag', 'category', 'start_time', 'end_time','imgs')
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'tag': forms.Select(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control'}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        'start_time': forms.DateTimeField(),
        'end_time': forms.DateTimeField(),
        'imgs': forms.ImageField()

    }

    # fields = ['title', 'content', 'donation_value', 'tag', 'start_time', 'end_time']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'main_page/about.html', {'title': 'About'})


def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main_page/posts.html', context)


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value == 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return render(request, 'main_page/posts.html')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body_comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body_comment': forms.Textarea(attrs={'class': 'form-control'})}

    def form_valid(self, form):
        form.instance.post_id = self.kwarges['pk']
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main_page/add_comment.html'
    success_url = "/"
