from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Post, BaseRegisterForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
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
    model = Post
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list')

class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'product.html'
    context_object_name = 'post'



class ExecutorView(LoginRequiredMixin, ListView):
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


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'



