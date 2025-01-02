from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('upload/', views.upload_image, name='upload_image'),
]
