from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Required Log In if not logedin  
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    paginate_by = 15
    template_name = "/core/recipe_list.html"