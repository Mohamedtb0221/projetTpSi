import datetime

from django.db import models

# Create your models here.
Sexe=(
    ('HOMME','homme'),
    ('FEMME','femme')
)


class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Maire (models.Model):
    matricule=models.BigIntegerField(auto_created=True,unique = True)
    nom= models.CharField ( max_length = 100 , verbose_name = "Nom du maire" ,default = ' ')
    prenom= models.CharField ( max_length = 100 , verbose_name = "Prenom du maire" ,default = ' ')
    def __str__ ( self ) :
        return str ( self.matricule )

class Bureauetatcivile (models.Model):
    le_maire = models.ForeignKey ( Maire , on_delete = models.CASCADE,null = True )
    wilaya= models.CharField ( max_length = 100 , verbose_name = "Nom du wilaya" ,default = ' ')
    daira = models.CharField ( max_length = 100 , verbose_name = "Nom du daira" ,default = ' ')
    commune =models.CharField ( max_length = 100 , verbose_name = "Nom du comunne" ,default = ' ')

    def __str__ ( self ) :
        return str ( self.commune )




def matricul():
    no = Officier.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Officier(models.Model):
    bureau = models.ForeignKey ( Bureauetatcivile , on_delete = models.CASCADE,null = True )
    matricule = models.BigIntegerField(unique = True,default=matricul)
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    datePriseService = models.DateField()
    def __str__ ( self ) :
        return str ( self.id )

class Centre(models.Model):
    libelle_centre = models.CharField(max_length=500, verbose_name="Centre de Santé")
    situation = models.CharField(max_length=500, verbose_name="Situation Geographique du Centre")

    def __str__ ( self ) :
        return str ( self.libelle_centre )

class RegistreNaissance(models.Model):
    bureau = models.ForeignKey ( Bureauetatcivile , on_delete = models.CASCADE,null = True )
    numero_registre = models.CharField ( max_length = 150 , verbose_name = 'Numero du Registre',primary_key=True )
    annee = models.IntegerField ( verbose_name = 'Annee' , default = datetime.datetime.now ( ).year )

    def __str__ ( self ) :
        return str ( self.numero_registre )

class RegistreMariage(models.Model):
    bureau = models.ForeignKey ( Bureauetatcivile , on_delete = models.CASCADE,null = True )
    numero_registre = models.CharField ( max_length = 150 , verbose_name = 'Numero du Registre',primary_key=True )
    annee = models.IntegerField ( verbose_name = 'Annee' , default = datetime.datetime.now ( ).year )

    def __str__ ( self ) :
        return str ( self.numero_registre )

class RegistreDeces(models.Model):
    bureau = models.ForeignKey ( Bureauetatcivile , on_delete = models.CASCADE,null = True )
    numero_registre = models.CharField ( max_length = 150 , verbose_name = 'Numero du Registre',primary_key=True )
    annee = models.IntegerField ( verbose_name = 'Annee' , default = datetime.datetime.now ( ).year )

    def __str__ ( self ) :
        return str ( self.numero_registre )


class Naissance(models.Model):
    officier=models.ForeignKey(Officier,on_delete=models.CASCADE,default=0)
    numero_registre = models.ForeignKey(RegistreNaissance,on_delete=models.CASCADE ,default = 0)
    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='Precise le sexe', choices=Sexe,default = 'Masculin')
    nom = models.CharField(max_length=250, verbose_name='Nom')
    prenoms = models.CharField(max_length=250, verbose_name='Prenoms')
    date_naiss = models.DateField(verbose_name='Date de Naissance',null = True)
    heure_naiss = models.TimeField(verbose_name='Heure de Naissance')
    hopital = models.ForeignKey(Centre,on_delete=models.CASCADE)
    pays=models.CharField(max_length = 50,verbose_name = 'pays de naissance',default = 'Algérie')
    # parents    
    profession_pere = models.CharField(max_length=250, verbose_name='Profession du Pere', blank=True)    
    profession_mere = models.CharField(max_length=250, verbose_name='Profession de la Mere')    
    # grand-parents    
    perei=models.ForeignKey("self",on_delete=models.CASCADE,default=1,blank=True,related_name="pereinfo")
    merei=models.ForeignKey("self",on_delete=models.CASCADE,default=1,blank=True,related_name="mereinfo")

    def __str__ ( self ) :
        return str ( self.id )
    


def num_mariage():
    no = Mariage.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Mariage(models.Model):
    officier=models.ForeignKey(Officier,on_delete=models.CASCADE,default=0)
    numero_registre = models.ForeignKey ( RegistreMariage , on_delete = models.CASCADE,default = 0 )
    numero = models.CharField(max_length=5, unique=True, default=num_mariage)
    profession_req1 = models.CharField ( max_length = 500 , verbose_name = "Profession du Marie" )
    domicile_req1 = models.CharField ( max_length = 500 , verbose_name = "Lieu de Domicile du Marie" )
    profession_req2 = models.CharField ( max_length = 500 , verbose_name = "Profession du Mariee" )
    domicile_req2 = models.CharField ( max_length = 500 , verbose_name = "Lieu de Domicile du Mariee" )
    filiation = models.CharField ( max_length = 500 , verbose_name = 'la filiation',default = ' ' )
    date_mariage = models.DateField ( verbose_name = "Date du Mariage" )
    lieu_mariage = models.CharField ( max_length = 500 , verbose_name = "Lieu du Mariage" )
    req1=models.ForeignKey(Naissance,on_delete=models.CASCADE,default=1,blank=True,related_name="req1info")
    temoin1=models.ForeignKey(Naissance,on_delete=models.CASCADE,default=1,blank=True,related_name="temoin1info")
    req2=models.ForeignKey(Naissance,on_delete=models.CASCADE,default=1,blank=True,related_name="req2info")
    temoin2=models.ForeignKey(Naissance,on_delete=models.CASCADE,default=1,blank=True,related_name="temoin2info")

    def __str__ ( self ) :
        return str ( self.id )

class Deces(models.Model):
    officier=models.ForeignKey(Officier,on_delete=models.CASCADE,default=0)
    numero_registre = models.ForeignKey ( RegistreDeces , on_delete = models.CASCADE,default = 0 )
    mariée=models.CharField(max_length = 10,choices = (('oui','OUI'),('non','NON')),default = 'NON')
    jour_deces=models.DateField ( verbose_name = 'Date de deces' )
    heure_deces=models.TimeField ( verbose_name = 'Heure de deces' )
    lieu_deces=models.CharField ( max_length = 250 , verbose_name = 'Lieu de deces' )
    numN=models.ForeignKey(Naissance,on_delete=models.CASCADE,default=0)

    def __str__ ( self ) :
        return str ( self.id )
    
