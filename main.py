import streamlit as st
import re

def is_coding_question(input_text):
   coding_keywords = ['code', 'coding', 'programming', 'algorithm', 'data structure']
   return any(keyword in input_text.lower() for keyword in coding_keywords)
# Chatbot 
def chatbot(input_text, previous_responses):
   if is_coding_question(input_text):
       response = "Sure, I can help you with coding questions! What specific problem are you facing?"
   else:
       
       response, _ = gpt2_chatbot(input_text, previous_responses)
   previous_responses.append(response)
   return response, previous_responses
def gpt2_chatbot(input_text, previous_responses):
   input_ids = tokenizer.encode(input_text, return_tensors='pt')
   with torch.no_grad():
       output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
   response = tokenizer.decode(output[0], skip_special_tokens=True)
   previous_responses.append(response)
   return response, previous_responses
def main():
   st.title("Chatbot with Streamlit")
   previous_responses = []
   user_input = st.text_input("You:", "")
   if st.button("Send"):
       response, previous_responses = chatbot(user_input, previous_responses)
       st.text_area("Chat History:", "\n".join(previous_responses))
       st.text_area("Chatbot:", response)
if __name__ == "__main__":
   main()
