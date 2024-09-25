from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('disorders_of_women',views.disorders_of_women,name='disorders_of_women'),
    path('skin_disorders',views.skin_disorders,name='skin_disorders'),
    path('cardiac_disorders',views.cardiac_disorders,name='cardiac_disorders'),

    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
   
    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_add_news',views.admin_add_news,name='admin_add_news'),
    path('admin_news_view',views.admin_news_view,name='admin_news_view'),
    path('admin_appointment_view',views.admin_appointment_view,name='admin_appointment_view'),
    path('admin_delete_appointments/<int:id>/',views.admin_delete_appointments,name='admin_delete_appointments'),
    path('admin_contact_view',views.admin_contact_view,name='admin_contact_view'),
    path('admin_update_news/<int:id>/',views.admin_update_news,name='admin_update_news'),
    path('admin_delete_news/<int:id>/',views.admin_delete_news,name='admin_delete_news'),
    path('admin_delete_contact/<int:id>/',views.admin_delete_contact,name='admin_delete_contact'),
    path('home', views.home, name='home'),
]