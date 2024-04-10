# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        # Process the form submission
        catchaText = request.POST.get('catchaText')
        
        if catchaText:
            return HttpResponse(f'{catchaText}')
        else:
            return HttpResponse('Please provide catchaText.')
    else:
        return HttpResponse('Method not allowed.')
    pass