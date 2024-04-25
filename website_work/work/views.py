from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Post, BaseRegisterForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# class CustomerView(ListView):
#     ...


class ExecutorView(ListView):
    ordering = '-date'
    template_name = 'executor.html'
    context_object_name = 'executor'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(category='or') .exclude(user=self.request.user)



class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'



