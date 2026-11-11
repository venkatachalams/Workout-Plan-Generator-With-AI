Application Description 
------------------------
This is a single-page Streamlit app that takes structured inputs about a user's fitness goals ,Experience level ,Days available per week and Equipment access as Dropdown Input and a Free text field to express any other requirements or restrictions. With the provided Input it generates a personalized workout plan using an LLM via the Groq API. 

Instructions to run the APP
---------------------------
Navigate to 'src/workout_plan_generator_with_ai' and run the following uv command 
uv Command : uv run streamlit run main.py

Other Requirement 
-----------------
Create .env file at the root 
generate groq api key and copy past the apikey  value against GROQ_API_KEY 
and for GROQ_MODEL you can specify openai/gpt-oss-20b in .env file or anyother valid model name for Groq


Result : Application will provide teh detail workout plan for the provided input , 
In case of any error it will handle those error show you highlevel message regarding the error along with status code.

Tech Stock 
----------
This app uses streamlit API for UI.
It uses Groq  as LLM to generate Workout plan
It uses uv for package management.

