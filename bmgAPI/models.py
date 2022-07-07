from django.db import models

from random import choice
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator
import datetime
from django.utils.timezone import now



UFS= [('AC', ' AC'),
('AL' , 'AL'), 
('AP' ,  'AP'),
('AM', 'AM'),  
('BA', 'BA') ,
('CE' ,  'CE'), 
('DF',  'DF'),
('ES' , 'ES'),
('GO', 'GO'),  
('MA', 'MA'), 
('MT', 'MT'),
( 'MS' , 'MS'), 
('MG',  'MG'), 
('PA', 'PA'), 
( 'PB', 'PB'),
('PR',  'PR'), 
('PE', ' PE'),
('PI' , 'PI'), 
('RJ', 'RJ'), 
('RN', 'RN'),
('RS', 'RS'),
('RO', 'RO'), 
('RR', 'RR' ),
('SC' ,  'SC'), 
('SP',  'SP'),
('SE',  'SE'),
('TO', 'TO')]

class ClienteModel(models.Model):
    id   = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    cpf  = models.CharField(max_length=11)
    ddd = models.IntegerField()
    telefone  = models.IntegerField()
    matricula = models.IntegerField()
    data_Nascimento = models.DateField()
    cidade = models.CharField(max_length=128)
    uf  = models.CharField(max_length = 128, choices=UFS)
    
    def __str__(self):
        return self.nome

    