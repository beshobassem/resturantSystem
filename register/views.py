from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from . import models

# Create your views here.
def signin(request):
    return render(request, 'signin.html', {})
def signinBack(request):
    try:
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        result = authenticate(username=user)
        if result is not None:
            login(request, result)
        link = '/register/home/'
        return HttpResponseRedirect(link)
    except:
        return HttpResponse('user is exist')
        #return render(request, 'notUser.html', {})

def log(request , username):
    return render(request, 'login.html', {'u':username})

def logBack(request):
    user = request.POST['username']
    password = request.POST['password']
    result = authenticate(username=user, password=password)
    if result is not None:
        #request.session['userid']=result.id
        login(request, result)
        link = '/register/home/'
        return HttpResponseRedirect(link)
    else:
        return HttpResponse('user is not exist')
        # return render(request, 'notUser.html', {})


def home(request ):

    return render(request, 'home.html', {})
def home2(request):
    return render(request, 'home.html',{})

def logoutBack(request):
    logout(request)
    return render(request, 'login.html', {})
def food(request):
    data = models.meal.objects.all()
    return render(request, 'food.html', {'d': data})

def ser(request):
    return render(request, 'sevices.html', {})
def order(request):

    return render(request, 'order.html', {})
def orderform(request):
    v1 = request.POST['address']
    v2 = request.POST['number']
    v3 = request.POST['size']
    v4 = request.POST['phone1']
    v5 = request.POST['phone2']
    new = models.delivary()
    new.address = v1
    new.number = v2
    new.size = v3
    new.phone1 = v4
    new.phone2 = v5

    new.save()
    return HttpResponseRedirect('/register/cart')
def cart(request):
    # data = models.delivary.objects.get(user_id=request.session['userid'])
    data = models.delivary.objects.all()
    return render(request, 'cart.html', {'d': data})
def cartupdate(request, id):
    data = models.delivary.objects.get(id=id)
    return render(request, 'orderupdate.html', {'key': id,'data': data})
def update(request , id):
    new = models.delivary(id=id,
                         address=request.POST['address'],
                         number=request.POST['number'],
                         size=request.POST['size'],
                         phone1=request.POST['phone1'],
                         phone2=request.POST['phone2'])

    new.save()
    return HttpResponseRedirect('/register/cart')
def delete(request, id):
    new=models.delivary(id=id)
    new.delete()
    return HttpResponseRedirect('/register/cart')

def drink(request):
    data = models.drink.objects.all()
    return render(request, 'drink.html', {'d': data})
def menu(request):
    return render(request, 'foodORdrink.html', {})
#####################################################
def order2(request):
    return render(request, 'order2.html', {})
def orderform2(request):
    v1 = request.POST['address']
    v2 = request.POST['number']
    v4 = request.POST['phone1']
    v5 = request.POST['phone2']
    new = models.delivary2()
    new.address = v1
    new.number = v2
    new.phone1 = v4
    new.phone2 = v5

    new.save()
    return HttpResponseRedirect('/register/cart2')
def cart2(request):
    data = models.delivary2.objects.all()
    return render(request, 'cart2.html', {'d': data})
def cartupdate2(request, id):
    data = models.delivary2.objects.get(id=id)
    return render(request, 'orderupdate2.html', {'key': id,'data': data})
def update2(request , id):
    new = models.delivary2(id=id,
                         address=request.POST['address'],
                         number=request.POST['number'],
                         phone1=request.POST['phone1'],
                         phone2=request.POST['phone2'])

    new.save()
    return HttpResponseRedirect('/register/cart2')
def delete2(request, id):
    new=models.delivary2(id=id)
    new.delete()
    return HttpResponseRedirect('/register/cart2')

#################################################

def table(request):
    return render(request, 'table.html', {})
def tableform(request):
    v1 = request.POST['number']
    v2 = request.POST['date']
    v4 = request.POST['time']
    v5 = request.POST['phone1']
    new = models.table()
    new.number = v1
    new.date = v2
    new.time = v4
    new.phone1 = v5

    new.save()
    return HttpResponseRedirect('/register/tablecart')
def tablecart(request):
    data = models.table.objects.all()
    return render(request, 'tablecart.html', {'d': data})
def tableupdate(request, id):
    data = models.table.objects.get(id=id)
    return render(request, 'tableupdate.html', {'key': id,'data': data})
def update3(request , id):
    new = models.table(id=id,
                         number=request.POST['number'],
                         date=request.POST['date'],
                         time=request.POST['time'],
                         phone1=request.POST['phone1'])

    new.save()
    return HttpResponseRedirect('/register/tablecart')
def tabledelete(request, id):
    new=models.table(id=id)
    new.delete()
    return HttpResponseRedirect('/register/tablecart')
###################
def birthday(request):
    return render(request, 'birthday.html', {})
def birthdayform(request):
    v1 = request.POST['date']
    v2 = request.POST['number']
    v4 = request.POST['phone1']
    v5 = request.POST['phone2']
    new = models.birthday()
    new.date = v1
    new.number = v2
    new.phone1 = v4
    new.phone2 = v5

    new.save()
    return HttpResponseRedirect('/register/birthdaycart')
def birthdaycart(request):
    data = models.birthday.objects.all()
    #num = models.birthday.objects.get(id=10)
    # print('the value'+str((num[id].number)*20))
    #numb = str((num.number)*20)
    return render(request, 'birthdaycart.html', {'d': data })
def birthdayupdate(request, id):
    data = models.birthday.objects.get(id=id)
    return render(request, 'birthdayupdate.html', {'key': id,'data': data})
def update4(request , id):
    new = models.birthday(id=id,
                         date=request.POST['date'],
                         number=request.POST['number'],
                         phone1=request.POST['phone1'],
                         phone2=request.POST['phone2'])

    new.save()
    return HttpResponseRedirect('/register/birthdaycart')
def birthdaydelete(request, id):
    new=models.birthday(id=id)
    new.delete()
    return HttpResponseRedirect('/register/birthdaycart')









