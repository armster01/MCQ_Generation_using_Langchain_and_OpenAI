#MCQ Generation using Langchain 🦜🔗 and OpenAI ֎

This project leverages the power of Langchain and OpenAI to automatically generate high-quality Multiple Choice Questions (MCQs). 
The solution is deployed on a Streamlit App, 
providing an easy-to-use interface for educators and content creators to quickly generate MCQs based on custom input texts or topics.

##Key Features:

1. Utilizes Langchain to structure and streamline the question generation process.
2. Employs OpenAI for generating content, ensuring diverse and high-quality MCQs.
3. Supports a variety of topics and input texts, providing flexibility for users.
4. Simple and intuitive user interface via Streamlit.

##Deployment:
1. The project runs on Streamlit, and you can start the app with the following command:
2. streamlit run Streamlit_App.py
##Please note, this application requires OpenAI API access, and charges will be incurred for token usage on the OpenAI platform during question generation.

##Prerequisites:
1. Python 3.x
2. Langchain library
3. Streamlit library
4. OpenAI API key (with sufficient credits for token generation)

##Setup Instructions:
1. Clone this repository:
   git clone https://github.com/your-repo/mcq-generation
2. Install the required packages:
   pip install -r requirements.txt
3. Set your OpenAI API key as an environment variable:
   export OPENAI_API_KEY='your-api-key'
4. Run the Streamlit app:
   streamlit run Streamlit_App.py

##Usage:
Once the Streamlit app is running, input a topic or text, and the system will generate MCQs based on your input. 
The questions generated will vary in difficulty, offering a range of choices to suit different learning levels.

##Important Note:
This project requires an OpenAI API key for token generation, which may incur costs based on usage. 
Ensure you have sufficient credits or a subscription plan on the OpenAI platform.
