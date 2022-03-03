import turtle
p = turtle.Turtle()
p.color("yellow")
p.penup()
sc = turtle.Screen()          
sc.bgcolor("red")             
screen_width = 600;           
screen_height = 350;          
star_length = 200;            
 
sc.setup(width = screen_width, height = screen_height)
sc.title("Flag of Vietnam")

p.setx((screen_width - star_length)/2 - screen_width/2)
p.sety(star_length/4)
p.shape("blank")             
p.pensize(3)                 
p.begin_fill()

# Draw the flag
for counter in range(5):
    p.forward(star_length)                 
    p.right(144)
p.end_fill()
p.penup()
p.hideturtle()
p.penup()
p.goto(0,-150)
p.pendown()
p.write("VietNam's National Flag", False, align="center",font=("Arial",30,"normal"))
turtle.done()

 
