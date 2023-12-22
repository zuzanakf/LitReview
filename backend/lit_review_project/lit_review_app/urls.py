from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('upload/', views.document_upload, name='document_upload'),
    path('signup/', views.signup, name='signup'),
]
