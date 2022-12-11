from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    form = UserRegisterForm()
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')

            return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')