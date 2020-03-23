import re

def validarContraseña(contraseña):
  print("La contraseña",end=" ");
  print("es valida" if validarPatron(contraseña) else " no es valida");

def validarPatron(contraseña):
  patron = re.compile("^[A-Z]\d{3}[a-z]+[^\w]{3}$");
  return patron.search(contraseña);

contraseña = input("Ingrese la contraseña: ");
validarContraseña(contraseña);