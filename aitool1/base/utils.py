
from requests import post

from json import loads

url = "https://api.openai.com/v1/chat/completions"
openai_api_key = "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"
model_name = "gpt-3.5-turbo"  # Example model name

headers = {
    "Authorization": f"Bearer {openai_api_key}"
}
# Function to generate text using GPT-3
def get_info(prompt):
    data = {
         "model": model_name,
         "messages": [
        {
            "role": "system",
            "content": "Hello, how can I assist you?"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
   
    
        }
    response = post(url=url, json=data, headers=headers)
    #create a python dictionary from json
    information = loads(response.text)
    #extract the content from dictionary
    data = information['choices'][0]['message']['content']
    return data
# Functions to generate content and questions based on the selected education level
def generate_content(topic, education_level):
    if education_level == "Elementary School":
        prompt = f"Generate a passage on the topic of {topic} suitable for elementary school students. Include simple explanations and key points."
        context = get_info(prompt)
        return context
    elif education_level == "High School":
        prompt = f"Create a more detailed passage on {topic} for high school students, covering advanced concepts and processes."
        context = get_info(prompt)
        return context
    elif education_level == "College":
        prompt = f"Craft an in-depth analysis of {topic} for college-level students, delving into the biochemical reactions and significance."
        context = get_info(prompt)
        return context
    else:
        context ="make sure you enter a valid education level[Elementary School,High School,College]"
        return context
    

def generate_questions(topic,context,education_level):
    if education_level == "Elementary School":
        prompt = f"Randomly provide multiple-choice question related to {topic} from the following context{context} at an elementary level."
        question = get_info(prompt)
        return question
    elif education_level == "High School":
        prompt = f"Provide  short answer question that challenge high school students' understanding of {topic} from the following context{context}."
        question = get_info(prompt)
        return question
    elif education_level == "College":
        prompt = f" Develop an essay question that require critical thinking and application of knowledge at a higher academic level from the following context{context}."
        question = get_info(prompt)
        return question
    else:
        question ="not now!"
        return question
   
#Function to generate the answer
def generate_answer(question):
    prompt=f"Answer this {question}",
    corr_answer = get_info(prompt)
    return corr_answer
# Function to evaluate the user's answer
def evaluate_answer(answer,question):
    prompt=f"Is this answer {answer} correct or incorrect?for the following question{question} Please provide feedback on the accuracy of the answer",
    rating = get_info(prompt)
    return rating
