from random import randint
import pygame
import asyncio

# Initialize Pygame
pygame.init()

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

# Load the images for Actor
fox = pygame.image.load("fox.png")
fox_rect = fox.get_rect(topleft=(100, 100))

coin = pygame.image.load("coin.png")
coin_rect = coin.get_rect(topleft=(200, 200))

# Load the background image
background = pygame.image.load("background.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

async def main():
    global game_over  # Declare game_over as a global variable

    # Set up the Pygame screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Coin Collector Game")

    # Load the music file
    pygame.mixer.music.load("music.mp3")

    # Play the music file in an infinite loop
    pygame.mixer.music.play(-1)

    def draw(screen):  # Pass screen as a parameter
        screen.blit(background, (0, 0))  # Draw the background first
        screen.blit(fox, fox_rect)
        screen.blit(coin, coin_rect)
        screen.blit(pygame.font.SysFont(None, 30).render("Score: " + str(score), True, (0, 0, 0)), (10, 10))

        if game_over:
            screen.fill((128, 0, 0))  # Use RGB values for the maroon color
            screen.blit(pygame.font.SysFont(None, 60).render("Score: " + str(score), True, (245, 222, 179)), (100, 100))

    def place_coin():
        coin_rect.x = randint(20, WIDTH - 20)
        coin_rect.y = randint(20, HEIGHT - 20)

    def time_up():
        global game_over  # Use global to modify the outer function's variable
        game_over = True

    def update():
        global score

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            fox_rect.x -= 8
        elif keys[pygame.K_RIGHT]:
            fox_rect.x += 8
        elif keys[pygame.K_UP]:
            fox_rect.y -= 8
        elif keys[pygame.K_DOWN]:
            fox_rect.y += 8

        coin_collected = fox_rect.colliderect(coin_rect)

        if coin_collected:
            score += 10
            place_coin()

    pygame.time.set_timer(pygame.USEREVENT, 15000)  # Set up a timer event every 15 seconds
    place_coin()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.USEREVENT:  # Timer event
                time_up()

        update()
        draw(screen)  # Pass screen to the draw function
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # 60 frames per second

    pygame.quit()

# Run the main function
asyncio.run(main())
