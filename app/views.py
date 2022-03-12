from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Client
import requests
from django.views.generic import ListView
from django.contrib import messages
from .forms import ClientForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def home_view(request):
    context = {}
    # create object of form
    form = ClientForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, "home.html", context)

# @login_required(login_url='login')
def services(request):
    return render(request, 'services.html')


# @login_required(login_url='login')
def blog(request):
    return render(request, 'blog.html')


# @login_required(login_url='login')
def registration(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        form = ClientForm()
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            registration = Client(name=name, email=email, password=password)
            registration.save()
            messages.success(request, 'Cheers...! you have successfully registered with us Now Login!')
        return render(request, 'registration.html')



def loginuser(request):
    # hgfhfhfffh
    # # import pdb; pdb.set_trace()
    # if request.method == 'POST':
    #     # AuthenticationForm_can_also_be_used__
    #     name = request.POST('name')
    #     password = request.POST('password')
    #     print(password,name)
    #     user = authenticate(request, name = name, password = password)
    #     if user is not None:
    #         form = login(request, user)
    #         messages.success(request, f' welcome {name} !!')
    #         return redirect('home')
    #     else:
    #         messages.info(request, f'account done not exit plz sign in')
    # form = ClientForm()
     print("hi Himnai")
     return render(request, 'login.html')



# def loginuser(request):
#  import pdb; pdb.set_trace()
#  if not request.user.is_authenticated:
#   if request.method == "POST":
#    form = ClientForm(request=request, data=request.POST)
#    if form.is_valid():
#     name = form.cleaned_data['name']
#     password = form.cleaned_data['password']
#     user = authenticate(name=name, password=password)
#     print(name, password)
#     if user is not None:
#      login(request, user)
#      messages.success(request, 'Logged in Successfully !!')
#      return HttpResponseRedirect('/home/')
#   else:
#    form = ClientForm()
#   return render(request, 'login1.html', {'form':form})
#  else:
#   return HttpResponseRedirect('/home/')



# @login_required(login_url='login')
def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
 
# @login_required(login_url='login') 
def aboutus(request):
    return render(request, 'aboutus.html')

# def reset(request):
#   return render(request,'reset.html')

 
# @login_required(login_url='login') 
def data(request):
    # new_data= Client.objects.all()   #return all Data

    new_data =Client.objects.all()  # fetching all post objects from database
    p = Paginator(new_data, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'database.html', context)

    # new_data = Contact.objects.all()
    # paginator = Paginator(new_data,2) # Show 2 contacts per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'database.html', {"page_obj": page_obj,"Database": new_data})
    # new_data= Client.objects.filter(password="gaurav")   # Filter Data
    # new_data= Client.objects.exclude(password="gaurav")   # Exclude Data
    # new_data= Client.objects.order_by("id")   # Order By Assending 
    # new_data= Client.objects.order_by("-id")   # Order By descending by adding - before
    # new_data= Client.objects.order_by("?")# Ordered randomely
    # new_data= Client.objects.order_by("id").reverse() # Reverse Data
    # new_data= Client.objects.order_by("id").reverse()[0:6] # Reverse 6 Data 
    # new_data= Client.objects.values("name","email")# Getting only desired values
    # new_data= Client.objects.values_list()    # Getting data in tuples
    # new_data= Client.objects.values_list("id","name")    # Getting data in tuples with required field
    # new_data= Client.objects.values_list("id","name", named=True)    # make it named tuples 
    # print("Return", new_data)
    # print("SQL QUERY",new_data.query)
    # return render(request, 'database.html',{"Database": new_data, "page_object": page_object})
