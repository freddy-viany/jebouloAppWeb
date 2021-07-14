
from django.contrib import admin
from django.urls import path
from jebouloapp import views


#app_name = 'jebouloapp'

urlpatterns = [
    path('', views.homepageview,  name='homepage'),
    path('signupuser/',views.signupuser, name="signupuserpage"),
    path('customer/modifieprofilview/',views.modifieprofilview, name="modifieprofilpage"),
    path('customer/modifiepasswordview/',views.modifiepasswordview),
    path('gohomepage/', views.homepageview,  name='gohomepage'),
    path('donatepageview/', views.donatepageview,  name='godonatepage'),
    path('userloginview/', views.userloginview, name="userloginpage"),
    path('usersignupview/', views.usersignupview, name="usersignuppage"),
    path('customer/authenticate/',views.userauthenticate),
    path('customer/welcome/',views.customerwelcomeview, name="customerpage"),
     path('customer/welcomepackagezero/',views.customerwelcomeview_Zeroannounce, name="customerpagezeroannounce"),
    path('userlogout/',views.userlogout),
    path('customer/addannounce/',views.addannounce, name='addannouncepage'),
    path('customer/pubannounce/',views.pubannounce, name='pubannouncepage'),
    path('customer/searchannounce/',views.SearchView.as_view(), name='searchannouncepage'),
    path('customer/resultannounce/', views.ResultView.as_view(), name='resultannouncepage'), 
    path('customer/user/<int:pk>/', views.DetailsUserView.as_view(), name='detailsUser'),
    path('paiement/premium/', views.paiementpremiumview,  name='paiementpremiumpage'),
    path('paiement/pro/', views.paiementproview,  name='paiementpropage'),
    path('paiement/vip/', views.paiementvipview,  name='paiementvippage'),
    path('paiement/donate/', views.donateview,  name='donatepage'),
    path('paiementProcess/', views.paiementProcessview,  name='paiementProcess'),
]
