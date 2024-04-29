from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Post, ReplyPost
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, ReplyForm
from django.urls import reverse_lazy


class CustomerCreateView(LoginRequiredMixin, CreateView):
    """Создание заказа"""

    form_class = PostForm
    model = Post
    template_name = 'customer.html'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.category = 'or'
        return super().form_valid(form)


class CustomerUserView(LoginRequiredMixin, ListView):
    """Список заказов пользователя"""
    ordering = '-date'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_post'] = True
        return context


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """Изменить заказ"""
    form_class = PostForm
    model = Post
    template_name = 'customer.html'


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """Удалить заказ"""
    model = Post
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list')


class CustomerDetailView(LoginRequiredMixin, DetailView):
    """Просмотр откликов"""
    model = Post
    template_name = 'customer_reply.html'
    context_object_name = 'post'


class ExecutorView(ListView):
    """Исполнитель"""

    ordering = '-date'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(category='or') .exclude(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_post'] = False
        return context


class ReplyCreateView(LoginRequiredMixin, DetailView):
    """Создвние отклика"""
    form_class = ReplyForm
    model = ReplyPost
    template_name = 'reply_create.html'

    def form_valid(self, form):
        reply = form.save(commit=False)
        # reply.user = self.request.user
        # reply.category = 'or'
        return super().form_valid(form)


