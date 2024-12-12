from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'mainapp/signup.html', {'form': form})