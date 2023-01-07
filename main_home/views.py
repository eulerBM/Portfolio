from django.shortcuts import render, redirect
from django.contrib import messages
from main_home.models import post






def home (request): # Pagina principal

    banco = post.objects.all() 

    if request.method == 'GET': # se o metodo for GET retorna pagina inicial

        return render (request,'html/home_page.html',{'banco':banco})


    if request.method == 'POST': # procura informação pelo input ( SEARCH... )   

        get_search = request.POST['search']    

        if get_search == '': # Se enviar input vazio retorna todos os CARDS      

            return render (request,'html/home_page.html',{'banco':banco})

        else: # se vier preenchido vai no banco, filtra e mostre
            search = post.objects.filter(titulo=get_search)

            return render (request,'html/home_page.html', {'banco':search})

      
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

        

def calcular_agua(request): # Calcular quantos de agua que vc deve beber

    if request.method == 'POST':

        get_box = eval(request.POST['calcular'])

        resultado = str((get_box * 35) / 100)

        messages.info(request,f"Voce deve beber { resultado.replace('.',',') } Litros por dia")
        return render (request,'html/select/agua_calcu.html')

    if request.method == 'GET':

        return render (request,'html/select/agua_calcu.html')
