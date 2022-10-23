import turtle

timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("yellow")
timmy.shapesize(10, 10)
timmy.pencolor("red")
timmy.fillcolor("green")
timmy.forward(100)
my_screen = turtle.Screen()
print(my_screen.canvheight)

my_screen.exitonclick()


import prettytable

table = prettytable.PrettyTable()
table.align = "l"
table.field_names = ["Name", "Type"]
table.add_row(["Barbarian", "Elixir Troop"])
table.add_row(["P.E.K.K.A", "Elixir Troop"])
table.add_row(["Hog Rider", "Dark Elixir Troop"])
table.add_row(["Bowler", "Dark Elixir Troop"])
print(table)