from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Action
from .models import Utilisateur
from .forms import ActionForm
# Create your views here.

def action_list(request):
    actions = Action.objects.all()
    return render(request, 'cnls/action_list.html', {'actions': actions})

def action_detail(request, pk):
    action = get_object_or_404(Action, pk=pk)
    return render(request, 'cnls/action_detail.html', {'action': action})


def action_new(request):
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.createur = request.user
            action.date_fin = timezone.now()
            action.save()
            return redirect('cnls.views.action_detail', pk=action.pk)
    else:
        form = ActionForm()
    return render(request, 'cnls/action_edit.html', {'form': form})



