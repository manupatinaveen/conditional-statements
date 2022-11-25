from django.shortcuts import render

# Create your views here.
def jinja_print (request):
    return render(request,'jinja_print.html', context={'name':'Naveen','age':20})
def condition(request):
    d={'a':10000,'b':3000,'c':400}
    return render(request,'condition.html',context=d)