import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import utilities
import warnings
warnings.filterwarnings("ignore")


url = 'https://narutoexplained.com/20-answers-to-the-most-frequently-asked-questions-about-naruto/'
webpage_text = utilities.extract_text_from_webpage(url)

if webpage_text:
    print("Chatbot loading, reading concepts.")

import re

# Defining the start and end patterns to filter webpage_text
start_pattern = r'When is Naruto’s Birthday \?20 Answers to the Most Frequently Asked Questions About NarutoNaruto’s Birthday is on October 10th\.'
end_pattern = r'They don’t simply come and go away\.This character improvement, ties the watchers with the story\.'

# filtering using regular expression
match = re.search(f'{start_pattern}(.*?){end_pattern}', webpage_text, re.DOTALL)

# Checking if a match is found
if match:
    extracted_text = match.group(1).strip()
    print("Text extracted")
else:
    print("No match found.")

paragraphs = re.split(r'\?\s*', extracted_text)
paragraphs = [s.strip() + '?' if i < len(paragraphs) - 1 else s.strip() for i, s in enumerate(paragraphs)]


sub_para = paragraphs[1:-1]

result_list = utilities.split_strings_at_last_period(sub_para)

#adding 1st question string and last answer string into the list
qa_list=[paragraphs[0]]+result_list+[paragraphs[-1]]
print("List of QnA extracted")
#creating qs-ans pairs
qa_pairs = [(qa_list[i], qa_list[i + 1]) for i in range(0, len(qa_list), 2)]
qa_pairs

#creating dataframe out of pairs
df=pd.DataFrame(qa_pairs, columns=['qs','ans'],index=None)
df

#creating a greetings dataframe
greetings_df = pd.DataFrame({
    'qs': [
        "Hi, how are you?",
        "Hello, what's up?",
        "Hey, how's it going?",
        "Good to see you, how have you been?",
        "Hi there, how can I help you today?",
        "Good Morning.",
        "Good Afternoon",
        "Good Evening."
    ],
    'ans': [
        "I'm doing well, Arigato!",
        "Not much, just here to assist you on anything you ask me on Naruto.",
        "Naruto being Hokage of our village, everything is going its best, thanks for asking!",
        "I've been well, how about you?",
        "I'm here to help. Do you want to know anything about Naruto?",
        "Ohayogozaimasu! How can I help you today?",
        "Konichiwa! Welcome to Leaf Village.",
        "Hello, how are you?"
    ]
})

#creating an ending chat dataframe
ending_chat_df = pd.DataFrame({
    'qs': [
        "It was nice chatting with you. Goodbye!",
        "I have to go now. Goodbye!",
        "If you have any more questions, feel free to ask. Goodbye!",
        "Thanks for the conversation. Take care!",
        "I'll be signing off now. Goodbye!",
        "Good Night."
    ],
    'ans': [
        "Sayonara! Feel free to return anytime. You are always welcome in our Hidden Leaf Village",
        "Sayonara! If you need assistance later, don't hesitate to ask. I can help you to get you in touch with Naruto-sama even",
        "Sure, feel free to reach Konohagakure again. Sayonara!",
        "You too! Take care and have a great day! Kanpai!",
        "Alright, Sayonara! If there's anything else, let me know.",
        "Oyasumi! Do you need anything else, just let me know."
    ]
})

df=pd.concat([df, greetings_df, ending_chat_df], ignore_index=True)
print("Adding greetings and chat ending prompts to context.")



# Loading a pre-trained BERT model for sentence embeddings
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# Encoding questions to obtain BERT embeddings
question_embeddings = model.encode(df['qs'].values.tolist())

# Function to get the most similar question from the dataset
def get_most_similar_question(user_input):
    user_input_embedding = model.encode([user_input])
    similarities = cosine_similarity(user_input_embedding, question_embeddings)[0]
    if max(similarities)<0.5:
        return "Hey, there is some language problem, I couldn't understand, I am still in learning phase. I'll ask Lord Seventh to help me understand more about this."
    else:
        most_similar_index = similarities.argmax()
        return df['ans'].iloc[most_similar_index]
    
print("Model Loaded. You can begin now."+"\n")
