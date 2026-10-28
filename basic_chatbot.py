# Chatbot ka main function jisme reply ke rules define hain
def get_bot_response(user_input):
    # User ke text ko small letters me convert karte hain taaki case mismatch na ho
    text = user_input.lower().strip()

    # if-elif conditions se check karte hain user ne kya bola hai
    if "hello" in text or "hi" in text:
        return "Hi there! How can I help you today?"
    elif "how are you" in text:
        return "I'm fine, thanks! How are you doing?"
    elif "your name" in text:
        return "I'm a simple rule-based Python Chatbot."
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! Have a great day ahead!"
    else:
        # Agar bot ke paas jawab na ho
        return "I'm sorry, I don't understand that. You can say 'hello', 'how are you', or 'bye'."

# Chatbot ko lagatar chalane ke liye main loop function
def start_chat():
    print("=" * 45)
    print("🤖 Welcome to the Rule-Based Chatbot!")
    print("Type 'bye' anytime to exit the chat.")
    print("=" * 45)     

    # while loop tab tak chalega jab tak user 'bye' na likh de
    while True:
        # User se input lete hain
        user_message = input("\nYou: ")
 
        # Bot ka response nikaalte hain
        bot_reply = get_bot_response(user_message)
        print(f"Bot: {bot_reply}")

        # Agar user 'bye' bolta hai toh chat yahin end ho jayegi
        if "bye" in user_message.lower():
            break

# Program ko run karne ke liye
if __name__ == "__main__":
    start_chat()