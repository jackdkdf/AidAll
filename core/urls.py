from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import PostingListView

urlpatterns = [
    path("posting/list", PostingListView.as_view(), name="posting-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)