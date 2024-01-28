from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import PostingListView, PostingCreateView, PostingDetailView, ApplicationsListView, ApplicationCreateView, PostingSearchView, PostingDeleteView

urlpatterns = [
    path("posting/list", PostingListView.as_view(), name="posting-list"),
    path("posting/search", PostingSearchView.as_view(), name="posting-search"),
    path("posting/create", PostingCreateView.as_view(), name="posting-create"),
    path("posting/<int:pk>/details", PostingDetailView.as_view(), name="posting-detail"),
    path("posting/<int:pk>/delete", PostingDeleteView.as_view(), name="posting-delete"),
    path("applications/list", ApplicationsListView.as_view(), name="application-list"),
    path("applications/create", ApplicationCreateView.as_view(), name="application-create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)