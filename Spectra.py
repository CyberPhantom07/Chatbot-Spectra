import random
import re

def chatbot():
    print("Bonjour! Je suis un chatbot nommée Spectra. Comment puis-je vous aider aujourd'hui?")

    while True:
        user_input = input("Vous: ")

        if user_input.lower() == 'exit':
            print("Au revoir! À bientôt.")
            break
        else:
            response = generate_response(user_input)
            print(f"Chatbot: {response}")

def generate_response(user_input):
    greetings = ["Bonjour!", "Salut!", "Coucou!"]
    farewells = ["Au revoir!", "À bientôt!", "À la prochaine!"]

    # Utilisation d'expressions régulières pour détecter différentes orthographes
    if re.search(r"comment ça va\??", user_input, re.IGNORECASE):
        return "Ça va bien, merci! Et vous?"
    elif re.search(r"quel est ton nom\??", user_input, re.IGNORECASE):
        return "Je suis un chatbot nommée Spectra."
    elif re.search(r"ça va merci", user_input, re.IGNORECASE):
        return "De rien! Si vous avez d'autres questions, n'hésitez pas."
    elif re.search(r"qui est ton créateur\??", user_input, re.IGNORECASE):
        return "Mon créateur se surnomme Raphaël."
    elif re.search(r"exit", user_input, re.IGNORECASE):
        return random.choice(farewells)
    else:
        return "Désolé, je ne comprends pas bien. Pouvez-vous reformuler votre question ?"

# Lancer le chatbot
chatbot()
