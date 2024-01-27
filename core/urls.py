from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import PostingListView, PostingCreateView, PostingDetailView

urlpatterns = [
    path("posting/list", PostingListView.as_view(), name="posting-list"),
    path("posting/create", PostingCreateView.as_view(), name="posting-create"),
    path("posting/<int:pk>/details", PostingDetailView.as_view(), name="posting-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)