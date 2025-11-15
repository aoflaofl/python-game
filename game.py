"""Basic Pygame Zero stub application."""

import pgzrun

WIDTH = 800
HEIGHT = 600

TITLE = "Python Game Stub"

message = "Hello from Pygame Zero!"

alien = Actor('alien')
alien.pos = 100, 56


def draw():
    screen.clear()
    screen.fill((128, 30, 30))
    screen.draw.text(
        message,
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=48,
        color="white",
    )
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'


if __name__ == "__main__":
    pgzrun.go()
