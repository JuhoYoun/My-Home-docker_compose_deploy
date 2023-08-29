from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
# from accountapp.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]
# Create your views here.
# @login_required
# def hello_world(request):
#     # return HttpResponse("Hello World")
#     if request.method == "POST":
#
#         temp = request.POST.get('hello_world_input')
#
#         new_hello_world = HelloWorld()
#         new_hello_world.text = temp
#         new_hello_world.save()
#
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#     else:
#         # return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
#         hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')  # 계정 만드는데 성공했다면 어느 URL로 redirect 될것인가
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'  # 인자로 넘겨 받은 pk와 일치하는 Model (여기선 User) 객체를 target_user 란 변수로 템플릿에 넘겨준다
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home')  # 계정 만드는데 성공했다면 어느 URL로 redirect 될것인가
    template_name = 'accountapp/update.html'

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
