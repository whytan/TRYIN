import streamlit as st
import re
# Function to check if the input is a coding-related question
def is_coding_question(input_text):
   coding_keywords = ['code', 'coding', 'programming', 'algorithm', 'data structure']
   return any(keyword in input_text.lower() for keyword in coding_keywords)
# Chatbot function
def chatbot(input_text, previous_responses):
   if is_coding_question(input_text):
       response = "Sure, I can help you with coding questions! What specific problem are you facing?"
   else:
       # If not a coding question, use the GPT-2 model
       response, _ = gpt2_chatbot(input_text, previous_responses)
   # Save the response to the list of previous responses
   previous_responses.append(response)
   return response, previous_responses
# GPT-2 Chatbot function (similar to the previous example)
def gpt2_chatbot(input_text, previous_responses):
   # Tokenize input text
   input_ids = tokenizer.encode(input_text, return_tensors='pt')
   # Generate response
   with torch.no_grad():
       output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
   # Decode and return the response
   response = tokenizer.decode(output[0], skip_special_tokens=True)
   # Save the response to the list of previous responses
   previous_responses.append(response)
   return response, previous_responses
# Streamlit app
def main():
   st.title("Chatbot with Streamlit")
   # Initialize the list of previous responses
   previous_responses = []
   # User input textbox
   user_input = st.text_input("You:", "")
   # Chatbot response
   if st.button("Send"):
       response, previous_responses = chatbot(user_input, previous_responses)
       # Display previous responses
       st.text_area("Chat History:", "\n".join(previous_responses))
       
       # Display the latest response
       st.text_area("Chatbot:", response)
if __name__ == "__main__":
   main()