import turtle
import _tkinter
import tkinter
def draw_koch_segment(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        draw_koch_segment(t, length / 3, depth - 1)
        t.left(60)
        draw_koch_segment(t, length / 3, depth - 1)
        t.right(120)
        draw_koch_segment(t, length / 3, depth - 1)
        t.left(60)
        draw_koch_segment(t, length / 3, depth - 1)

def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        draw_koch_segment(t, length, depth)
        t.right(120)

def main():
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    # Початкова позиція
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    draw_koch_snowflake(t, 300, recursion_level)

    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()


