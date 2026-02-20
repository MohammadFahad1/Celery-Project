from django.shortcuts import render
from celeryproject.celery import add
from myapp.tasks import sub

# Using delay function
""" def home(request):
    print("Results: ")
    result1 = add.delay(10,20)
    print("Result 1: ", result1)
    
    result2 = sub.delay(80, 100)
    print("Result 2: ", result2)
    return render(request, 'home.html') """
    
# Using apply_async
""" def home(request):
    print("Results: ")
    result1 = add.apply_async(args=[10,20])
    print("Result 1: ", result1)
    
    result2 = sub.apply_async(args=[80, 100])
    print("Result 2: ", result2)
    return render(request, 'home.html') """

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')