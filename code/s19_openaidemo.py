from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.responses.create(model="gpt-5-nano", input="Write a one-sentence bedtime story about a unicorn.")

print(response.output_text)

# write a shorter story online 30 lines and make it more interactive with the user, asking them questions about the story and responding to their answers.
def interactive_story():
    print("Welcome to the Interactive Unicorn Story! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        story = interative_story(user_input)
        print(f"Chatbot: {story}")
        follow_up = input("What do you think happens next? ")
        follow_up_response = interactive_story(f"{story} {follow_up}")
        print(f"Chatbot: {follow_up_response}")
if __name__ == "__main__":
    interactive_story()
