from django.urls import path, include
from . import views

urlpatterns = [
    path('ajout_officier/', views.ajout_officier,name="ADD_off"),
    path('ajout_naissance/', views.ajout_naissance,name="ADD_Naiss"),
    path('ajout_mariage/' , views.ajout_mariage, name = "ADD_Mar"),
    path('ajout_Deces/' , views.ajout_deces, name = "ADD_Dec"),
    path('rechercherN/',views.searchN,name="searchN"),
    path('rechercherM/',views.searchM,name="searchM"),
    path('rechercherD/',views.searchD,name="searchD"),
    path('edit/<int:id>', views.edit,name="edit"),
    path('editM/<int:id>', views.editM,name="editM"),
    path('editD/<int:id>', views.editD,name="editD"),
    path('modifierN/<int:id>', views.Modifier_acteN,name="modifierN"),
    path('modifierM/<int:id>', views.Modifier_acteM,name="modifierM"),
    path('modifierD/<int:id>', views.Modifier_acteD,name="modifierD"),
    path('mairePage/', views.afficherOff,name="mairePage"),
    path('SupprimerOff/<int:id>', views.suppOffic, name="SUPP_Off"),
    path( 'loginPage/' , views.login, name = "login"),
]