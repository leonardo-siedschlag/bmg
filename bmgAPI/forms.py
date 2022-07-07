from django import forms
from .models import ClienteModel, UFS
from validate_docbr import CPF
import requests

url  =  'https://ws1.bmgconsig.com.br/webservices/ConsultaMargemIN100?wsdl'

Headers = {'content-type': "text/xml; charset=utf-8",
           'soapaction': 'http://myendpoint/url'}


class ClienteForm(forms.ModelForm):
    
    uf = forms.ChoiceField(choices=UFS)
    telefone  = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self._telefone = kwargs.pop('telefone',None)
        super().__init__(*args, **kwargs) 
    
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if self._telefone == "Celular j&#xE1; usado em outro CPF!":
            raise forms.ValidationError('celular usado em outro CPF')
        
        return telefone  

    class Meta:
        model = ClienteModel
        fields = '__all__' 


def validacaoToken(token, numeroSolicitacao):
    
    return """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.econsig.bmg.com">
    <soapenv:Header/>
    <soapenv:Body>
        <web:validarToken>
            <DadosConsultaIN100>
                <login>soma.saudade</login>
                <senha>1f485d8%</senha>
                <numeroSolicitacao>"""+numeroSolicitacao+"""</numeroSolicitacao>
                <token>"""+token+"""</token>
            </DadosConsultaIN100>
        </web:validarToken>
    </soapenv:Body>
    </soapenv:Envelope>
    """

class ValidacaoToken(forms.Form):
     
    Digite_Token = forms.CharField() 
    
    def __init__(self, *args, **kwargs):
        self._pwd = kwargs.pop('pwd',None)
        super().__init__(*args, **kwargs)            
              
        
    def clean_Digite_Token(self):    
        token = self.cleaned_data.get('Digite_Token')
        
        numeroSolicitado = self._pwd
        print(numeroSolicitado)
        response = requests.post(url, headers=Headers, 
            data=validacaoToken(token, numeroSolicitado))
        print(response.text)
               
        if "Fault" in response.text:
            raise forms.ValidationError('TOKEN INVÁLIDO')
        
        
        return token        
    

    

    
