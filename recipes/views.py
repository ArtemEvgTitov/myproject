from . import models
from .forms import PostForm
from .models import Recipe
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, DetailView


def index(request):
    recipes = Recipe.objects.filter(delete=False)[:5]
    context = {'recipes': recipes, 'title': 'Новые рецепты'}
    return render(request, 'recipes/index.html', context)


def all_recipes(request):
    recipes = Recipe.objects.filter(delete=False)
    context = {'recipes': recipes, 'title': 'Все рецепты'}
    return render(request, 'recipes/index.html', context)

def my_recipes(request, user_id):
    recipes = Recipe.objects.filter(delete=False, author_id=user_id)
    context = {'recipes': recipes, 'title': 'Ваши рецепты'}
    return render(request, 'recipes/index.html', context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            steps_cooking = form.cleaned_data['steps_cooking']
            time_for_cooking = form.cleaned_data['time_for_cooking']
            author = request.user
            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            recipe = Recipe(title=title, description=description, steps_cooking=steps_cooking,
                            time_for_cooking=time_for_cooking, photo=photo, author=author)
            recipe.save()
            return render(request, 'recipes/index.html',
                          {'form': form})
    else:
        form = PostForm()
    return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Новый рецепт'})


def delete_post(request, **kwargs):
    recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
    recipe.delete = True
    recipe.save()
    return index(request)


def update_post(request, **kwargs):
    recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.data['title'] = recipe.title
            recipe.title = form.cleaned_data['title']
            recipe.description = form.cleaned_data['description']
            recipe.steps_cooking = form.cleaned_data['steps_cooking']
            recipe.time_for_cooking = form.cleaned_data['time_for_cooking']
            recipe.photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            recipe.save()
    else:
        form = PostForm()
    return render(request, 'recipes/recipe_form.html',
                  {'form': form, 'title': 'Редактирование рецепта'})
