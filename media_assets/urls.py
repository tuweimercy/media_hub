from django.urls import path
from . import views

# create the namespace
app_name = 'media_assets'

urlpatterns = [
    # '' :root path : 8000/
    path('', views.dashboard_view,name='dashboard'),
    path('my_media/',views.my_media_view,name='my_media'),
    path('upload/', views.upload_view, name='upload_media'),
    #media full detail view
    path('media/<int:pk>',views.media_detail_view,
    name='media_detail'),
    path('media/<int:pk>/edit/', views.edit_media_view,
    name='edit_media'),
    path('madia/<int:pk>/delete/', views.delete_media_view,
    name='delete_media'),
]