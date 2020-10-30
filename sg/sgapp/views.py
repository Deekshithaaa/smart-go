
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Fri
from .models import Per
'''from sgapp.models import Dt'''
'''from .forms import Form'''



def home(request):
    return render(request,'sgapp/home.html',{})
def vacation(request):
    return render(request,'sgapp/vacation.html', {})
def fri(request):
    return render(request, 'sgapp/fri.html', {})
def fam(request):
    return render(request, 'sgapp/fam.html', {})
def per(request):
    return render(request, 'sgapp/per.html', {})
def sin(request):
    from sklearn import tree

    clf = tree.DecisionTreeClassifier()


    f0 = request.POST.get("pername")
    f1 = request.POST.get("per1")
    f2 = request.POST.get("per2")
    f3 = request.POST.get("per3")
    f4 = request.POST.get("per4")
    f5 = request.POST.get("per5")
    f6 = request.POST.get("per6")
    f7 = request.POST.get("per7")
    f8 = request.POST.get("per8")
    f9 = request.POST.get("per9")
    f = Per(user_namep=f0, Q1p=f1, Q2p=f2, Q3p=f3, Q4p=f4, Q5p=f5, Q6p=f6, Q7p=f7, Q8p=f8, Q9p=f9)
    f.save()
    X = [[21, 31], [21, 32], [21, 33], [21, 34], [22, 31], [22, 32], [22, 33], [22, 34], [23, 31], [23, 32], [23, 33],
         [23, 34],
         [24, 31], [24, 32], [24, 33], [24, 34]]

    Y = ['La place sarovar portico,Lucknow', 'The Panache', 'Red fox hotel,Hyderabad', 'peacock siute,Bengaluru',
         'colonia santa maria',
         'Sagara beach resort', 'sea shell,Neil', 'sea shell', 'Havelock', 'ITc grand ,Goa', 'The Oberoi cecil,Shimla',
         'Sindabezi island', 'Nihi Sumba Island,Indonesia',
         'Chandar Frozen River Trek', 'The Dream Ride Motor Bike Expedition to Ladak', 'Hot air Balooning at Jaipur']

    clf = clf.fit(X, Y)

    prediction = clf.predict([[f2,f3]])

    return render(request, 'sgapp/sin.html', {'f2': prediction})
def fam2(request):
    if request.method=='POST':
        return render(request, 'sgapp/fam2.html', {})
def part1(request):
    return render(request, 'sgapp/part1.html', {})
def hhh(request):
    return render(request, 'sgapp/hhh.html', {})
def vacdet(request):
    from sklearn import tree

    clf = tree.DecisionTreeClassifier()



    p0 = str(request.POST.get("naf"))
    p1 = request.POST.get("fri1")
    p2 = str(request.POST.get("fri2"))
    p3 = request.POST.get("fri4")
    p4 =request.POST.get("fri5")
    p5 = str(request.POST.get("fri6"))
    p6 =str(request.POST.get("fri7"))
    p7 =str( request.POST.get("fri8"))
    p8 =str( request.POST.get("fri9"))
    p9 = str(request.POST.get("fri_10"))
    p10 = str(request.POST.get("fri_11"))
    p=Fri(user_name=p0,Q1=p1,Q2=p2,Q3=p3,Q4=p4,Q5=p5,Q6=p6,Q7=p7,Q8=p8,Q9=p9,Q10=p10)
    p.save()
    X = [[11, 41,51],
        [11, 41, 52], [11, 41,53], [11,42,51], [11,42,52],
        [11, 42, 53], [11, 43, 51],
        [11, 43, 52], [11, 43, 53], [12, 41, 51],
        [12, 41, 52], [12, 41, 53],
        [12, 42, 51], [12, 42, 52], [12, 42, 53],
        [12, 43, 51],
        [12, 43, 52], [12, 43, 53],
         [11, 44,51],
        [11, 44, 52], [11, 44,53]]

    Y = ['Island Water Sports', 'Island Water Sports', 'Island Water Sports', 'Yumthang Valley - Sikkim',
        'Yumthang Valley - Sikkim', 'Yumthang Valley', 'Tajmahal', 'Tajmahal',
        'Tajmahal', 'Myrtos Beach (Greece)', 'Myrtos Beach (Greece)', 'Myrtos Beach (Greece)', 'Sondrio-Italy',
        'Sondrio-Italy', 'Sondrio-Italy', 'secret world of spies in london',
        'secret world of spies in london', 'secret world of spies in london','Rishikesh','Rishikesh','Rishikesh']

    clf = clf.fit(X, Y)

    prediction = clf.predict([[p1, p3, p4]])
    a=1
    return render(request,'sgapp/fam.html',{'ppp':prediction,'a':1})
