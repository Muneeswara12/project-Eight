from django.shortcuts import render

# Create your views here.
def rohit(request):
    d={'name':'rohit','team':'mumbai indians'}
    return render(request,'mi.html',context=d)