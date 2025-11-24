from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request, 'admin.html')

def add_item(request):
    return render(request, 'add_item.html')
