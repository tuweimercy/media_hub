from django.urls import path
from . import views

# create the namespace
app_name = 'media_assets'

urlpatterns = [
    # '' :root path : 8000/
    path('', views.dashboard_view,name='dashboard'),
]