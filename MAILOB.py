import turtle

def dibujar_corazon():
    turtle.color("red")
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def dibujar_corazon2():
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()    

def dibujar_mensaje():
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    
    turtle.write("Te amo Mary", font=("Arial", 12, "normal"))

# Configurar la ventana de Turtle
turtle.title("Mensaje de Amor con Corazón")
turtle.bgcolor("Black")
turtle.color("darkred")
turtle.speed(2)

# Llamar a las funciones para dibujar el corazón y el mensaje
dibujar_corazon()
dibujar_corazon2()
dibujar_mensaje()

# Mantener la ventana abierta
turtle.done()
