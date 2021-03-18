
from django.contrib import admin
from django.urls import path
from jebouloapp import views


#app_name = 'jebouloapp'

urlpatterns = [
    path('', views.homepageview,  name='homepage'),
    path('gohomepage/', views.gohomepageview,  name='gohomepage'),
    path('signupuser/',views.signupuser, name="signupuserpage"),
    path('userloginview/', views.userloginview, name="userloginpage"),
    path('usersignupview/', views.usersignupview, name="usersignuppage"),
    path('customer/authenticate/',views.userauthenticate),
    path('customer/welcome/',views.customerwelcomeview, name="customerpage"),
    path('userlogout/',views.userlogout),
    path('customer/addannounce/',views.addannounce, name='addannouncepage'),
    path('customer/pubannounce/',views.pubannounce, name='pubannouncepage'),
    path('customer/searchannounce/',views.SearchView.as_view(), name='searchannouncepage'),
    path('customer/resultannounce/', views.ResultView.as_view(), name='resultannouncepage'), 
    path('customer/user/<int:pk>/', views.DetailsUserView.as_view(), name='detailsUser'), 
]
