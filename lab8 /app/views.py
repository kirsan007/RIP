from django.shortcuts import render
a=["Привет","Клубничное","Ванильное","Лимонное"]
b=["-","Вкусное мороженное","Такое себе мороженное","Не вкусное мороженное"]
c=["-","Фисташковые", "Орешковый", "Простой"]
def index(request):
    return render(request, 'index.html',{})
# Create your views here.
def detail(request, ID):
    return render(request, 'detail.html',{'X':a[ID],'B':b[ID], 'C':c[ID]

    })

