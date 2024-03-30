"""
This  code is underconstruction , i want to write snake game , that a user can tap yes or no 
to continue to play game , bat not to rerun in consol .
Please enjoy to add your idea 
"""




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

def compare_score(update_score,last_score):
        if update_score> last_score:
            last_score=update_score
            return True
        else :
            return False
            

def game(screen):
    snake=Snake()
    scoreboard=ScoreBoard()
    food=Food()
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
            
                
      
    game_is_over=False

    while not game_is_over:
        screen.update()
        if level_choisi=="diff":
            time.sleep(0.05)
            compare_score(scoreboard.score,score_dif)
            
        elif level_choisi=="normal":
            time.sleep(0.1)
            compare_score(scoreboard.score,score_norm)
            
        else:
            time.sleep(0.5)
            compare_score(scoreboard.score,score_easy)
            
        
        
        
        snake.move()
        scoreboard.show_score()
        
        # Detection with wall
        
        if snake.head.xcor()< -285 or snake.head.xcor()>285 or snake.head.ycor()< -285 or snake.head.ycor()> 285 :
            game_is_over=True
            scoreboard.game_over()
            del snake
            del food
            del scoreboard
        # Detection with food 
        
        if snake.head.distance(food)<15:
            food.random_place()
            scoreboard.score+=1
            snake.extend()
            
        # Detection with tail
        
        for segment in  snake.segments[1:] :
            if snake.head.distance(segment) <15 :
                game_is_over=True
                scoreboard.game_over()
                del snake
                del food
                del scoreboard
                
        with open ("score_file.txt","w") as file :
                file.write(f"Level_diff={score_dif}\nLevel_normal={score_norm}\nLevel_easy={score_easy}")
                

    return game_is_over

play_more=True
while play_more:
    
    
    
    if game(screen):
        
        play_again=screen.textinput(title="Play again",prompt="Guess \"yes\" to play again or \"no\" to stop").lower()
        if play_again=="no":
            play_more=False
        else:
            report_game=game(screen)
screen.exitonclick()

            
                
            