from turtle import Screen
from snake_body import Snake
from scoreboard import ScoreBoard
from food import Food

import time



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
scoreboard=ScoreBoard()
food=Food()

level_choisi=screen.textinput(title="Level choice",prompt="Choose a level: diff/normal/easy").lower()
    


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

try :
    with open("score_file.txt","r") as file :
        for line in file :
            if "Level_diff" in line:
                score_dif=int(line.split("=")[-1])
            elif "Level_normal" in line:
                score_norm=int(line.split("=")[-1])
            elif "Level_easy" in line:
                score_easy=int(line.split("=")[-1])
except FileNotFoundError:
    with open("score_file.txt","w") as file :
        score_dif=0
        score_easy=0
        score_norm=0
        file.write(f"Level_diff={score_dif}\nLevel_normal={score_norm}\nLevel_easy={score_easy}")
        
            


def compare_score(update_score,last_score):
   return update_score> last_score
        



    
game_is_over=False

while not game_is_over:
    screen.update()
    if level_choisi=="diff":
        time.sleep(0.05)
        if compare_score(scoreboard.score,score_dif):
            score_dif=scoreboard.score
        
    elif level_choisi=="normal":
        time.sleep(0.1)
        
        if compare_score(scoreboard.score,score_norm):
            score_norm=scoreboard.score
    else:
        time.sleep(0.5)
        if compare_score(scoreboard.score,score_easy):
            score_easy=scoreboard.score
    
    
    snake.move()
    scoreboard.show_score()
    
    # Detection with wall
    
    if snake.head.xcor()< -285 or snake.head.xcor()>285 or snake.head.ycor()< -285 or snake.head.ycor()> 285 :
        game_is_over=True
        scoreboard.game_over()
    # Detection with food 
    
    if snake.head.distance(food)<15:
        food.random_place()
        scoreboard.score+=1
        snake.extend()
        
    # Detection with tail
    
    for segment in  snake.segments[1:] :
        if snake.head.distance(segment) < 15 :
            game_is_over=True
            scoreboard.game_over()
            
    if game_is_over:
        
        with open ("score_file.txt","w") as file :
                file.write(f"Level_diff={score_dif}\nLevel_normal={score_norm}\nLevel_easy={score_easy}")
                


screen.exitonclick()