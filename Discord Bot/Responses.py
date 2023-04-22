import random
def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'hey there'
    return "error"