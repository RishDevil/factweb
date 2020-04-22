from django.urls import path,include

from .views import List,createVote
from .views import ListDetail,UderPtrofileDetail,UserUpate,LinkCreate
urlpatterns = [

    path('',List.as_view(),name='fact'),
    path('vote/<slug>/',createVote,name='vote'),
    path('linkdetail/<slug>/',ListDetail.as_view(),name='linkdetail'),
    path('user/<slug>/',UderPtrofileDetail.as_view(),name="user"),
    path('profileedit/',UserUpate.as_view(),name="profileedit"),
    path('create/',LinkCreate.as_view(),name="create")

]
