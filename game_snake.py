import turtle
import time
import random

#Creacion del espacio del juego

pantalla = turtle.Screen() # Creación de la pantalla
pantalla.setup(700,700) #Tamaño de la pantalla
pantalla.bgcolor('#aaa') #Color de fondo
pantalla.title('Snake Game') #Titulo de la pantalla

#Creación del jugador

serpiente = turtle.Turtle() 
serpiente.speed(1) # Velocidad inicial
serpiente.shape('circle') #Forma de la serpiente
serpiente.penup() #Esto hace que la serpiente no dibuje una linea cuando avance
serpiente.goto(0,0) #Que inicie en el centro de la pantalla
serpiente.direction = 'stop' # 'stop' #Detiene la serpiente cuando se reinicia el juego
serpiente.color('#449C4A') #Color de la serpiente
retraso = 0.1

#Creacion de la comida

comida = turtle.Turtle()
comida.shape('turtle')
comida.color('black')
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = [] #Incremento del cuerpo, se usa en While de movimiento

#Movimiento de la serpiente

#Movimiento por teclado

def arriba():
    serpiente.direction = 'up'

def abajo():
    serpiente.direction = 'down'

def izquierda():
    serpiente.direction = 'left'

def derecha():
    serpiente.direction = 'right'

#Funcion que se va a repetir hasta que termine el programa

def movimiento():
    if serpiente.direction == 'up': #Si la direccion de la serpiente es 'up'
        y = serpiente.ycor() #'y' es igual a su posición actual
        serpiente.sety(y + 20) #Posición actual más 20px
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

#Evento de escucha del teclado para el movimiento

pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(izquierda, "Left")
pantalla.onkeypress(derecha, "Right")

#loop de movimiento del juego

while True:
    serpiente._update() # Actualización de la posición de la serpiente
    
    #En caso de tocar uno de los bordes de si mismo
    
    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(1)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop'
        cuerpo.clear()

    if serpiente.distance(comida) < 20: #Cuando la serpiente toca la tortuga, ésta, reaparece en otro lugar random
        x = random.randrange(-300, 300, 20)
        y =  random.randrange(-300, 300, 20)
        comida.goto(x, y)
        nuevo_cuerpo = turtle.Turtle()#Creacion del incremento de la serpiente
        nuevo_cuerpo.shape('circle')
        nuevo_cuerpo.color('#449C4A')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo) #Se agrega la nueva parte del cuerpo en la lista 'cuerpo'

    #Vamos a agregar el cuerpo a la serpiente

    total = len(cuerpo)

    for index  in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0: #El primer elemento creado, no sigue a otro elemento similar, si no a la serpiente principal
        x = serpiente.xcor() #Se obtienen las coodenadas del la serpiente principal
        y = serpiente.ycor()
        cuerpo[0].goto(x, y) #Se envía el primer elemento a las coordenadas de la serpiente principal

    movimiento()# Movimiento de la serpiente

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction= 'stop'

    time.sleep(retraso) #Retraso del movimiento
    #Repetición


turtle.done()