import random
import bot

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return 'Hey There!'
    
    if p_message == "!roll captains":
        return "Success"
    
    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    
    if p_message == '!randompug':
        return "This is a random pug"