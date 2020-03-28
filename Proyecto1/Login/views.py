from django.shortcuts import render,redirect
from django.views.generic import View 
from django.contrib.auth import login as login_django

#IMPORTAR METODO DE AUTENTICACION
from django.contrib.auth import authenticate
 #LLEGA A LA VISTA Y LA EJECUTA

class LoginClass(View):
    templates='index.html'
    #templateOk='dashboard.html'

    def get(self,request, *args,**kwargs,):
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:dashboard')
        return render(request, self.templates,{})
        # print("aqui esta login")
        # return render(request,self.templates,{})
    
    def post(self,request,*args,**kwargs,):
        userPost=request.POST['user']
        passwordPost=request.POST['password']
        user_session = authenticate(username = userPost, password = passwordPost)
        #ACÁ LO VALIDO 
        if user_session is not None:
            login_django(
                request, user_session
            )
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:dashboard')
        else: 
            self.message = 'Usuario o contraseña incorrecto'
        
        return render(request, self.templates, self.get_context())
        # user_session=authenticate(username=userPost, password=passwordPost)

        # if user_session is not None:
        #     print('si existe')
        #     #return render(request,DashboardClass.templateOk,{}) 
        #     return redirect('Dashboard:dashboard') 
        # else:
        #     print('no existe')
        #     self.message='Usuario o contraseña incorrectos'
                       
        
        # #pass
        # return render(request,self.templates, self.getContext())

    def getContext(self):
        return{
            'error':self.message,
        }
# def Index (request):
#     return render(request,'index.html',{})

# def Landing (request):
#     return render(request,'landing.html',{})