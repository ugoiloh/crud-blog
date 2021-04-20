from django.contrib import admin
from django.urls import path
from .views import HomePage, PostDetailView

app_name = 'newsfeed'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view() , name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail')
]