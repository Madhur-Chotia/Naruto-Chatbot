import chatbot_model

def ask_ques():
    input_string=input("Your query: ")
    response = chatbot_model.get_most_similar_question(input_string)
    print(response)
    return ask_ques()
ask_ques()