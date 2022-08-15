#HELENA KUCHINSKI FERREIRA
import random
import numpy as np
import logging 
import time

numeros = np.random.randint(1,1000000, (1,1000000))
random.shuffle(numeros) 

#CRIANDO CLASSES
class Valores:
  valores = None
  proxValor = None

  def __init__(self, valores):
    self.valores = valores

class Pilha:
  topoPilha = None

  def __init__(self):
    self.topoPilha = None

  def push(self, valores):
    auxiliar = Valores(valores)
    if self.topoPilha == None:
      self.topoPilha = auxiliar
    else:
      auxiliar.proxValor = self.topoPilha
      self.topoPilha = auxiliar

  def pop(self):
    if self.topoPilha != None:
      reserva = self.topoPilha.valores
      self.topoPilha = self.topoPilha.proxValor
      return reserva
    else:
      logging.error(f'O topo da pilha se encontra vazio')
      
  def impriTopo(self):
    if self.topoPilha == None:
      logging.error(f'O topo da pilha se encontra vazio')
    else:
      return self.topoPilha.valores

  def soma(self):
    return self.topoPilha.valores.sum()

  def reverso(self):
    return np.flip(self.topoPilha.valores)

#MAIN
#ALOCANDO E SOMANDO DADOS  
pilhaHOT = Pilha()

tPInicio1 = time.process_time() 
pilhaHOT.push(numeros)
tPFinal1 = time.process_time() 

print(f'Alocacao de dados na PILHA: {round(1000*(tPFinal1 - tPInicio1),5)} ms')
  
for i in pilhaHOT.impriTopo():
  tPInicio2 = time.process_time()
  i = pilhaHOT.soma()
  tPFinal2 = time.process_time()
  
pilhaHOT.push(i)

print(f'Soma de dados da PILHA: {round(1000*(tPFinal2 - tPInicio2),5)} ms')

pilhaHOT.pop()

'----------------------------------------------------'
#VERIFICANDO SE A UM INTEIRO QUALQUER

tPInicioV = time.process_time()
equal = (numeros == pilhaHOT.impriTopo()).all()
if equal == True:
  pass
else:
  logging.error(f'Numero não consta na Pilha')
tPFinalV = time.process_time() 

print(f'\nVerificao de todos os numeros na PILHA : {round(1000*(tPFinalV - tPInicioV),5)} ms')

'----------------------------------------------------'
#ALOCANDO E SOMANDO DADOS NA ORDEM CONTRARIA
tPInicioR1 = time.process_time()
pilhaHOT.reverso()
tPFinalR1 = time.process_time()

print(f'\nAlocacao de dados reversos na PILHA: {round(1000*(tPFinalR1 - tPInicioR1),5)} ms')

for i in pilhaHOT.reverso():
  tPInicioR2 = time.process_time()
  pilhaHOT.push(i)
  i = pilhaHOT.soma()
  tPFinalR2 = time.process_time()
  
pilhaHOT.push(i)

print(f'Soma de dados reversos da PILHA: {round(1000*(tPFinalR2 - tPInicioR2),5)} ms')

pilhaHOT.pop()

'----------------------------------------------------'
#VERIFICANDO SE A UM INTEIRO QUALQUER PILHA ORDEM REVERSA
tPInicioV1 = time.process_time()
equal = (numeros == pilhaHOT.reverso()).all()
if equal == True:
  pass
else:
  logging.error(f'Numero não consta na Pilha')
tPFinalV1 = time.process_time() 

print(f'\nVerificao de todos os numeros na PILHA ordem reversa: {round(1000*(tPFinalV1 - tPInicioV1),5)} ms')  

