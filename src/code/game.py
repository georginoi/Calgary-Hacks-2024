import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Define constants
font = pygame.font.SysFont('monospace', 36)
scenario_font = pygame.font.SysFont('monospace', 16)  # Smaller font for scenario options

# Define game states
MAIN_MENU = 0
SCENARIO_1 = 1 # Dorm Scenario
SCENARIO_2 = 2 # Rent Scenario
SCENARIO_3 = 3 # At home Scenario

# Game metrics
class Student:
    def __init__(self):
        super().__init__()

        self.current_study_time = 0
        self.max_study_time = 45
        self.study_bar_length = 1000
        self.study_time_ratio = self.max_study_time / self.study_bar_length

        self.current_account_balance = 0
        self.min_account_balance = 0
        self.max_account_balance = 10000
        self.account_balance_bar_length = 1000
        self.account_balance_ratio = self.max_account_balance / self.account_balance_bar_length

        self.current_credit_allowance = 900
        self.max_credit_allowance = 900
        self.min_credit_allowance = 0
        self.credit_allowance_bar_length = 1000
        self.credit_allowance_ratio = self.max_credit_allowance / self.credit_allowance_bar_length

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        self.current_credit_score = 640
        self.min_credit_score = 300
        self.max_credit_score = 900
        self.credit_score_bar_length = 1000
        self.credit_score_ratio = self.max_credit_score / self.max_credit_score_bar_length


    def update(self):
        self.study_time()
        self.account_balance()
        self.credit_allowance()
        self.credit_score()

    def get_account_balance(self,amount):
        if self.current_account_balance - amount >= 0:
            self.current_account_balance -=amount
        if self.current_account_balance <=0:
            self.game_over_message()
            

    def get_account_balance(self,amount):
        if self.current_account_balance - amount >= 0:
            self.current_account_balance -=amount
        if self.current_account_balance <=0:
            self.current_account_balance = 0
        
    def study_time(self):
        pygame.draw.rect(screen,'Black',(0,0,self.current_study_time/self.study_time_ratio,20))
        pygame.draw.rect(screen,'Black',(0,0,self.study_bar_length,20),4)

    def account_balance(self):
        pygame.draw.rect(screen,'Black',(25,0,self.current_account_balance/self.account_balance_ratio,20))
        pygame.draw.rect(screen,'Black',(25,0,self.account_balance_bar_length,20),4)

    def credit_allowance(self):
        pygame.draw.rect(screen,'Black',(0,1025,self.current_credit_allowance/self.credit_allowance_ratio,20))
        pygame.draw.rect(screen,'Black',(0,1025,self.credit_allowance_bar_length,20),4)

    def credit_score(self):
        pygame.draw.rect(screen,'Black',(25,1025,self.current_credit_allowance/self.credit_allowance_ratio,20))
        pygame.draw.rect(screen,'Black',(25,1025,self.credit_allowance_bar_length,20),4)  

    def game_over_message(message):
        game_over_text = font.render('Game Over', False, 'Black', 'White')
        game_over_text_rect = game_over_text.get_rect(center=(width_center,height_center))



# Set the screen size
screen_width = 900
screen_height = 720
width_center = (screen_width // 2)
height_center = (screen_height // 2)
screen = pygame.display.set_mode((screen_width,screen_height))

# Set display caption
pygame.display.set_caption('Scenario game')

# Load the background image
try:
    background_surface = pygame.image.load('../files/textured_wall.jpg')
except pygame.error:
    print(f"Could not load background image at {'../files/textured_wall.jpg'}")
    sys.exit(1)

# Main menu button setup
main_menu_button_text = font.render('Start', False, 'Black', 'White')
main_menu_button_rect = main_menu_button_text.get_rect(center=(width_center,height_center-100))

# Load the menu description image
try:
    main_menu_description = pygame.image.load('../files/menu_description.png')
except pygame.error:
    print(f"Could not load background image at {'../files/menu_description.png'}")
    sys.exit(1)
# Main menu description rectangle for easy positioning
main_menu_description_rect = main_menu_description.get_rect(center=(width_center,height_center+60))

# Set the clock for fps 
clock = pygame.time.Clock()




# Dorm scenario branch 
scenario_1_options = {
    'A': {
        'text': 'Save the Refund, Decline the Job, Don\'t Apply for Credit Card',
        'impact': {
            'account_balance': 2000,
            'credit_allowance': 0,
            'credit_score': 0  # No change
        }
    },
    'B': {
        'text': 'Invest in Educational Resources, Accept the Job, Apply for Credit Card',
        'impact': {
            'study_time': 5,
            'account_balance': 500,  # Assumes the refund is spent, but starts earning $500 monthly
            'credit_allowance': 500,
            'credit_score': 20  # Increase by 20 points
        }
    },
    'C': {
        'text': 'Use Refund for Living Expenses, Decline the Job, Apply for Credit Card for Emergencies',
        'impact': {
            'account_balance': -2000,  # Assumes the refund will be spent over time
            'credit_allowance': 300,
            'credit_score': 10  # Increase by 10 points
        }
    },
    'D': {
        'text': 'Partially Save Refund, Accept Job for Savings, Decline Credit Card',
        'impact': {
            'study_time': -2,
            'account_balance': 1500,  # $1000 saved + $500 from the job
            'credit_allowance': 0,
            'credit_score': 0  # No change
        }
    }
}

# Game state
game_state = MAIN_MENU


# Main game loop
game_active = True
while game_active:

    screen.blit(background_surface,(0,0))  # Show the background image on the screen position 0,0

    if game_state == MAIN_MENU:
        screen.blit(main_menu_button_text,main_menu_button_rect)  # Show the main menu button
        screen.blit(main_menu_description,main_menu_description_rect) # Show the description of the game





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit pygame and window
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    
    
   
        




    # Update the display
    pygame.display.flip()
    # Set max fps to 60
    clock.tick(60)

#     if game_state == MAIN_MENU:
#         pygame.draw.rect(screen, GREEN, main_menu_button_rect)  # Background for button
#         screen.blit(main_menu_button_text, main_menu_button_rect)
#     elif game_state == SCENARIO_1:
#         draw_scenario(screen, scenario_1_options, SCENARIO_FONT)

#     if game_state != MAIN_MENU:
#         draw_metrics(screen, metrics, FONT, 10, 10)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == MAIN_MENU and main_menu_button_rect.collidepoint(mouse_pos):
#                 game_state = SCENARIO_1
#             elif game_state == SCENARIO_1:
#                 y_offset = 150
#                 for option_id, option_info in scenario_1_options.items():
#                     text_surface = SCENARIO_FONT.render(f"{option_id}: {option_info['text']}", True, WHITE)
#                     text_rect = text_surface.get_rect(topleft=(50, y_offset))
#                     bg_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10)

#                     if bg_rect.collidepoint(mouse_pos):
#                         for key, impact in option_info['impact'].items():
#                             metrics[key] += impact
#                         print(f"Selected option: {option_id}")
#                         # Here, handle the transition to the next game state or repeat SCENARIO_1 for simplicity
#                     y_offset += text_rect.height + 20
pygame.quit()