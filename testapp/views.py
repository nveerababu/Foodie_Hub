from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
def home_view(request):
    return render (request,'home.html')

from testapp.models import MenuItem
@login_required
def manage_menu_view(request):
    items = MenuItem.objects.all()
    return render (request,'manage_menu.html',{'items':items})


from django.http import HttpResponseRedirect
from testapp.forms import MenuItemForm
def add_menu_item(request):
    form =  MenuItemForm()
    if request.method == 'POST':
        form =  MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_menu')
    return render(request, 'add_menu_item.html', {'form':form})  

from testapp.models import MenuItem
def delete_menu_item(request,id): 
     item =  MenuItem.objects.get(id=id)
     item.delete()
     return redirect('manage_menu')

from testapp.forms import MenuItemForm
def edit_menu_item(request,id):
    item =  MenuItem.objects.get(id=id)
    form = MenuItemForm(instance=item)
    if request.method == 'POST':
        form = MenuItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('manage_menu')
    return render(request, 'edit_menu_item.html', {'form':form}) 

from django.contrib.auth import logout
def logout_view(request):
    logout(request)

    return render (request,'logout.html')
def about_view(request):
    return render (request,'about.html')

def contactus_view(request):
    return render (request,'contactus.html')




















from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
def signupform_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    return render(request, 'signup.html', {'form': form})



