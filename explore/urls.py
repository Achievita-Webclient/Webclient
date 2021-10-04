from . import views
from django.urls import path

urlpatterns = [
    path('explore', views.ExploreList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
