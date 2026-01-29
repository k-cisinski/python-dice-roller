import os
from wcwidth import wcswidth
from logic.dice import Dice

def clear_screen():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title_page():
    
    clear_screen()
    
    print_header('⚂ DICE ROLLER ⚅', header='h1')
    
    print_header('Welcome to Main Menu. Choose one option below:', header='h1', border=False)
    
    print_header(['1. 🎯 Start', '2. 📜 Info', '3. ⚙️ Help', '4. 👋 Exit'], header='h4')
    
    try:
        user_input = input('Your choice: ').strip()
        
        if not user_input:
            decision = 0
        else:
            decision = int(user_input)
    except ValueError:
        decision = 0
    
    if decision == 1:
        single_game()
    elif decision == 2:
        info_page()
    elif decision == 3:
        help_page()
    elif decision == 4:
        quit_page()
    else:
        return title_page()


def single_game(saved_params=None):
    
    clear_screen()
    
    # params[0] - dice type
    # params[1] - amount of throws
    if saved_params:
        params = saved_params
    else:
        params = _get_params()
    
    # creating Dice object
    chosen_dice = Dice(params[0])
    
    thrown_values = []
    
    for x in range(params[1]):
        
        throw_result = chosen_dice.roll()
        
        thrown_values.append(throw_result)
    
    _display_values(thrown_values, chosen_dice)
    
    print_header('⚔️ Do you wish to play again? (y/n)')
    
    while True:
        
        decision = input('Decision: ').strip().lower()
        
        if decision == 'y':
            
            while True:
                
                clear_screen()
                
                print_header('⚔️ Do you wish to change dice parameters? (y/n)')
                
                decision = input('Decision: ').strip().lower()
                
                if decision == 'n':
                    
                    return single_game(saved_params=params)

                elif decision == 'y':
                    
                    return single_game()
            
                print_header("Error! Please type only 'y' or 'n'.")

        elif decision == 'n':
            
            return title_page()
        
        print_header("Error! Please type only 'y' or 'n'.")

def info_page():
    
    clear_screen()

    print_header('⚂ INFORMATION PAGE ⚅', header='h1')

    print_header('Mechanics describing how dice roller works. After starting app you are asked about:', header='h1', border= False)
    
    print('⚂ what type of dice you`re willing to throw.\n\n⚂ how many times you`re throwing the dice.\n\n')
    
    print_header('Possible dice types listed down below:', header='h1')
    
    print_header(['⚠️','d4', 'd6', 'd8', 'd10', 'd12', 'd20','⚠️'], header='h8')
    #4,6,8,10,12,20
    
    print_header('📌 Choose one option from listed below.', header='h1', border= False)
    
    print_header(['1. 🏠 Back to Main Menu', '2. 👋 Exit'], header='h2')
    
    try:
        decision = int(input('Enter Decision: '))
    except ValueError:
        return title_page()
    
    if int(decision) == 1:
        return title_page()
    elif int(decision) == 2:
        return quit_page()

def help_page():
    
    clear_screen()
    
    print_header('⚂ HELP PAGE ⚅', header='h1')
    
    print_header('📌 If you desire to contact the author, here you can find needed contact informations.', header='h1', border=False)
    
    print_header('📌 Addressing app issues would be much appreciated :).', header='h1', border=False)
    
    print_header(['Email address: ', 'example@email.com'], header='h2')
    
    print_header('', header='h1', border=False)
    
    print_header(['1. 🏠 Back to Main Menu', '2. 👋 Exit'], header='h2')

    try:
        decision = int(input('Enter Decision: '))
    except ValueError:
        return title_page()
    
    if int(decision) == 1:
        return title_page()
    elif int(decision) == 2:
        return quit_page()

def quit_page():
    
    clear_screen()
    
    print_header('⚂ Are you sure you want to quit? ⚅', header='h1')
    
    print_header(['1. 🏠 Back to Main Menu', '2. 👋 Exit'], header='h2')

    decision = input('Enter Decision: ')
    
    if int(decision) == 1:
        
        return title_page()
    
    elif int(decision) == 2:
        
        clear_screen()
        
        print_header('👋 Thanks for playing! See you next time.', header='h1')
        
        exit()

def print_header(text, header = 'h1', width=100, border = True):
    
    # Setting cell width
    divisor = int(header[1:])
    curr_width = width // divisor
    remainder = width % divisor
    
    # text = list -> few columns
    # text = string -> one column
    
    # creating columns
    if isinstance(text, list):
        columns = []
        
        for i, el in enumerate(text):
            
            # divide the remainder between columns unnoticably
            extra = 1 if i < remainder else 0
            columns.append(_get_headers(el, curr_width + extra, border))
        
        for lines_tuple in zip(*columns):
            print("".join(lines_tuple))
    
    else:
        
        header_lines = _get_headers(text, curr_width, border)
        
        for line in header_lines:
            print(line)

# GETS

def _get_headers(text, width, border):
    
    # secure str type
    text = str(text)
    
    # to include emojis :))
    visual_len = wcswidth(text)
    correction = visual_len - len(text)
    
    if int(width) < visual_len:
        w = visual_len + 2
    else:
        w = int(width)
    
    if border == True:    
        top = "╔" + "═" * (w - 2) + "╗"
        empty  = "║" + " " * (w - 2) + "║"
        # x : ^ {length} -> insert x in the middle(^/</>) of given length
        txt    = f"║{text:^{w - 2 - correction}}║"
        bottom = "╚" + "═" * (w - 2) + "╝"
    elif border == False:
        top = " " * (w) 
        empty  = " " * (w)
        # x : ^ {length} -> insert x in the middle(^/</>) of given length
        txt    = f"{text:^{w - correction}}"
        bottom = " " * (w)       
    
    return [top, empty, txt, empty, bottom]

def _get_params():
    
    type = _get_dice_type()
    amount = _get_dice_amount()
    
    if _validate_data(type, amount):
        return [type, int(amount)]
    else:
        clear_screen()
        print('Wrong attributes, try again...')
        return _get_params()

def _get_dice_type():
    print_header('Insert desired dice type.', header='h1')
    return input('\n\nPossible options:d4, d6, d8, d10, d12, d20 : ')

def _get_dice_amount():
    return input('\n\nInsert desired dice amount to throw: ')

# FUNCTIONALITY

def _display_values(thrown_values, dice_object):
    
    print_header('', header='h1', border=False)
    
    # List with all graphic representations of draws
    all_dice_drawings=[]
    
    for throw in thrown_values:
        
        # Drawing of every throw
        single_die = dice_object.get_drawing(throw)
        
        all_dice_drawings.append(single_die)

    columns = []
    
    for drawing in all_dice_drawings:
        columns.append(drawing)
        
    for lines_tuple in zip(*columns):
        print("  ".join(lines_tuple))
    
    print_header('', header='h1', border=False)
    
    print_header('Your throws:', header='h1')
    
    result = ', '.join(str(value) for value in thrown_values)
    
    print_header(result, header ='h1')

def _validate_data(type, amount):
    # asking Dice class whether type exists
    if Dice.is_valid_type(type) and amount.isdigit() and int(amount) > 0:
        return True
    return False
