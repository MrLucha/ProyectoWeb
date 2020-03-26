from django.shortcuts import render,redirect
from django.views.generic import View 

#IMPORTAR METODO DE AUTENTICACION
from django.contrib.auth import authenticate
 #LLEGA A LA VISTA Y LA EJECUTA

class DashboardClass(View):
    templates='dashboard.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.templates,{})
