import pygame;
import sys
import os
from button import Button
#Youtube video used for reference: https://www.youtube.com/watch?v=AY9MnQ4x3zk


#ADD COLORS HERE(use hexadecimal):
Mint_green = '#008080'

screen_width = 1280
screen_height = 720

# pygame setup - always gotta do this. dont mind this code
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))# display surface. only one of them. you add to this 
pygame.display.set_caption("Financial Literacy")
clock = pygame.time.Clock()
running = True

Font_Everything = pygame.font.Font(None, 50) #the font used for everything


#HOW TO ADD IMAGES - to run file, we need to use move into frontend in our terminal(command: cd theNameOfTheFilesToGetIn)
#1. since we are in frontend, we need to go back to src. then from src we are going into files to grab the image
background_Path = os.path.join('..', 'files', 'background2.png') # this is grabbing the path
background_image = pygame.image.load(background_Path)# put path into loading image

#ADDING MORE IMAGES
background_Path2 = os.path.join('..', 'files', 'start.png')
SecondScreen_image = pygame.image.load(background_Path2) # switching to this

#
scenario_1_background = os.path.join('..', 'files', 'scenario_1.png') 
scenario_1_background = pygame.image.load(scenario_1_background)
scenario_1_dorm_result = os.path.join('..', 'files', 'scenario_1_dorm_result.png')
scenario_1_dorm_result = pygame.image.load(scenario_1_dorm_result)
scenario_1_rental_result = os.path.join('..', 'files', 'scenario_1_rental_result.png')
scenario_1_rental_result = pygame.image.load(scenario_1_rental_result)
scenario_1_parents_result = os.path.join('..', 'files', 'scenario_1_parents_result.png')
scenario_1_parents_result = pygame.image.load(scenario_1_parents_result)

scenario_2_background = os.path.join('..', 'files', 'scenario_2.png')
scenario_2_background = pygame.image.load(scenario_2_background)
scenario_2_job_result = os.path.join('..', 'files', 'scenario_2_job_result.png')
scenario_2_job_result = pygame.image.load(scenario_2_job_result)
scenario_2_nojob_result = os.path.join('..', 'files', 'scenario_2_nojob_result.png')
scenario_2_nojob_result = pygame.image.load(scenario_2_nojob_result)
scenario_2_paycheck_result = os.path.join('..', 'files', 'scenario_2_paycheck_result.png')
scenario_2_paycheck_result = pygame.image.load(scenario_2_paycheck_result)

scenario_3_background = os.path.join('..', 'files', 'scenario_3.png')
scenario_3_background = pygame.image.load(scenario_3_background)
scenario_3_job_rent_result = os.path.join('..', 'files', 'scenario_3_job_rent_result.png')
scenario_3_job_rent_result = pygame.image.load(scenario_3_job_rent_result)
scenario_3_job_buy_result = os.path.join('..', 'files', 'scenario_3_job_buy_result.png')
scenario_3_job_buy_result = pygame.image.load(scenario_3_job_buy_result)
scenario_3_job_no_result = os.path.join('..', 'files', 'scenario_3_job_no_result.png')
scenario_3_job_no_result = pygame.image.load(scenario_3_job_no_result)

scenario_3_nojob_rent_result = os.path.join('..', 'files', 'scenario_3_nojob_rent_result.png')
scenario_3_nojob_rent_result = pygame.image.load(scenario_3_nojob_rent_result)
scenario_3_nojob_buy_result = os.path.join('..', 'files', 'scenario_3_nojob_buy_result.png')
scenario_3_nojob_buy_result = pygame.image.load(scenario_3_nojob_buy_result)
scenario_3_nojob_no_result = os.path.join('..', 'files', 'scenario_3_nojob_no_result.png')
scenario_3_nojob_no_result = pygame.image.load(scenario_3_nojob_no_result)

final_background = os.path.join('..', 'files', 'final.png')
final_background = pygame.image.load(final_background)

#ADD IMAGES WE WANT TO LOAD HERE:



#CODE USED TO ADD TO SCREEN: screen.blit(image,position in a tuple (0,0)) Ex. screen.blit(background_image,(0,0)



#STATES
current_state = 'start'

#CHANGING STATES FUNCTIONS
#how we change the scenario based on the option clicked
            
def switch_to(switch):
    global current_state
    current_state = switch 



#BUTTONS TO SWITCH 
 #NOTE:(screen_width // 2 - pos_button_width, screen_height // 2 - pos_button_width, boarder_button_height, boarder_button_width)
 #NOTE: we can use print statements to find where the button is and then adjust the
 #PROBLEM: have to adjust the size of the outline to the word 
    
#IMPORTANT TO MOVE
 # + 240 on the screen_height puts it bellow the text
 # -/+ 240 on the screen_width puts it 
 # 50 is the middle
 #(screen_width // 2 - pos_button_width, screen_height // 2 - pos_button_width, boarder_button_height, boarder_button_width)
 #PLAY AROUND WITH VALUES TO SEE HOW THEY WORK   
