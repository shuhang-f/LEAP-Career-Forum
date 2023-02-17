from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('signup')
    
    else:
        form = UserCreationForm()
    users = User.objects.all()

    return render(request, 'signup.html', {'form': form, 'users': users})
