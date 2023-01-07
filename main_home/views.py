from django.shortcuts import render, redirect
from django.contrib import messages
from main_home.models import post



def home (request): # Pagina principal

    if request.method == 'GET':

        banco = post.objects.all()

      

    
        return render (request,'html/home_page.html',{'banco':banco})



      
def calcular_imc(request): # Calcular IMC

    if request.method == 'POST':

        altura_input = eval(request.POST['altura'])
        peso_input = eval(request.POST['peso'])

        altura = altura_input * altura_input
        
        resultado_0 = peso_input / altura

        resultado = round( resultado_0,2)


        if resultado <= 18.5:
            messages.info(request,"Abaixo do peso")
            return render (request,'html/select/cal_peso.html', {'resultado': resultado})

        elif resultado >= 40:
            messages.info(request,"Obesidade grau 3")
            return render (request,'html/select/cal_peso.html', {'resultado': resultado})

        elif resultado >= 18.5 and resultado <= 24.9:
            messages.info(request,"Peso normal")
            return render (request,'html/select/cal_peso.html', {'resultado': resultado})

        elif resultado >= 25 and resultado <= 29.9:
            messages.info(request,"Sobrepeso")
            return render (request,'html/select/cal_peso.html', {'resultado': resultado})

        elif resultado >= 30 and resultado <= 34.9:
            messages.info(request,"Obesidade grau 1")
            return render (request,'html/select/cal_peso.html', {'resultado': resultado})

        elif resultado >= 35 and resultado <= 39.9:
            messages.info(request,"Obesidade grau 2")
            return render (request,'html/select/cal_peso.html', {'resultado': resultado})


    if request.method == 'GET':

        return render (request,'html/select/cal_peso.html')

        

# Create your views here.
