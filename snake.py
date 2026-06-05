import curses
import random
import time

def main(stdscr):
    # Set up curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh every 100ms
    sh, sw = stdscr.getmaxyx()

    # Initial snake position and body
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # Initial food position
    food = [sh // 2, sw // 2]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    # Initial direction
    key = curses.KEY_RIGHT

    score = 0

    while True:
        stdscr.border(0)
        stdscr.addstr(0, 2, f' Score: {score} ')
        next_key = stdscr.getch()
        
        # Support WASD and Arrow Keys
        if next_key in [ord('w'), ord('W'), curses.KEY_UP]:
            if key != curses.KEY_DOWN: key = curses.KEY_UP
        elif next_key in [ord('s'), ord('S'), curses.KEY_DOWN]:
            if key != curses.KEY_UP: key = curses.KEY_DOWN
        elif next_key in [ord('a'), ord('A'), curses.KEY_LEFT]:
            if key != curses.KEY_RIGHT: key = curses.KEY_LEFT
        elif next_key in [ord('d'), ord('D'), curses.KEY_RIGHT]:
            if key != curses.KEY_LEFT: key = curses.KEY_RIGHT
        elif next_key == 27: # ESC key
            break

        # Check for Game Over (Hitting walls or self)
        if (snake[0][0] in [0, sh - 1] or 
            snake[0][1] in [0, sw - 1] or 
            snake[0] in snake[1:]):
            break

        # Calculate new head
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Move snake
        snake.insert(0, new_head)

        # Check if snake ate food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        # Draw snake
        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

    # Game Over Message
    stdscr.nodelay(0)
    msg = f"Game Over! Score: {score}"
    stdscr.addstr(sh // 2, (sw - len(msg)) // 2, msg)
    stdscr.refresh()
    time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)
