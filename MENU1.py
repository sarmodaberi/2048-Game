import pygame

pygame.init()


# تنظیمات صفحه
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("صفحه اصلی")

# متغیرهای بازی
game_paused = False

# فونت و رنگ‌ها
FONT = pygame.font.SysFont("comicsans", 40, bold=True)
TEXT_COLOR = (0, 0, 0)
HOVER_COLOR = (100, 100, 100)
BUTTON_COLOR = (200, 200, 200)

# موقعیت دکمه‌ها
buttons = {
    "Sound": pygame.Rect(300, 150, 200, 50),
    "New Game": pygame.Rect(300, 250, 200, 50),
    "Continue": pygame.Rect(300, 350, 200, 50),
    "Records": pygame.Rect(300, 450, 200, 50),
    "Exit": pygame.Rect(300, 550, 200, 50),
}

def draw_button(screen, text, font, color, hover_color, rect, hovered):
    """ تابع برای رسم دکمه با قابلیت تغییر رنگ هنگام هاور شدن """
    pygame.draw.rect(screen, hover_color if hovered else color, rect, border_radius=10)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def draw_text(text, font, color, x, y):
    """ تابع برای رسم متن روی صفحه """
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


# حلقه بازی
run = True
while run:
    screen.fill((205, 192, 180))  # رنگ پس‌زمینه
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    if game_paused:

        for text, rect in buttons.items():
            hovered = rect.collidepoint(mouse_pos)
            draw_button(screen, text, FONT, BUTTON_COLOR, HOVER_COLOR, rect, hovered)

            if hovered and mouse_click:  # بررسی کلیک روی دکمه
                if text == "Sound":
                    print("Sound Button Clicked")
                elif text == "New Game":
                    print("Starting New Game")
                elif text == "Continue":
                    game_paused = False  # ادامه بازی
                elif text == "Records":
                    print("Viewing Records")
                elif text == "Exit":
                    run = False  # خروج از برنامه

    else:
        draw_text("Press SPACE to Pause", FONT, TEXT_COLOR, 220, 250)

    # مدیریت رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_paused = not game_paused  # تغییر وضعیت توقف بازی

    pygame.display.update()

pygame.quit()