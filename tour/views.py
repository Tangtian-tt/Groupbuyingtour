from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tour,Review
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def tourhome(request):
    searchTerm = request.GET.get('searchTour')
    if searchTerm:
        tour_list = Tour.objects.filter(title_contains=searchTerm)
    else:
        tour_list = Tour.objects.all()
    paginator = Paginator(tour_list, 3)
    page_number = request.GET.get('page', 1)
    tours = paginator.page(page_number)
    return render(request,'tourhome.html',{'searchTerm':searchTerm,'tours':tours})
    # return HttpResponse('<h1>欢迎来到tour应用首页</h1>')

def home(request):
    return render(request,'home.html',
                  {'name':'TT'})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})


def tourdetail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    reviews = Review.objects.filter(tour=tour)
    return render(request, 'tourdetail.html', {'tour':
    tour,'reviews':reviews})
@login_required
def createtourreview(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'GET' :
      return render(request, 'createtourreview.html',
    {'form':ReviewForm , 'tour':tour})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.tour = tour
            newReview.save()
            return redirect('tourdetail',newReview.tour.id)
        except ValueError:
            return render(request,'createtourreview.html',
            {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updatetourreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatetourreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('tourdetail', review.tour.id)
        except ValueError:
            return render(request, 'updatetourreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})
@login_required
def deletetourreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('tourdetail', review.tour.id)
