# Naruto-Chatbot
Explore the chatboot centered around most favourite anime character, Naruto! 

I used BERT to train the model to understand the context and have not used any LLM models or Open AI APIs which could have made the task lot easier and more accurate, but on the other hand would deprive me off to showcase my ML skills too.

Built using the BERT model, the bot comprehends context and provides answers through semantic search based on a curated list of frequently asked questions about Naruto. It includes engaging greetings and chat-ending prompts too for a lively experience.

The source code, available in both .ipynb and .py formats, extracts information from the specified webpage mentioned below.
# https://narutoexplained.com/20-answers-to-the-most-frequently-asked-questions-about-naruto/

# How the Application works-
- all the text data has been extracted from the given webpage and using BeautifulSoup, the texts are cleaned and specific FAQ has been filtered and stored in a dataframe as Questions and Answers.
- Basic Greetings such as welcome, Hi, Good morning, afternoon, or chat ending prompts like Goodbye, Nice talking to you, etc has been appended to the dataframe.
- The BERT model, i.e "paraphrase-distilroberta-base-v1" is used to transform the text into contextual embeddings. The contextual embeddings or vectors are then created for texts in Question columns.
- Now, any input string given by user is initially transformed to vectors and after it its cosine similarity is matched with all the vectors from Question columns and similar result is then showed up where cosine similarity is max.
- However, if the cosine similarity doesn't cross a particular threshold (here in this case I used 0.5, can be changed accordingly), the bot-application will generate a hard-coded response that it doesn't understand the language and will ask Naruto or Lord Hokage to make this more clear to it. Did this bcz I know people would test chatbots giving gibberish prompts as well.

# Note to start with-
- The application is built in both .ipynb and .py format
- To start the application and experience it seamlessly, install all required libraries as mentioned in requirements.txt.
  Use this code to install all the required libraries - <pip3 install -r requirements.txt>
- To run using .py file, after installing required libraries just type <python main.py>.

Check out the repository, explore the code, and feel free to reach out with any questions or suggestions!🍥 

If you liked this work please star this repo, follow me and I'll see you in the next one, Dattebayo! 👊

#Naruto #Chatbot #BERT #BERTmodel
