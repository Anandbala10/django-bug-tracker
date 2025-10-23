from django.shortcuts import render

# Create your views here.
# tracker/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bug
from .forms import BugForm

# LIST / HOME
def home(request):
    bugs = Bug.objects.all()
    return render(request, 'tracker/home.html', {'bugs': bugs})

# DETAIL
def bug_detail(request, id):
    bug = get_object_or_404(Bug, id=id)
    return render(request, 'tracker/bug_detail.html', {'bug': bug})

# CREATE
def bug_create(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BugForm()
    return render(request, 'tracker/bug_form.html', {'form': form})

# UPDATE
def bug_update(request, id):
    bug = get_object_or_404(Bug, id=id)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('bug_detail', id=bug.id)
    else:
        form = BugForm(instance=bug)
    return render(request, 'tracker/bug_form.html', {'form': form})

# DELETE
def bug_delete(request, id):
    bug = get_object_or_404(Bug, id=id)
    if request.method == 'POST':
        bug.delete()
        return redirect('home')
    return render(request, 'tracker/bug_confirm_delete.html', {'bug': bug})

