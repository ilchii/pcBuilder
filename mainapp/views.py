from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mainapp.models import Build, Processor, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply

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

@login_required
def create_build(request):
    if request.method == "POST":
        # Get the user
        user = request.user

        # Get selected components
        build_name = request.POST.get("build_name", "Untitled Build")
        processor = Processor.objects.get(id=request.POST["processor"]) if request.POST.get("processor") else None
        motherboard = Motherboard.objects.get(id=request.POST["motherboard"]) if request.POST.get("motherboard") else None
        memory = Memory.objects.get(id=request.POST["memory"]) if request.POST.get("memory") else None
        storage = Storage.objects.get(id=request.POST["storage"]) if request.POST.get("storage") else None
        video_card = VideoCard.objects.get(id=request.POST["video_card"]) if request.POST.get("video_card") else None
        case = Case.objects.get(id=request.POST["case"]) if request.POST.get("case") else None
        power_supply = PowerSupply.objects.get(id=request.POST["power_supply"]) if request.POST.get("power_supply") else None

        # Create the Build
        Build.objects.create(
            user=user,
            name=build_name,
            processor=processor,
            motherboard=motherboard,
            memory=memory,
            storage=storage,
            video_card=video_card,
            case=case,
            power_supply=power_supply,
        )

        return redirect("index")  # Redirect to a list of builds or another page after saving

    # Load available components for selection
    context = {
        "processors": Processor.objects.all(),
        "motherboards": Motherboard.objects.all(),
        "memories": Memory.objects.all(),
        "storages": Storage.objects.all(),
        "videocards": VideoCard.objects.all(),
        "cases": Case.objects.all(),
        "powersupplies": PowerSupply.objects.all(),
    }
    return render(request, "mainapp/list.html", context)

def completed_builds(request):
    builds = Build.objects.all()
    return render(request, 'mainapp/completed_builds.html', {'builds': builds})

def build_detail(request, build_id):
    build = get_object_or_404(Build, id=build_id)
    return render(request, 'mainapp/build_detail.html', {'build': build})