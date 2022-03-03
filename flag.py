import turtle
vin = turtle.Turtle()
wn = turtle.Screen()          
wn.bgcolor("red")             
screen_width = 600;           
screen_height = 350;          
star_length = 200;            
 
wn.setup(width = screen_width, height = screen_height)
wn.title("Flag of Vietnam")
                # Set the color of the turtle to red
# Move the turtle to a predefined coordinate
vin.color("yellow")
vin.penup()
vin.setx((screen_width - star_length)/2 - screen_width/2)
vin.sety(star_length/4)
vin.color("yellow")
vin.shape("blank")             
vin.pensize(3)                 
 
vin.begin_fill()
# Draw the flag
for counter in range(5):
    vin.forward(star_length)                 
    vin.right(144)
vin.end_fill()
 