start_button = Button('Start', ((screen_width / 2) - (100 / 2), screen_height // 2 - 25, 100, 50), lambda: switch_to('second'))
second_button = Button('Next', ((screen_width / 2) - (100 / 2), screen_height // 2 + 240, 100, 50), lambda: switch_to('Scenario 1'))

# Buttons for choosing living
# ------------------------- SCENARIO 1 ----------------------
scenario_1_dorm_button = Button('Dorm', ((screen_width / 2) - ((525 + 50)/2), screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 1 Dorm Result'))
scenario_1_parents_button = Button('With Parents', ((screen_width / 2) - ((525 + 50)/2) + 175 + 25 , screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 1 Parents Result'))
scenario_1_rental_button = Button('Rental', ((screen_width / 2) - ((525 + 50)/2) + 350 + 50, screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 1 Rental Result'))

scenario_1_continue_result_button = Button('Continue', ( (screen_width / 2) - (150 / 2), screen_height // 2 + 240, 150, 50), lambda: switch_to('Scenario 2'))

scenario_2_job_button = Button('Get Job', ((screen_width / 2) - ((350 + 25) / 2), screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 2 Job Result'))
scenario_2_nojob_button = Button('No Job', ((screen_width / 2) - ((350 + 25) / 2) + 175 + 25, screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 2 No Job Result'))

scenario_2_job_continue_result_button = Button('Continue', ((screen_width / 2) - (150 / 2), screen_height // 2 + 240, 150, 50), lambda: switch_to('Scenario 2 Paycheck Result'))
scenario_2_paycheck_continue_result_button = Button('Continue', ((screen_width / 2) - (150 / 2), screen_height // 2 + 240, 150, 50), lambda: switch_to('Scenario 3'))
scenario_2_nojob_continue_result_button = Button('Continue', ((screen_width / 2) - (150 / 2), screen_height // 2 + 240, 150, 50), lambda: switch_to('Scenario 3'))

scenario_3_rent_button = Button('Rent', ((screen_width / 2) - ((525 + 50)/2), screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 3 Rent Result'))
scenario_3_buy_button = Button('Buy New', ((screen_width / 2) - ((525 + 50)/2) + 175 + 25, screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 3 New Result'))
scenario_3_no_button = Button('No Textbook', ((screen_width / 2) - ((525 + 50)/2) + 350 + 50, screen_height // 2 + 240, 175, 50), lambda: switch_to('Scenario 3 No Result'))

scenario_3_continue_result_button = Button('Continue', ((screen_width / 2) - (150 / 2), screen_height // 2 + 240, 150, 50), lambda: switch_to('Result'))

result_continue_result_button = Button('Continue', ((screen_width / 2) - (150 / 2), screen_height // 2 + 240, 150, 50), lambda: switch_to('Final'))



# Metrics
study_time = 100  # Percentage
account_balance = 1000  # Dollars
credit = 500  # Dollars
credit_score = 600  # Plain value

def draw_metrics(surface, study_time, account_balance, credit, credit_score):
    font = pygame.font.Font(None, 36)  # Adjust the size as needed

    # Define the starting position
    start_x = screen_width - 250  # Adjust based on your screen width and desired positioning
    start_y = 20
    line_height = 40  # Space between lines

    # Render each metric
    metrics = [
        f"Study Time: {study_time}%",
        f"Account: ${account_balance}",
        f"Credit: ${credit}",
        #f"Credit Score: {credit_score}"
    ]

    for i, metric in enumerate(metrics):
        text_surf = font.render(metric, True, (0, 0, 0))  # White color
        surface.blit(text_surf, (start_x, start_y + i * line_height))

# Job
job = False

scenario_1_metric_bool = True
scenario_2_metric_bool = True
scenario_3_metric_bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_state == 'start':
            start_button.handle_event(event)
        elif current_state == 'second':
            second_button.handle_event(event)
        
        elif current_state == 'Scenario 1':
            scenario_1_dorm_button.handle_event(event)
            scenario_1_parents_button.handle_event(event)
            scenario_1_rental_button.handle_event(event)

        elif current_state == 'Scenario 1 Dorm Result':
            scenario_1_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 1 Parents Result':
            scenario_1_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 1 Rental Result':
            scenario_1_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 2':
            scenario_2_nojob_button.handle_event(event)
            scenario_2_job_button.handle_event(event)

        elif current_state == 'Scenario 2 Job Result':
            scenario_2_job_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 2 No Job Result':
            scenario_2_nojob_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 2 Paycheck Result':
            scenario_2_paycheck_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 3':
            scenario_3_no_button.handle_event(event)
            scenario_3_rent_button.handle_event(event)
            scenario_3_buy_button.handle_event(event)

        elif current_state == 'Scenario 3 Rent Result':
            scenario_3_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 3 New Result':
            scenario_3_continue_result_button.handle_event(event)

        elif current_state == 'Scenario 3 No Result':
            scenario_3_continue_result_button.handle_event(event)

        elif current_state == 'Result':
            result_continue_result_button.handle_event(event)


        elif current_state == 'Final':
            pass


    # Render loop - draws the correct screen and button depending on the current state.
    
    if current_state == 'start':
        screen.blit(background_image, (0, 0))
        start_button.draw(screen)
    #NOTE: here should explain how it works
    elif current_state == 'second':
        screen.blit(SecondScreen_image, (0, 0)) #the image you want to be in when you switch state
        second_button.draw(screen) # a new button that will be used to go to the next state
    
    elif current_state == 'Scenario 1':
        screen.blit(scenario_1_background, (0, 0))
        scenario_1_parents_button.draw(screen)
        scenario_1_rental_button.draw(screen)
        scenario_1_dorm_button.draw(screen)

    elif current_state == 'Scenario 1 Dorm Result':
        if scenario_1_metric_bool:
            account_balance -= 1000
            scenario_1_metric_bool = False

        screen.blit(scenario_1_dorm_result, (0, 0))
        scenario_1_continue_result_button.draw(screen)

    elif current_state == 'Scenario 1 Parents Result':
        if scenario_1_metric_bool:
            account_balance -= 250
            study_time -= 20
            scenario_1_metric_bool = False

        screen.blit(scenario_1_parents_result, (0, 0))
        scenario_1_continue_result_button.draw(screen)

    elif current_state == 'Scenario 1 Rental Result':
        if scenario_1_metric_bool:
            account_balance -= 500
            study_time -= 5
            scenario_1_metric_bool = False

        screen.blit(scenario_1_rental_result, (0, 0))
        scenario_1_continue_result_button.draw(screen)

    elif current_state == 'Scenario 2':
        screen.blit(scenario_2_background, (0, 0))
        scenario_2_job_button.draw(screen)
        scenario_2_nojob_button.draw(screen)

    elif current_state == 'Scenario 2 Job Result':
        job = True
        screen.blit(scenario_2_job_result, (0, 0))
        scenario_2_job_continue_result_button.draw(screen)

    elif current_state == 'Scenario 2 No Job Result':
        if scenario_2_metric_bool:
            study_time = study_time + 10 if study_time < 90 else 100
            scenario_2_metric_bool = False

        screen.blit(scenario_2_nojob_result, (0, 0))
        scenario_2_nojob_continue_result_button.draw(screen)

    elif current_state == 'Scenario 2 Paycheck Result':
        if scenario_2_metric_bool:
            account_balance += 200
            study_time -= 10
            scenario_2_metric_bool = False

        screen.blit(scenario_2_paycheck_result, (0, 0))
        scenario_2_paycheck_continue_result_button.draw(screen)

    elif current_state == 'Scenario 3':
        screen.blit(scenario_3_background, (0, 0))
        scenario_3_rent_button.draw(screen)
        scenario_3_buy_button.draw(screen)
        scenario_3_no_button.draw(screen)

    elif current_state == 'Scenario 3 Rent Result':
        if job:
            if scenario_3_metric_bool:
                account_balance -= 125
                study_time = study_time + 10 if study_time < 90 else 100
                scenario_3_metric_bool = False


            screen.blit(scenario_3_job_rent_result, (0, 0))
        else:
            if scenario_3_metric_bool:
                credit -= 125
                study_time = study_time + 10 if study_time < 90 else 100
                scenario_3_metric_bool = False
            screen.blit(scenario_3_nojob_no_result, (0, 0))
        scenario_3_continue_result_button.draw(screen)

    elif current_state == 'Scenario 3 New Result':
        if job:
            if scenario_3_metric_bool:
                account_balance -= 325
                study_time = study_time + 10 if study_time < 90 else 100
                scenario_3_metric_bool = False
            screen.blit(scenario_3_job_buy_result, (0, 0))
        else:
            if scenario_3_metric_bool:
                credit -= 325
                study_time = study_time + 10 if study_time < 90 else 100
                scenario_3_metric_bool = False
            screen.blit(scenario_3_nojob_no_result, (0, 0))
        scenario_3_continue_result_button.draw(screen)

    elif current_state == 'Scenario 3 No Result':
        if job:
            if scenario_3_metric_bool:
                study_time -= 10
                account_balance -= 150
                scenario_3_metric_bool = False
            screen.blit(scenario_3_job_no_result, (0, 0))
        else:
            if scenario_3_metric_bool:
                study_time -= 10
                scenario_3_metric_bool = False
            screen.blit(scenario_3_nojob_no_result, (0, 0))
        scenario_3_continue_result_button.draw(screen)

    elif current_state == 'Result':

        result_continue_result_button.draw(screen)


    elif current_state == 'Final':
        screen.blit(final_background, (0, 0))

    if not current_state == 'start':
        draw_metrics(screen, study_time, account_balance, credit, credit_score)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
