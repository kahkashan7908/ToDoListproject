from django.shortcuts import render,redirect
from.models import todoData
def mainPage(request):
    data=todoData.objects.all()
    return render(request,'mainpage.html',{'data':data})
def formPage(request):
    if request.method=='GET':
        return render(request,'form.html')
    else:
        todoData(
            title=request.POST['title'],
            date=request.POST['date'],
            Description=request.POST['desc']
        ).save()
        return redirect('mainPage')
def updatePage(request,id):
    data=todoData.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update.html',{'val':data})
    else:
        data.title=request.POST['title']
        data.date=request.POST['date']
        data.Description=request.POST['desc']
        data.save()
        return redirect('mainPage')
def deletePage(request,id):
    data=todoData.objects.get(id=id)
    data.delete()
    return redirect('mainPage')

