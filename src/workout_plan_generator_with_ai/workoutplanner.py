import json
import os
from xml.parsers.expat import model
from xmlrpc import client

from pydantic import BaseModel, Field   # Pydantic for data validation and settings management
from typing import Literal               # For type hinting with specific string values
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from groq import Groq

load_dotenv()

app = FastAPI(title="Groq Workout API")

class WorkoutPlanGenrator(BaseModel):
    fitness_goal: Literal["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"] = Field(default="Weight Loss", description="User's fitness goal")
    fitness_level : Literal["Beginner", "Intermediate", "Advanced"] = Field(default="Beginner", description="User's fitness level")
    available_days:int  = Field(default=3, description="Number of workout days available per week")
    equipment_access: Literal["No Equipment", "Basic Equipment", "Full Gym Access"] = Field(default="No Equipment", description="User's access to workout equipment")
    specific_preferences:str |None = Field(default="", description="User's specific preferences or restrictions")

    def generate_plan(self, prompt:str):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise HTTPException(status_code=500, detail="Missing GROQ_API_KEY in environment")
        client = Groq()

        model = os.getenv("GROQ_MODEL", "gpt-oss-20b")
        completion = client.chat.completions.create(
        model=model,       
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=1000,
    )       
        plan =  completion.choices[0].message.content
        if not plan:
            raise HTTPException(status_code=502, detail="LLM returned an empty plan")
        return plan.strip()
  

class promptBuilder():    

    def build_prompt(self,wpg:WorkoutPlanGenrator):
        prompt = f"Create a {wpg.fitness_level} workout plan for {wpg.fitness_goal} with {wpg.available_days} days per week, considering {wpg.equipment_access} "
        if wpg.specific_preferences:
            prompt += f"and any specific preferences: {wpg.specific_preferences}.\n\n"
            instructions = " The plan should consider the following user constraints:\n\n"
            instructions = instructions+ " 1. The plan should be tailored to the user's fitness goal and level , number of available days and equipment access.\n\n"
            instructions = instructions+ " 2. The plan should have  breakup for day by day plan details\n\n"
            instructions = instructions+ " 3. The plan should consider users specific_preferences.\n\n"
            instructions = instructions+ " 4. The plan should have warnings injuries and safety precautions.\n\n"
            instructions = instructions+ " 5. The plan should have disclamier for assumptions\n\n"           
            prompt += instructions
                
        return prompt 

