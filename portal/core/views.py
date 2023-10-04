from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import JobApplication, UserProfile, PortalPhotos

from django.contrib.auth import logout

from item.models import Department, Category, Item

from .forms import SignupForm, UserProfileForm, UserProfileEditForm, JobApplicationForm



def index(request):
    items = Item.objects.filter(available=True)[0:20]
    departments = Department.objects.all()
    categories = Category.objects.all()


    return render(request, 'core/index.html', {
        'categories':categories,
        'departments':departments,
        'items':items,

    })



def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')  
    else:
        form = UserProfileForm()
    return render(request, 'core/user_profile_form.html', {'form': form})


def contact(request):
    return render(request, 'core/contact.html')


@login_required
def userprofile(request):
    profiles = UserProfile.objects.all()

    return render(request, 'core/userprofile.html', {
        'profiles': profiles
    })


def privacyPolicy(request):
    return render(request, 'core/Privacypolicy.html')

def about(request):
    return render(request, 'core/about.html')

def myBasket(request):
    applications= JobApplication.objects.all()
    return render(request, 'core/myBasket.html', {
        'applications':applications
    })

def termofuse(request):
    return render(request, 'core/termsofuse.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/create-profile/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })




@login_required
def edit_user_profile(request):
    user_profile = request.user.userprofile  # Gets user's profile associated with the logged-in user

    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/user profile/')  
    else:
        form = UserProfileEditForm(instance=user_profile)  

    return render(request, 'core/user_profile_edit_form.html', {'form': form})



@login_required
def apply_for_job(request):
    user_profile = request.user.userprofile
    position = "Position placeholder"  # Retrieve the position object based on 'position_id', you can adjust this based on your implementation

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user_profile = user_profile
            application.position = position
            application.save()
            return redirect('/')  
    else:
        form = JobApplicationForm()

    return render(request, 'core/job_application_form.html', {'form': form})


def base_logos(request):
    logo = PortalPhotos.objects.all()

    return render(request, 'base.html', {
        'logo': logo
    })