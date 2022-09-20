import turtle
import time
import random

#Creacion del espacio del juego

pantalla = turtle.Screen() # Creación de la pantalla
pantalla.setup(750,750) #Tamaño de la pantalla
pantalla.bgcolor('#fef') #Color de fondo
pantalla.title('Snake Game') #Titulo de la pantalla

#Creación del jugador

serpiente = turtle.Turtle() 
serpiente.speed(1) # Velocidad inicial
serpiente.shape('circle') #Forma de la serpiente
serpiente.penup() #Esto hace que la serpiente no dibuje una linea cuando avance
serpiente.goto(0,0) #Que inicie en el centro de la pantalla
serpiente.direccion = 'stop' #Detiene la serpiente cuando se reinicia el juego
serpiente.color("#449C4A") #Color de la serpiente

turtle.done()