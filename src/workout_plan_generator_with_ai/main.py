import streamlit as st               # Streamlit for building web apps
from workoutplanner import WorkoutPlanGenrator  # Importing the WorkoutPlanGenrator and promptBuilder classes from workoutplanner.py
from workoutplanner import promptBuilder



st.title("Workout Plan Generator with AI")  # Title of the app


workoutplan = WorkoutPlanGenrator()

with st.form("Workout Plan Generator"):  # Form for user input
    workoutplan.fitness_goal = st.selectbox("Select your fitness goal", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"],   placeholder="Choose a fitness goal")  # Dropdown for fitness goals
    workoutplan.fitness_level = st.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"],  placeholder="Choose your fitness level")  # Dropdown for fitness levels
    workoutplan.available_days = st.slider("Select your available workout days per week", 1, 7, 3)
    workoutplan.equipment_access = st.selectbox("Select your Equipment access", ["No Equipment", "Basic Equipment", "Full Gym Access"], placeholder="Choose your equipment access")  # Dropdown for equipment access
    workoutplan.specific_preferences = st.text_area("Any specific preferences or restrictions? (Optional)")

    if st.form_submit_button("Generate Workout Plan"):
        prompt = promptBuilder().build_prompt(workoutplan)
        woplan =workoutplan.generate_plan(prompt)
        st.subheader("Your Personalized Workout Plan:")
        st.write(woplan) # Display the generated workout plan in a text area



