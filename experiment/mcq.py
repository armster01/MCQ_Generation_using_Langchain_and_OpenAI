import os
import json
import pandas as pd
import traceback


!pip install langchain-community
!pip install --upgrade langchain
!pip show langchain-community


from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
KEY=os.getenv("OPENAI_API_KEY")
print(KEY)


llm=ChatOpenAI(openai_api_key=KEY,model_name="gpt-3.5-turbo",temperature=0.5)
llm


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
import PyPDF2


RESPONSE_JSON = {
    "1":{
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
    "correct": "correct answer",
    },
    "2":{
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
    "correct": "correct answer",
    },
    "3":{
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
    "correct": "correct answer",
    },
}


TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice question for {subject} student in {tone} tone.
Make sure the question are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {numberrr} MCQs
### RESPONSE_JSON
{response_json}

"""


quiz_generation_prompt = PromptTemplate(
    import_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)


quiz_chain=LLMChain(llm=llm,prompt=quiz_generation_prompt, output_key="quiz",verbose=True)


TEMPLATE2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complex analysis of the quiz. Only use at max 50 words for complexity
if the quiz is not at per with the cognitive and analytical abilities of the students, \
update the quiz question which needs to be changes and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""


quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE)


review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True,)


file_path=r"C:\Users\armst\mcqgen\experiment\data.txt"


with open(file_path, 'r') as file:
    TEXT = file.read()


print(TEXT)
#serialize the python dictionary into a JSON-formatted string
json.dumps(RESPONSE_JSON)


NUMBER = 5
SUBJECT = "machine learning"
TONE = "simple"


#how to setup token usage tracking in Langchain
with get_openai_callback() as cb:
    response=generate_evaluate_chain(
    {
        "text": TEXT,
        "number": NUMBER,
        "subject": SUBJECT,
        "tone": TONE,
        "response_json": json.dumps(RESPONSE_JSON)
    }
    )


print(f"Total Tokens:{cb.total_tokens}")
print(f"Prompt Tokens:{cb.prompt_tokens}")
print(f"Completion Tokens:{cb.completion_tokens}")
print(f"Total cost:{cb.total_cost}")


response
quiz = response.get("quiz")
quiz = json.loads(quiz)


quiz_table_data = []
for key, value in quiz.items():
    mcq = value["mcq"]
    options = " | ".json(
        [
            f"{option}: {option_value}"
            for option, option_value in value["options"].items() 
            ]
        )
    correct = value["correct"]
    quiz_table_data.append({"MCQ": mcq, "Choices: options, "Correct": correct})


quiz_table_data
quiz = pd.DataFrame(quiz_table_data)
quiz.to_csv("machine_learning.csv",index=False)
