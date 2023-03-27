import turtle

# Define the sample family tree
family_tree = [
    "Grandpa",
    [
        "Dad",
        [
            "Child 1",
            "Child 2"
        ]
    ],
    "Uncle"
]

# Define the Turtle graphics settings
turtle.setup(800, 600)
turtle.bgcolor("white")
turtle.pensize(2)
turtle.speed(0)

# Define the position of the first node
x_pos = 0
y_pos = 0

# Define the function to draw a node
def draw_node(name, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.goto(x, y - 70)
    turtle.write(name, align="center", font=("Arial", 16, "normal"))

# Define the function to draw a connection between two nodes
def draw_connection(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1 - 50)
    turtle.pendown()
    turtle.goto(x2, y2 + 50)

# Define the function to recursively draw the family tree
def draw_family_tree(tree, x, y):
    # Draw the current node
    draw_node(tree[0], x, y)
    # If the current node has children, draw connections to them and recursively draw the children
    if len(tree) > 1:
        child_x = x - (len(tree[1]) * 100) // 2
        child_y = y - 150
        for child in tree[1]:
            child_width = len(child) * 15
            draw_connection(x, y, child_x + child_width // 2, child_y)
            draw_family_tree(child, child_x + child_width // 2, child_y)
            child_x += child_width + 50

# Draw the family tree
draw_family_tree(family_tree, x_pos, y_pos)

# Exit on click
turtle.exitonclick()
