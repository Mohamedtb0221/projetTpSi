from django import forms
from .models import *

class officierForm (forms.ModelForm):

    class Meta:
        model = Officier
        fields = [ 'matricule','bureau', 'nom', 'prenom','datePriseService' ]
        widgets = {
            'matricule' : forms.NumberInput ( attrs = { 'class' : 'form-control' }),
            'bureau':forms.Select(attrs = {'class':'form-control'}),
            'nom':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'prenom':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'datePriseService': forms.DateInput( attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            }


class naissanceForm(forms.ModelForm):
    class Meta:
        model=Naissance
        fields = "__all__"
        widgets={
            'officier':forms.Select(attrs = {'class':'form-control'}),
            'numero_registre':forms.Select(attrs = {'class':'form-control'}),
            'annee' : forms.NumberInput ( attrs = { 'class' : 'form-control' }),
            'nom' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'prenoms' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'sexe' : forms.Select ( attrs = { 'class' : 'form-control' },choices = (('M','Masculin'),('F','Feminin'))),
            'hopital':forms.Select ( attrs = { 'class' : 'form-control' },),
            'date_naiss':forms.DateInput( attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'heure_naiss':forms.TimeInput(attrs = {'class':'form-control','placeholder':'heure de naissance','type':'time'}),
            'pays':forms.TextInput(attrs = {'class':'form-control'}),
            'perei':forms.Select ( attrs = { 'class' : 'form-control' } ) ,            
            'profession_pere':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'merei':forms.Select ( attrs = { 'class' : 'form-control' } ) ,            
            'profession_mere':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            

        }

class mariageForm(forms.ModelForm):
    class Meta:
        model=Mariage
        fields = ['officier','req1','req2','temoin1','temoin2','numero_registre','profession_req1','domicile_req1','profession_req2','domicile_req2','filiation','date_mariage','lieu_mariage']
        widgets={
            'officier':forms.Select(attrs = {'class':'form-control'}),
            'numero_registre':forms.Select(attrs = {'class':'form-control'}),
            'numero':forms.NumberInput(attrs = {'class':'form-control'}),
            'req1':forms.Select(attrs = {'class':'form-control'}),
            'profession_req1':forms.TextInput(attrs = {'class':'form-control'}),
            'domicile_req1':forms.TextInput(attrs = {'class':'form-control'}),
            'req2':forms.Select(attrs = {'class':'form-control'}),
            'profession_req2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'domicile_req2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'temoin1':forms.Select(attrs = {'class':'form-control'}),
            'temoin2':forms.Select(attrs = {'class':'form-control'}),
            'filiation':forms.TextInput(attrs = {'class':'form-control'}),
            'date_mariage':forms.DateInput( attrs={'class':'form-control', 'placeholder':'date de mariage', 'type':'date'}),
            'lieu_mariage' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,

        }

class decesForm(forms.ModelForm):
    class Meta:
        model=Deces
        fields = "__all__"
        widgets={
            'officier':forms.Select(attrs = {'class':'form-control'}),
            'numero_registre':forms.Select(attrs = {'class':'form-control'}),
            'nom' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'prenoms' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'sexe' : forms.Select ( attrs = { 'class' : 'form-control' },choices = (('M','Masculin'),('F','Feminin'))),
            'date_naiss':forms.DateInput( attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'lieu_naiss':forms.TextInput(attrs = {'class':'form-control'}),
            'mariée':forms.Select ( attrs = { 'class' : 'form-control' },choices = (('oui','OUI'),('non','NON'))),
            'jour_deces':forms.DateInput(attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'heure_deces':forms.TimeInput(attrs = {'class':'form-control','placeholder':'heure de naissance','type':'time'}),
            'lieu_deces':forms.TextInput(attrs = {'class':'form-control'}),
            'numN':forms.Select(attrs = {'class':'form-control'})
        }

class loginForm(forms.ModelForm):


    class Meta :
        model = User
        fields = ('username','password')
        widgets={
            'username':forms.TextInput(attrs = {'class':'form-control form-control-lg','placeholder': "Nom d'utilisateur"}),
            'password':forms.PasswordInput(attrs = {'class':'form-control form-control-lg','placeholder': "Mot de passe"}),
        }


