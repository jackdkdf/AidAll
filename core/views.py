from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Posting

# Redirect to login page if not logged in
# View for handling all volunteer postings
class PostingListView(LoginRequiredMixin, ListView):
    model = Posting
    paginate_by = 15
    template_name = "/core/posting_list.html"

# Listview with queryset filtered by user's search
class PostingSearchView(LoginRequiredMixin, ListView):
    model = Posting
    paginate_by = 15
    template_name = "/core/posting_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Posting.objects.filter(name__icontains=query)
        return object_list

class PostingDetailView(DetailView):
    model = Posting

# TODO
class PostingOfTheDayView(DetailView):
    model = Posting

class PostingCreateView(CreateView):
    model = Posting
    fields = "__all__"
    success_url = reverse_lazy('posting-list')

class PostingUpdateView(UpdateView):
    model = Posting
    fields = "__all__"

class PostingDeleteView(DeleteView):
    model = Posting
    success_url = reverse_lazy('posting-list')