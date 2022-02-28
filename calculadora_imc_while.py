#Este prgrama calcula en indice de masa corporal de una persona.
import os 
import platform

def limpiar_pantalla():
    os.system('clear')

print('Este prgrama calcula en indice de masa corporal de una persona.');
comienzo =int(input('Desea comenzar ? 1=SI , 0= No : '));

while comienzo >=1 :
    peso = float(input('Ingrese su peso en KG: '));
    altura = float(input('Ingrese su altura en M : '));
    imc = peso / (altura*altura)
    print(f'Su indice de masa corporal es: {imc}');

    print(' ');
    if imc < 18.5 :
          print('Tiene un peso, basjo de lo normal');
    elif  imc > 18.5 and imc < 24.9:
          print('Tiene un peso normal');
    elif imc > 24.9 and imc < 29.9 :
          print('Tiene sobre peso.'); 
    elif imc > 29.9 :
          print('Tiene obesidad');

    print('');
    comienzo = int(input('Desea continuar ? 1=SI, 0=NO :  '))
    if comienzo >= 1:
        limpiar_pantalla()
        print('Continuamos¡¡');
    else:
        print('');

print ('Gracias por su tiempo');
print('Saludos');
