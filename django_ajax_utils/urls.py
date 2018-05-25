from django.urls import path

from file_upload.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
