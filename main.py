from snake import Snake
from food import Food
from score import Score

if __name__ == '__main__':
    # constants
    WINDOW_TITLE = "Snake Py - steezyouthere"
    SNAKE_SPEED = 0.1
    FOOD_DISTANCE = 15
    WALL_DISTANCE = 290
    TAIL_DISTANCE = 5
    SPEED_LIMIT = 20
    SPEED_INCREMENT = 0.5

    # screen setup
    from turtle import Screen
    s = Screen()
    s.setup(width=600, height=600)
    s.title(WINDOW_TITLE)
    s.bgcolor("black")
    s.tracer(0)

    # init objects
    snake = Snake()
    food = Food()
    score = Score()

    # load key listeners
    snake.controls()

    # generate snake
    snake.start()

    game_is_active = True
    while game_is_active:
        s.update()
        import time
        time.sleep(SNAKE_SPEED)

        snake.move()
        # check for food collision
        if snake.head.distance(food) < FOOD_DISTANCE:
            score.increase_score()
            snake.extend()
            food.refresh()
            if snake.speed < SPEED_LIMIT:
                snake.speed += SPEED_INCREMENT

        # check for wall collision
        if snake.head.xcor() > WALL_DISTANCE or snake.head.xcor() < -WALL_DISTANCE or snake.head.ycor() > WALL_DISTANCE or snake.head.ycor() < -WALL_DISTANCE:
            game_is_active = False
            score.game_over()

        # check for tail collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < TAIL_DISTANCE:
                game_is_active = False
                score.game_over()

    s.exitonclick()
