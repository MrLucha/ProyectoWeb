from django.shortcuts import render,redirect
from django.views.generic import View 

#IMPORTAR METODO DE AUTENTICACION
from django.contrib.auth import authenticate
 #LLEGA A LA VISTA Y LA EJECUTA

class LoginClass(View):
    templates='index.html'
    #templateOk='dashboard.html'

    def get(self,request, *args,**kwargs,):
        print("aqui esta login")
        return render(request,self.templates,{})
    
    def post(self,request,*args,**kwargs,):
        userPost=request.POST['user']
        passwordPost=request.POST['password']
        user_session=authenticate(username=userPost, password=passwordPost)

        if user_session is not None:
            print('si existe')
            #return render(request,DashboardClass.templateOk,{}) 
            return redirect('Login:dashboard') 
        else:
            print('no existe')
            self.message='Usuario o contraseña incorrectos'
                       
        
        #pass
        return render(request,self.templates, self.getContext())

    def getContext(self):
        return{
            'error':self.message,
        }
# def Index (request):
#     return render(request,'index.html',{})

# def Landing (request):
#     return render(request,'landing.html',{})