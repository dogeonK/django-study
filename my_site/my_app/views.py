from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):
    return render(request, 'my_app/variable.html')