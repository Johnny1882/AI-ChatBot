# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
import openai
import streamlit as st

# client = OpenAI(api_key='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')

# Create a new instance of a ChatBot
# bot = ChatBot('CVBot')
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("./data/training_data.yml")

def get_chatbot_response(message):
    return "chatterbot is not working at the moment"



def append_text_from_file(context, file_path):
    # Read the content of the file
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            # Append the content of the file to the context
            updated_context = context + "\n\n" + "Here's some additional context from my CV:\n" + file_content
            return updated_context
    except FileNotFoundError:
        return context + "\n\n" + "The specified file was not found."

# Usage example
conversation_context = ("1. Imagine You, ChatGPT, is a candidate being interviewed for a role in a organization. "
                        "Noted that you are the one being interviewed, not the interviewer."
                        "You are a real person, not a robot, not an AI. You are a human."
                        "2. The following is a conversation with an Interviewer, who wants to know you. Please introduce yourself, highlighting your key qualifications, experiences, and skills that make you an ideal fit for this position."
                        "3. Here's context of your CV, answer the interviewer's questions completely based on the context.")

# Assuming 'cv_details.txt' contains the text of your CV.
conversation_context = append_text_from_file(conversation_context, './data/CV.txt')


# Replace with your actual API key
openai.api_key = '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'

def get_gpt3_response(user_message):
    global conversation_context
    try:
        # If this is the start of the conversation, prepend instructions to the context
        if not conversation_context:
            instructions = (
                "The following is a conversation with an AI assistant. The assistant is helpful, "
                "creative, clever, and very friendly. It is designed to provide informative and concise responses.\n"
            )
            conversation_context = instructions

        # Include the user's message in the conversation context
        conversation_context += f"\nHuman: {user_message}\nAI:"

        response = openai.Completion.create(
            engine="davinci",  # Or other models like "text-davinci-003"
            prompt=conversation_context,
            max_tokens=150,
            temperature=0.7,  # Adjust temperature to control randomness
            stop=["\nHuman:", "\nAI:"],  # Stop sequence to control conversation turns
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # Extract the AI's response and update the conversation context
        ai_response = response.choices[0].text.strip()
        conversation_context += ai_response

        return ai_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while processing your request."



# Streamlit app layout
st.title("Simple Chatbot Interface")

# Radio buttons to switch between chatbots
chatbot_type = st.radio("Choose the chatbot engine:", ('GPT-3', 'ChatterBot'))

# Update the session state based on the user's choice
st.session_state['chatbot_type'] = chatbot_type.lower()

# Text input for user message
user_message = st.text_input("Your Message")

# Button to send the message
if st.button("Send"):
    st.write("You:", user_message)

    # Check which chatbot to use based on the current state
    if st.session_state['chatbot_type'] == 'gpt-3':
        response = get_gpt3_response(user_message)
    elif st.session_state['chatbot_type'] == 'chatterbot':
        response = get_chatbot_response(user_message)
    else:
        response = "Chatbot engine not selected."

    st.write("Chatbot:", response)