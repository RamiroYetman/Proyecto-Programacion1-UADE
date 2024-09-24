import re

def validar_dni(cad):
    '''
    pre: toma por parametro una cadena y determina el patron del xx.xxx.xxx
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "[0-9]{8}+"
    return re.match(patron,cad) 
    
def validar_email(cad):
    '''
    pre: toma por parametro una cadena y determina un patron de mail
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9]+\.[a-z]+$"
    return re.match(patron,cad)

def validar_telefono(cad):
    '''
    pre: toma por parametro una cadena y determina el patron del xxx-6
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "[0-9]{3}-[0-9]{6,}"
    return re.match(patron,cad)
def validar_id(num):
  return num >=1 and num <=6