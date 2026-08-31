from django.shortcuts import render,redirect
from .forms import RegistrationForm,MovieForm,ProfileForm,ProfilePhotoForm
from django.contrib.auth import authenticate,login
from .models import Movie , Category ,Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def register_view(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user =form.save()
            Profile.objects.create(user=user)
            return redirect("login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )



def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"accounts/login.html",{'error':"invalid username or password"})

    return render(request,'accounts/login.html')


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()

            return redirect("home")

    else:
        form = MovieForm()

    return render(request, "accounts/add_movie.html", {"form": form})

def home(request):
    movies=Movie.objects.all()
    categories=Category.objects.all()
    return render(request,"accounts/home.html",{"categories":categories,"movies":movies})

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)

    trailer = movie.trailer_link

    if "watch?v=" in trailer:
        video_id = trailer.split("watch?v=")[1].split("&")[0]
        trailer = f"https://www.youtube-nocookie.com/embed/{video_id}"

    elif "youtu.be/" in trailer:
        video_id = trailer.split("youtu.be/")[1].split("?")[0]
        trailer = f"https://www.youtube-nocookie.com/embed/{video_id}"

    elif "youtube.com/embed/" in trailer:
        trailer = trailer.replace( "https://www.youtube.com/embed/","https://www.youtube-nocookie.com/embed/")
    return render( request,"accounts/movie_detail.html", { "movie": movie,"trailer": trailer})


def edit_movie(request,id):
    movie=Movie.objects.get(id=id)

    if movie.added_by!=request.user:
        return redirect("movie_detail",id=id)

    if request.method=='POST':
        form=MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_detail",id=id)
    else:
        form=MovieForm(instance=movie)

    return render(request,"accounts/edit_movie.html",{"form":form,"movie":movie})


def delete_movie(request,id):
    movie=Movie.objects.get(id=id)

    if movie.added_by!=request.user:
        return render("movie_detail",id=id)

    if request.method=="POST":
        movie.delete()
        return redirect("home")

    return render(request,"accounts/delete_movie.html",{"movie":movie})

def category_movies(request,id):
    category=Category.objects.get(id=id)
    movies=Movie.objects.filter(category=category)

    return render(request, "accounts/category_movies.html",{"category":category,"movies":movies})


def search_movies(request):
    query=request.GET.get('query','').strip()

    movies=Movie.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))

    return render(request,"accounts/search_results.html",{ "movies":movies,"query":query })

@login_required
def profile(request):

    profile = Profile.objects.get(user=request.user)

    return render(request,"accounts/profile.html",{"profile": profile})

@login_required
def edit_profile(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        form = ProfileForm(  request.POST,  instance=request.user )

        photo_form = ProfilePhotoForm( request.POST, request.FILES, instance=profile  )

        if form.is_valid() and photo_form.is_valid():
            form.save()
            photo_form.save()

            return redirect("profile")

    else:
        form = ProfileForm( instance=request.user )

        photo_form = ProfilePhotoForm( instance=profile)

    return render(request,"accounts/edit_profile.html",{"form": form,"photo_form": photo_form})