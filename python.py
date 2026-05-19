import turtle
import random

WIDTH = 600
HEIGHT = 600

COLORS = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "black",
    "purple",
    "pink",
    "brown",
    "cyan"
]


def main():
    racers = get_number_of_racers()

    init_turtle()

    random.shuffle(COLORS)

    colors = COLORS[:racers]

    winner = race(colors)

    print(f"The winner is: {winner}")

    turtle.done()


def get_number_of_racers():
    while True:
        racers = input("Enter number of racers (2-10): ")

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric.")
            continue

        if 2 <= racers <= 10:
            return racers

        print("Number must be between 2 and 10.")


def init_turtle():
    screen = turtle.Screen()

    screen.setup(WIDTH, HEIGHT)

    screen.title("Turtle Racing Game")


def create_turtles(colors):
    turtles = []

    spacingx = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):

        racer = turtle.Turtle()

        racer.shape("turtle")

        racer.color(color)

        racer.left(90)

        racer.penup()

        racer.setpos(
            -WIDTH // 2 + (i + 1) * spacingx,
            -HEIGHT // 2 + 20
        )

        racer.pendown()

        turtles.append(racer)

    return turtles


def race(colors):

    turtles = create_turtles(colors)

    while True:

        for racer in turtles:

            distance = random.randrange(1, 20)

            racer.forward(distance)

            x, y = racer.pos()

            if y >= HEIGHT // 2 - 10:

                winner = colors[turtles.index(racer)]

                return winner


if __name__ == "__main__":
    main()
