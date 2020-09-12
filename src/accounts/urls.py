
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
                  path('', views.get_profiles_list),
                  path('add/', views.add_profile),
                  path('show/<slug>', views.get_profile),
                  path('edit/<slug>', views.edit_profile)]
