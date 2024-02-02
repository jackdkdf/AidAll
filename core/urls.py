from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import PostingListView, PostingCreateView, PostingDetailView, ApplicationsListView, ApplicationsDetailView, ApplicationsCreateView, PostingSearchView, PostingDeleteView, apply

urlpatterns = [
    path("posting/list", PostingListView.as_view(), name="posting-list"),
    path("posting/search", PostingSearchView.as_view(), name="posting-search"),
    path("posting/create", PostingCreateView.as_view(), name="posting-create"),
    path("posting/<int:pk>/details", PostingDetailView.as_view(), name="posting-detail"),
    path("posting/<int:pk>/delete", PostingDeleteView.as_view(), name="posting-delete"),
    path("applications/list", ApplicationsListView.as_view(), name="application-list"),
    path('applications/<int:pk>/details', ApplicationsDetailView.as_view(), name="application-detail"),
    path("applications/create", ApplicationsCreateView.as_view(), name="application-create"),
    path("applications/create/ajax", apply, name="apply"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)