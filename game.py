"""Basic Pygame Zero stub application."""

import pgzrun

WIDTH = 800
HEIGHT = 600

TITLE = "Python Game Stub"

message = "Hello from Pygame Zero!"


def draw():
    screen.clear()
    screen.fill((30, 30, 30))
    screen.draw.text(
        message,
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=48,
        color="white",
    )


if __name__ == "__main__":
    pgzrun.go()
