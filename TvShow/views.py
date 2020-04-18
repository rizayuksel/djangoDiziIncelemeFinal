from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import TvShow, Comment

# Create your views here.

def index(request):
    keyword = request.GET.get("keyword")#arama yapmak için
    if keyword:
        series = TvShow.objects.filter(title__contains = keyword)
        return render(request, "index.html", {"series":series})
    series = TvShow.objects.all() #Autos veri tabanındaki tüm verileri sözlük yapısıyla aldık
    return render(request,"index.html",{"series":series})
 
def crime(request):
    series = TvShow.objects.filter(kind__contains = "Suç")
    return render(request,"crime.html",{"series":series})

def comedy(request):
    series = TvShow.objects.filter(kind__contains = "Komedi")
    return render(request,"comedy.html",{"series":series})

def mystery(request):
    series = TvShow.objects.filter(kind__contains = "Gizem")
    return render(request,"mystery.html",{"series":series})

def scifi(request):
    series = TvShow.objects.filter(kind__contains = "Bilim Kurgu")
    return render(request,"scifi.html",{"series":series})

def sport(request):
    series = TvShow.objects.filter(kind__contains = "Spor")
    return render(request,"sport.html",{"series":series})

def detail(request,id):
    series =get_object_or_404(TvShow, id = id)
    comments = series.comments.all()
    return render(request, "detail.html",{"series":series,"comments":comments})

def comment(request,id):
    series = get_object_or_404(TvShow, id = id)
    if request.method == "POST":
        username = request.user
        content = request.POST.get("content")

        newComment = Comment(username = username, content = content)
        newComment.series = series
        newComment.save()
    return redirect(reverse("TvShow:detail", kwargs={"id":id}))
