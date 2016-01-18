# Register your models here.
from django.contrib import admin
#Activer l une ou l autre des 2 instruction ci dessous JPN 13/10/2015
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import Organisme, Utilisateur, Action, Typeintervention, Status,Cible,ActionCible,ActionTypeintervention,ActionLocalisation

## PERMISSIONS (ajout nvx element de la liste) ##

class CibleAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

class TypeinterventionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

## SECTIONS  ##

class ActionCibleAdmin(admin.TabularInline):
    model = ActionCible

class ActionTypeinterventionAdmin(admin.TabularInline):
    model = ActionTypeintervention  

class ActionLocalisationAdmin(admin.TabularInline):
    model = ActionLocalisation  
    
## L'Admin Principal compose des SECTIONS ##

class ActionAdmin(admin.ModelAdmin):
    model = Action
    radio_fields = {"echelle_localisation": admin.VERTICAL}
    inlines = [ActionCibleAdmin,ActionTypeinterventionAdmin,ActionLocalisationAdmin,] # On a agrege les sections



#admin.site.register(mdgRegion, admin.OSMGeoAdmin)
#admin.site.register(mdgRegion, LeafletGeoAdmin)
admin.site.register(Organisme)
admin.site.register(Utilisateur)
#admin.site.register(ActionLocalisation)
#Activer l une ou l autre des 2 instructions ci dessous JPN 13/10/2015
#admin.site.register(Action)
admin.site.register(Action,ActionAdmin)
admin.site.register(ActionLocalisation, LeafletGeoAdmin)
admin.site.register(Typeintervention,TypeinterventionAdmin)

admin.site.register(Status)
admin.site.register(Cible,CibleAdmin)

