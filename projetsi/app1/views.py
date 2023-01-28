from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from app1.filters import *


from .models import *
from .forms import *

# Create your views here.

def ajout_officier(request):
    if request.method == 'POST':
        form = officierForm(request.POST)
        if form.is_valid():
            form.save()
            form = officierForm()
            mssg = "officier ajouté, vous pouvez ajouté une autre"

            return render(request, "ajoutOfficier.html", {"form": form, "message": mssg})
    else:
        form = officierForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutOfficier.html", {"form": form, "message ": mssg})

def ajout_naissance(request):
    if request.method == 'POST':
        form = naissanceForm(request.POST)
        if form.is_valid():
            form.save()
            form = naissanceForm()
            mssg = "act ajouté, vous pouvez ajouté une autre"
            return render(request, "ajoutNaissance.html", {"form": form, "message": mssg})
    else:
        form = naissanceForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutNaissance.html", {"form": form, "message ": mssg})

def ajout_mariage(request):
    if request.method == 'POST':
        form = mariageForm(request.POST)
        if form.is_valid():
            form.save()
            form = mariageForm()
            mssg = "acte ajouté, vous pouvez ajouté une autre"

            return render(request, "ajoutMariage.html", {"form": form, "message": mssg})
    else:
        form = mariageForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutMariage.html", {"form": form, "message ": mssg})

def ajout_deces(request):
    if request.method == 'POST':
        form = decesForm(request.POST)
        if form.is_valid():
            form.save()
            form = decesForm()
            mssg = "acte ajouté, vous pouvez ajouté une autre"

            return render(request, "ajoutDeces.html", {"form": form, "message": mssg})
    else:
        form = decesForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutDeces.html", {"form": form, "message ": mssg})

def login(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        form=loginForm(request.POST)
        if form.is_valid():
            check=User.objects.filter(username=username) and User.objects.filter(password=password).exists()
            if check:
                if username=="maire" and password=="maire":
                    return redirect('/mairePage')                
                return redirect('/rechercherN')
            else:
                messages.success(request,'mot de passe ou nom utilisateur incorrect ! ')
                return redirect('/loginPage')
    else:
        form=loginForm()
    return  render(request,'login.html',{'form':form})


def searchN(request):
    acte_list = Naissance.objects.all()
    acte_filter = acteFilter(request.GET, queryset=acte_list)
    return render(request, 'searchN.html', {'filter': acte_filter})


def edit(request, id):
    acte = Naissance.objects.get(id=id)
    marie=Mariage.objects.filter(id=id)
    if marie:
        return render(request,'voir.html', {'acte':acte,'marie':'oui' })
    return render ( request , 'voir.html' , { 'acte' : acte , 'marie' : 'non' } )

def editM(request, id):
    acte = Mariage.objects.get(id=id)
    return render(request,'voirM.html', {'acte':acte })

def editD(request, id):
    acte = Deces.objects.get(id=id)
    return render(request,'voirD.html', {'acte':acte })

def searchM(request):
    acte_list = Mariage.objects.all()
    acte_filter = MariageFilter(request.GET, queryset=acte_list)
    return render(request, 'searchM.html', {'filter': acte_filter})

def searchD(request):
    acte_list = Deces.objects.all()
    acte_filter = DecesFilter(request.GET, queryset=acte_list)
    return render(request, 'searchD.html', {'filter': acte_filter})


def Modifier_acteN(request, id):
    acteN = Naissance.objects.get(id=id)
    if request.method == 'POST':
        form = naissanceForm(request.POST, instance=acteN)
        if form.is_valid():            
            form.save()            
            return redirect('searchN')
    else:
        form = naissanceForm(instance=acteN)
    return render(request,'modifierN.html', {'form':form})

def Modifier_acteM(request, id):
    acteM = Mariage.objects.get(id=id)
    if request.method == 'POST':
        form = mariageForm(request.POST, instance=acteM)
        if form.is_valid():            
            form.save()            
            return redirect('searchM')
    else:
        form = mariageForm(instance=acteM)
    return render(request,'modifierM.html', {'form':form})

def Modifier_acteD(request, id):
    acteD = Deces.objects.get(id=id)
    if request.method == 'POST':
        form = decesForm(request.POST, instance=acteD)
        if form.is_valid():            
            form.save()            
            return redirect('searchD')
    else:
        form = decesForm(instance=acteD)
    return render(request,'modifierD.html', {'form':form})
    
def afficherOff(request):
    total=Officier.objects.all()
    return render(request,'mairePage.html', {'total':total })

def suppOffic(request,id):
    off = Officier.objects.get(id=id)    
    off.delete()
    return redirect('mairePage')
    
