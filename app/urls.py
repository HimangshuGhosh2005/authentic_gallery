from django.urls import path
from . import views
urlpatterns = [
    path("",views.gallery,name="gallery"),
    path("loging",views.logingin,name="loginpage"),
    path('signup',views.signup,name="signingup"),
    path('logouting',views.logouting,name='logoutiing'),
    path('dele',views.delimg,name='delimage'),
    path('view',views.view,name='view'),
]
