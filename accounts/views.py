from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from accounts.forms import ProfileForm, UserForm, UserUpdateForm, ProfileUpdateForm
from accounts.models import AuthorProfile


def home(request):
    return render(request, 'accounts/accounts_home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            return redirect('blogs_home')
    else:
         form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})


def register(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            gender = p_form.cleaned_data.get('gender')
            date_of_birth = p_form.cleaned_data.get('date_of_birth')
            contact_number = p_form.cleaned_data.get('contact_number')

            author = AuthorProfile.objects.create(author=user, gender=gender, date_of_birth=date_of_birth,
                                                      contact_number=contact_number)
            p_form = ProfileForm(request.POST, instance=author)
            p_form.save()

            messages.success(request, 'Your account has been created!')
            return redirect('login')
    else:
        u_form = UserForm()
        p_form = ProfileForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/register.html', context)


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.authorprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Account updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.authorprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)

