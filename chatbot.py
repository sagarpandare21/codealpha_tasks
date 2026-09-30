# TASK 4: Basic Chatbot

def chatbot():
    print("===== BASIC CHATBOT =====")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user_input == "help":
            print("Bot: You can say hello, ask how I am, or say bye.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()