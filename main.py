"""Starter Snake game with optional OpenClaw hints (press H)."""
from __future__ import annotations
import random
import pygame
from openclaw_bridge import ask_openclaw

CELL, COLS, ROWS, FPS = 20, 30, 24, 10
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL
BG, GRID, SNAKE, FOOD, TEXT = (18,22,30), (31,38,49), (92,210,130), (244,100,100), (238,242,247)


def random_free_cell(snake):
    free = [(x,y) for x in range(COLS) for y in range(ROWS) if (x,y) not in snake]
    return random.choice(free) if free else None


def new_game():
    snake = [(COLS//2, ROWS//2), (COLS//2-1, ROWS//2)]
    return snake, (1,0), random_free_cell(snake), 0, False, "Mũi tên/WASD: di chuyển | H: hỏi OpenClaw"


def draw_text(screen, font, text, x, y, color=TEXT):
    screen.blit(font.render(text, True, color), (x,y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Roguelike Snake + OpenClaw")
    clock, font, small = pygame.time.Clock(), pygame.font.Font(None,25), pygame.font.Font(None,20)
    snake, direction, food, score, game_over, message = new_game()
    dirs = {pygame.K_UP:(0,-1),pygame.K_w:(0,-1),pygame.K_DOWN:(0,1),pygame.K_s:(0,1),
            pygame.K_LEFT:(-1,0),pygame.K_a:(-1,0),pygame.K_RIGHT:(1,0),pygame.K_d:(1,0)}
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                elif event.key == pygame.K_r and game_over:
                    snake, direction, food, score, game_over, message = new_game()
                elif event.key == pygame.K_h:
                    prompt = f"Cho một gợi ý ngắn để chơi Snake. Điểm: {score}; đầu rắn: {snake[0]}; thức ăn: {food}. Chỉ đưa lời khuyên."
                    message = "Đang hỏi OpenClaw..."
                    pygame.display.flip()
                    message = ask_openclaw(prompt)
                elif event.key in dirs and not game_over:
                    candidate = dirs[event.key]
                    if candidate != (-direction[0],-direction[1]): direction = candidate
        if not game_over:
            head = snake[0]
            nxt = (head[0]+direction[0], head[1]+direction[1])
            eating = nxt == food
            collision_body = snake if eating else snake[:-1]
            if not (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS) or nxt in collision_body:
                game_over, message = True, "Game over! Nhấn R để chơi lại."
            else:
                snake.insert(0,nxt)
                if eating:
                    score += 1
                    food = random_free_cell(snake)
                    if food is None: game_over, message = True, "Bạn đã thắng! Nhấn R để chơi lại."
                else: snake.pop()
        screen.fill(BG)
        for x in range(0,WIDTH,CELL): pygame.draw.line(screen,GRID,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,CELL): pygame.draw.line(screen,GRID,(0,y),(WIDTH,y))
        if food is not None: pygame.draw.rect(screen,FOOD,(food[0]*CELL+2,food[1]*CELL+2,CELL-4,CELL-4),border_radius=5)
        for i,(x,y) in enumerate(snake):
            inset = 1 if i == 0 else 2
            pygame.draw.rect(screen,SNAKE,(x*CELL+inset,y*CELL+inset,CELL-2*inset,CELL-2*inset),border_radius=4)
        draw_text(screen,font,f"Điểm: {score}",8,6)
        if game_over: draw_text(screen,font,"GAME OVER",WIDTH//2-60,HEIGHT//2-18,FOOD)
        shown = message.replace("\n"," ")
        if len(shown)>100: shown = shown[:97]+"..."
        draw_text(screen,small,shown,8,HEIGHT-23)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__": main()
