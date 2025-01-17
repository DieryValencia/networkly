from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm ##
from .models import Profile##

# Create your views here.

def home(request):
    return render(request, 'networkly_app/home.html')


@login_required
def products(request):
    return render(request, 'networkly_app/products.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):

    data = {
        'form' : CustomUserCreationForm()
    }


    if request.method == 'POST' :
        user_creation_form = CustomUserCreationForm(data= request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('home')

    return render(request, 'registration/register.html', data)

##
def profile_view(request):
    try:
        # Obtener el perfil asociado al usuario
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        # el formulario es POST, actualizamos el perfil
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la página del perfil después de guardar
    else:
        #un GET, mostramos el perfil y el formulario de edición
        form = ProfileForm(instance=profile)

    return render(request, 'networkly_app/perfil.html', {'profile': profile, 'form': form})
##




