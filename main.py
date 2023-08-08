from classes import *
import sys


def game():

    player = PLayer((WIDTH / 2, 200), player_big_img)

    #text_game = font_text.render("Game", False, (0, 0, 0))


    objet_group = pygame.sprite.Group()
    objet_group.add(player)
    clock = pygame.time.Clock()
    min_fps = 200
    while True:
        pressed_button = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        hitbox_floor = Images(hitbox_img, (WIDTH / 2, 593))
        floor_1 = Images(level1_floor_img,(WIDTH / 2, HEIGHT / 2))

        level1_images_gr = pygame.sprite.Group()
        level1_images_gr.add(hitbox_floor)
        level1_images_gr.add(floor_1)

        SCREEN.blit(level1_back_img, (-100, 0))
        objet_group.draw(SCREEN)
        level1_images_gr.draw(SCREEN)
        pygame.display.flip()


        player.update(12)
        player.falling(hitbox_floor)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if min_fps > clock.get_fps() > 0:
            min_fps = clock.get_fps()

        clock.tick(FPS)



def main_menu():


    # pygame.mixer.music.load(menu_fon_music)
    # pygame.mixer.music.set_volume(music_volume)
    # pygame.mixer.music.play(-1)

    pygame.display.set_caption("GAME")

    play_btn = Button(play_btn_img, (WIDTH / 2, HEIGHT * 0.44))
    #options_btn = Button(options_btn_img, (WIDTH / 2, HEIGHT * 0.33))
    exit_btn = Button(exit_btn_img, (WIDTH / 2, HEIGHT * 0.66))
    heading_img = Images(heading_menu_img, (WIDTH / 2, HEIGHT * 0.12))

    buttons_gr = pygame.sprite.Group()
    images_gr = pygame.sprite.Group()
    buttons_gr.add(play_btn, exit_btn)
    images_gr.add(heading_img)

    SCREEN.blit(fon_img, (0, 0))
    buttons_gr.draw(SCREEN)
    images_gr.draw(SCREEN)

    pygame.display.flip()
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_btn.rect.collidepoint(mouse_pos):
                    SCREEN.blit(fon_img, (0, 0))
                    game()
                elif exit_btn.rect.collidepoint(mouse_pos):
                    sys.exit()


main_menu()
