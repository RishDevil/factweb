from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import  UpdateView
from .forms import UserForm,LinkForm
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Link,Voters,UserProfile
from django.shortcuts import render,redirect

class List(ListView):
    model=Link
    template_name = 'a.html'
    queryset = Link.with_votes.all()

def createVote(request,slug):
    link=Link.objects.get(slug=slug)
    vote=Voters.objects.create(link=link,voter=request.user)
    return redirect('fact')

class ListDetail(DetailView):
    model=Link
    template_name = 'detail.html'

class UderPtrofileDetail(DetailView):

    model = get_user_model()
    template_name = "user.html"
    slug_field = 'username'
    def get_object(self, queryset=None):
        user=super(UderPtrofileDetail,self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

#
class UserUpate(UpdateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'upateuser.html'

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]
    def get_success_url(self):
        return  reverse('user',kwargs={"slug":self.request.user})




class LinkCreate(CreateView):
    model=Link
    form_class = LinkForm
    template_name = "create.html"
    def get_success_url(self):
        return reverse('fact')

