from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import Processor, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply

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

def list(request):
    context = {
        "processors": Processor.objects.all(),
        "motherboards": Motherboard.objects.all(),
        "memories": Memory.objects.all(),
        "storages": Storage.objects.all(),
        "videocards": VideoCard.objects.all(),
        "cases": Case.objects.all(),
        "powersupplies": PowerSupply.objects.all(),
    }
    return render(request, 'mainapp/list.html', context)