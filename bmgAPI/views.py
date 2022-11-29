from django.http import HttpResponse
from django.urls import reverse

import requests
from django.http import HttpResponse
from bmgAPI.forms import   ClienteForm, ValidacaoToken
from django.shortcuts import  redirect, render
import datetime

url  =  'https://ws1.bmgconsig.com.br/webservices/ConsultaMargemIN100?wsdl'

Headers = {'content-type': "text/xml; charset=utf-8",
           'soapaction': 'http://myendpoint/url'}

dd ='47'
def mandarSms():
    return """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.econsig.bmg.com">
        <soapenv:Header/>
        <soapenv:Body>
            <web:inserirSolicitacao>
                <solicitacaoIN100>
                <login>soma.saudade</login>
                <senha>1f485d8%</senha>
                <cidade>JARAGUA DO SUL</cidade>
                <cpf>47637226972</cpf>
                <dataNascimento>1960-07-02T09:56:57</dataNascimento>
                <ddd>"""+dd+"""</ddd>
                <estado>SC</estado>
                <matricula>1856999995</matricula>
                <nome>Irene Hotz</nome>
                <telefone>997418343</telefone>
                </solicitacaoIN100>
            </web:inserirSolicitacao>
        </soapenv:Body>
    </soapenv:Envelope>
    """

def mandarSmsToken(nome , sobrenome, cpf, ddd, telefone, matricula, data_nascimento, uf, cidade):
    return """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.econsig.bmg.com">
        <soapenv:Header/>
        <soapenv:Body>
            <web:inserirSolicitacao>
                <solicitacaoIN100>
                <login>soma.saudade</login>
                <senha>1f485d8%</senha>
                <cidade>JOINVILLE</cidade>
                <cpf>01717736831</cpf>
                <dataNascimento>1953-01-15T09:56:57</dataNascimento>
                <ddd>"""+dd+"""</ddd>
                <estado>SC</estado>
                <matricula>1487725385</matricula>
                <nome>MARIA GORETE PIMENTA</nome>
                <telefone>988234282</telefone>
                </solicitacaoIN100>
            </web:inserirSolicitacao>
        </soapenv:Body>
    </soapenv:Envelope>
    """

def pesquisaToken(cpf):
   today = str(datetime.date.today())
   tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
     
   return """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.econsig.bmg.com">
    <soapenv:Header/>
    <soapenv:Body>
        <web:pesquisar>
            <FiltroConsultaIN100>
                <login>soma.saudade</login>
                <senha>1f485d8%</senha>
                <cpf>97972991120</cpf>
                <numeroSolicitacao></numeroSolicitacao>
                <periodoFinal>"""+tomorrow+"""T09:56:57</periodoFinal>
                <periodoInicial>"""+today+"""T09:56:57</periodoInicial>
            </FiltroConsultaIN100>
        </web:pesquisar>
    </soapenv:Body>
    </soapenv:Envelope>
    """

def searchText(texto, search):

    i = texto.find(search)
    text= ""
    e = 0
   
    while i < len(texto):
    
        if texto[i] ==">" or e==1:
            e = 1    
            if texto[i+1] == "<":
                break
            text = text + texto[i+1]
        
        i = i + 1     
    
    
    return text

globalCpf = "97972991120"
def validatorTokenView(request, numeroSolicitado):
    
    if request.method == 'POST':
       form = ValidacaoToken(request.POST, pwd = numeroSolicitado)
       if form.is_valid():
            responses = requests.post(url, headers=Headers, data=pesquisaToken(globalCpf))
            valorLimiteCartao  = searchText(responses.text, "valorLimiteCartao")
            margemDisponivel  = searchText(responses.text, "margemDisponivel")
            
            
            print(responses.text)
            print("valor ",valorLimiteCartao, "margem", margemDisponivel)
    else:
        form =  ValidacaoToken()    
    return render(request,'main/bmgValidacaoToken.html', {'validacaoToken':form})   




def index(request):
    
    if request.method == "POST":  
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            cpf = form.cleaned_data['cpf']
            ddd = str(form.cleaned_data['ddd'])
            telefone  = str(form.cleaned_data['telefone'])
            matricula  = str(form.cleaned_data['matricula'])
            data_nascimento = str(form.cleaned_data['data_Nascimento'])
            uf  = form.cleaned_data['uf']
            cidade  = form.cleaned_data['cidade']
            textoValidation  = "Gentileza coleta-lo com cliente"
            celularUsado = "Celular j&#xE1; usado em outro CPF!"
            
            try:
                response = requests.post(url, headers=Headers, timeout=5,
                data=mandarSmsToken(nome , sobrenome, cpf, ddd, telefone, matricula, data_nascimento, uf, cidade))
                if celularUsado in response.text:
                    form = ClienteForm(request.POST, telefone = celularUsado)
                
                elif  textoValidation in response.text:
                    try:
                        responses = requests.post(url, headers=Headers, data=pesquisaToken(cpf))
                        if responses.status_code == 200:
                            numeroSolicitacao =  searchText(responses.text, "numeroSolicitacao")
                            return redirect(reverse('validatorTokenView', args = [numeroSolicitacao]))
                    except: 
                        return render(request,'main/bmgTokenRequire.html', {'cliente':form})
                
                else:
                    return render(request,'main/bmgTokenRequire.html', {'cliente':form})

            except:
                return render(request,'main/bmgTokenRequire.html', {'cliente':form})
                            
    else:
        form  = ClienteForm()
    return render(request,'main/bmgTokenRequire.html', {'cliente':form})  



#FUNCAO DESATIVADA!
def teste(request):
    response = requests.post(url, headers=Headers, data=mandarSms())
    print(response.text)
    if response.status_code == 200:
        print('ente')
    else:
        print('none')
    return HttpResponse('Hello, world. Youre at the polls index.')

