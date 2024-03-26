from django.shortcuts import render,redirect
from todoapp.models import Phone
# Create your views here.
def Home(req):
    Phonebook=Phone.objects.all()
    print(Phonebook)
    if req.method == 'POST':
        name = req.POST.get('name', '')
        phone = req.POST.get('phone', '')
      
        contact=Phone(name=name,phone=phone)
        contact.save()
    return render(req,'index.html',{'PhoneBook':Phonebook})

def Delete(req,id):
   print(id)
   contact=Phone.objects.get(id=id)
   contact.delete()

   return  redirect('todo:home')

def Update(req,id):
    print(id)
    contact=Phone.objects.get(id=id)
    if req.method=="POST":
        name = req.POST.get('name', '')
        phone = req.POST.get('phone', '')
        contact.name = name
        contact.phone = phone
        contact.save()
        return redirect('todo:home')
    return render(req,'update.html',{'contact':contact})