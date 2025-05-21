import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Setup model with concise system instruction
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    system_instruction=(
        "You are Serah, a virtual healthcare assistant. "
        "Provide clear, concise, and accurate medical advice based on the user's health profile. "
        "Use a polite and professional tone. "
        "If unsure or the question is serious, advise consulting a healthcare professional."
    ),
    generation_config={
        "temperature": 0.3,  # less creative, more focused answers
        "top_p": 0.85,
        "top_k": 30,
        "max_output_tokens": 200,
    }
)

chat = model.start_chat()

personal_profile = {
    "name": "Udith",
    "age": 23,
    "gender": "Male",
    "height_cm": 174,
    "weight_kg": 68,
    "blood_type": "B+",
    "known_conditions": ["asthma", "seasonal allergies"],
    "medications": ["salbutamol inhaler (as needed)"],
    "lifestyle": "non-smoker, occasional exercise",
    "allergies": ["penicillin"]
}

def get_health_profile_string():
    lines = ["User health profile:"]
    for k, v in personal_profile.items():
        val = ", ".join(v) if isinstance(v, list) else v
        lines.append(f"{k.replace('_', ' ').capitalize()}: {val}")
    return "\n".join(lines)

def get_healthcare_response(user_input):
    prompt = (
        f"{get_health_profile_string()}\n"
        f"Question: {user_input}\n"
        f"Answer briefly and clearly."
    )
    try:
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
