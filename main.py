# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Persona:
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año    = año

    def descripcion(self):
        return '{} tiene {} años de edad. '.format(self.nombre, self.año)

    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)

class Email:
    pass
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
# Por defecto 'enviado' vale False
print(mi_correo.enviado)
# Cambiar a 'enviado' de la instancia enviar_correo pasa a valer True
mi_correo.enviar_correo()
print(mi_correo.enviado)

frase = "la cruda realidad es que los políticos como la sociedad en general, no están de acuerdo a las pautas Biblicas."
Doctor = Persona('Diego', 39)

print(Doctor.descripcion())
print(Doctor.comentario(frase))



