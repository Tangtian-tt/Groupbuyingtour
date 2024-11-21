from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Abroad,Review
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def abroadhome(request):
    searchTerm = request.GET.get('searchAbroad')
    if searchTerm:
        abroad_list = Abroad.objects.filter(title_contains=searchTerm)
    else:
        abroad_list = Abroad.objects.all()
    paginator = Paginator(abroad_list, 3)
    page_number = request.GET.get('page', 1)
    abroads = paginator.page(page_number)
    return render(request,'abroadhome.html',{'searchTerm':searchTerm,'abroads':abroads})
    # return HttpResponse('<h1>欢迎来到abroad应用首页</h1>')

def home(request):
    return render(request,'home.html',
                  {'name':'TT'})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})


def abroaddetail(request, abroad_id):
    abroad = get_object_or_404(Abroad, pk=abroad_id)
    reviews = Review.objects.filter(abroad=abroad)
    return render(request, 'abroaddetail.html', {'abroad':
    abroad,'reviews':reviews})
@login_required
def createabroadreview(request, abroad_id):
    abroad = get_object_or_404(Abroad, pk=abroad_id)
    if request.method == 'GET' :
      return render(request, 'createabroadreview.html',
    {'form':ReviewForm , 'abroad':abroad})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.abroad = abroad
            newReview.save()
            return redirect('abroaddetail',newReview.abroad.id)
        except ValueError:
            return render(request,'createabroadreview.html',
            {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updateabroadreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updateabroadreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('abroaddetail', review.abroad.id)
        except ValueError:
            return render(request, 'updateabroadreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})
@login_required
def deleteabroadreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('abroaddetail', review.abroad.id)
