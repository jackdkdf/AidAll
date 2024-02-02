from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Posting, Applications

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
        object_list = Posting.objects.filter(title__icontains=query)
        return object_list

class PostingDetailView(LoginRequiredMixin, DetailView):
    model = Posting

class PostingCreateView(LoginRequiredMixin, CreateView):
    model = Posting
    fields = (
        'title',
        'organization',
        'country',
        'region',
        'city',
        'hours',
        'description',
        )
    success_url = reverse_lazy('posting-list')

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super(PostingCreateView, self).form_valid(form)
    

class PostingUpdateView(LoginRequiredMixin, UpdateView):
    model = Posting
    fields = "__all__"

class PostingDeleteView(LoginRequiredMixin, DeleteView):
    model = Posting
    success_url = reverse_lazy('posting-list')

class ApplicationsListView(LoginRequiredMixin, ListView):
    model = Applications
    paginate_by = 15

    def get_queryset(self):
        object_list = Applications.objects.filter(posting__poster=self.request.user)
        return object_list
    
class ApplicationsDetailView(LoginRequiredMixin, DetailView):
    model = Applications
    exclude = ['']

class ApplicationsCreateView(LoginRequiredMixin, CreateView):
    model = Applications

# Handle Ajax POST Request for creating applications
# Takes FormData from apply-form in posting_detail.html
# Respective fields are set based on the data sent in the POST request -
# the name of the form element corresponds to the key of the value in the POST dictionary
def apply(request):
    if request.method == 'POST':
        posting = Posting.objects.filter(id=request.POST["posting_id"])[0]
        applicant = request.user
        fName = request.POST['firstName']
        lName = request.POST['lastName']
        country = request.POST['country']
        region = request.POST['region']
        city = request.POST['city']
        message = request.POST['message']
        existing_app = Applications.objects.filter(posting=posting, applicant=applicant)
        print(len(existing_app))
        if len(existing_app) == 0:
            application = Applications(
                posting = posting,
                applicant = applicant,
                firstName = fName,
                lastName = lName,
                country = country,
                region = region,
                city = city,
                message = message,
                status = "PENDING"
                )
            
            application.save()
            return HttpResponse("Created application!")
        else:
            print("Updating application")
            existing_app = existing_app[0]
            existing_app.firstName = fName
            existing_app.lastName = lName
            existing_app.country = country
            existing_app.region = region
            existing_app.city = city
            existing_app.message = message
            existing_app.save()
            return HttpResponse("Updated application!")
    else:
        return HttpResponse("Request method is not a POST")
