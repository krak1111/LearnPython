import ephem

planet_list = [name for _0, _1, name in ephem._libastro.builtin_planets()]

def greet_user(bot, update):
    """
    Function for start chat
    """
    answer_text = 'Greetings Me Friend'
    update.message.reply_text(answer_text)
    

def planet_constellation(bot, update):
    """
    Handling a command '/planet <planet_name>' or '/planet'
    if '/planet' return details for input
    else return constellation of the planet or error
    """
    update_list = update.message.text.split()
    
    try:
        planet = update_list[1].capitalize() # planet name

        if planet in planet_list: #if name exist in ephem base
            planet_class = getattr(ephem, planet)() #create class ex like ephem.Mars()
            planet_class.compute() #magic
            # answer preparing
            answer_text = f'Planet: {planet}\nConstellation: {ephem.constellation(planet_class)}'
            
            update.message.reply_text(answer_text)
        
        else:
            update.message.reply_text(f'Nonexistent planet "{planet}!\n"Retry please!')

    except IndexError:
        update.message.reply_text("\n".join(['Please Enter an planet or planetmoon or star (except Earth).',
                                            '/planet <Plannet_name>', 
                                            '/planetlist for list of planets']))


def list_planet(bot, update):
    update.message.reply_text(', '.join(planet_list))

    
def talk_to_me(bot, update):
    """
    Function for text processing
    """
    user_text = update.message.text

    if user_text == 'fool':
        answer_text = 'I am not a fool!!!'
    else:
        answer_text = f'You tell me "{user_text}"'

    update.message.reply_text(answer_text)