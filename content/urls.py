from django.urls import path
from . import views

urlpatterns = [
    path("contents/", views.ContentMultiplyView.as_view()),
    path("contents/filter/", views.ContentFilterView.as_view()),
    path("contents/<content_id>/", views.ContentCRUDView.as_view()),
]
