from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('home',views.home,name='home'),
    path('logout',views.userLogout,name='logout'),
    # path('api/medicalsummary', views.medicalsummaryView.as_view()),
    # path('api/medicalsummary/<int:pk>', views.medicalsummaryView.as_view()),
    path('medicalsummary',views.getAllMedicalSummary,name='getAllMedicalSummary'),
    path('medicalsummary/<int:pk>',views.getOneMedicalSummary,name='getOneMedicalSummary'),
    path('addOneRecord',views.addOneRecord,name='addOneRecord'),
    path('updateRecord/<int:pk>',views.updateRecord,name='updateRecord'),
    path('deleteRecord/<int:pk>',views.deleteRecord,name='deleteRecord'),
]