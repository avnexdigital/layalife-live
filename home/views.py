from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'page.html') 

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dateofbirth = request.POST.get('dateofbirth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        blank1 = request.POST.get('blank1')
        blankw = request.POST.get('blankw')
        blankh = request.POST.get('blankh')
        blankf = request.POST.get('blankf')
        blanki = request.POST.get('blanki')
        blanks = request.POST.get('blanks')
        blankv = request.POST.get('blankv')
        blankg = request.POST.get('blankg')
        blankn = request.POST.get('blankn')
        blankt = request.POST.get('blankt')
        blanke = request.POST.get('blanke')

        contact = Contact( name=name, dateofbirth=dateofbirth,  email=email, phone=phone,  blank1=blank1, blankw=blankw, blankh=blankh , blankf=blankf, blanki=blanki, blanks=blanks, blankv=blankv, blankg=blankg, blankn=blankn, blankt=blankt, blanke=blanke,  date=datetime.now() )
        contact.save()
        messages.success(request, 'Profile details registered.')

    

    return render(request, 'jobreg.html')


def search(request):


    
    return render(request, 'search.html')