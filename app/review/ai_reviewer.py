import os
import json
import time  # <--- FIX: This was missing!
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ai_review(code: str, language: str) -> dict:
    try:
        start_time = time.time()
        
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are a senior {language} architect. Respond ONLY with valid JSON. "
                        "Do not use triple backticks or triple quotes inside JSON values. "
                        "Escape all newlines with \\n."
                    )
                },
                {
                    "role": "user",
                    "content": f"Review this code and return a JSON object with keys: "
                               f"score, security_risk, complexity (with time and space keys), "
                               f"explanation, points (list), improved_code, unit_tests, chat_intro. \n\n"
                               f"CODE:\n{code}"
                }
            ],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"},
            temperature=0.1 
        )

        duration = time.time() - start_time
        raw_content = response.choices[0].message.content
        ai_data = json.loads(raw_content)
        
        # Calculate speed metrics
        total_tokens = response.usage.total_tokens
        tps = round(total_tokens / duration, 1) if duration > 0 else 0

        # Safely extract complexity
        comp = ai_data.get("complexity", {})
        # Handle cases where complexity might be a string or a dict
        if isinstance(comp, dict):
            comp_str = f"Time: {comp.get('time', 'N/A')} | Space: {comp.get('space', 'N/A')}"
        else:
            comp_str = str(comp)

        return {
            "score": ai_data.get("score", "N/A"),
            "security_risk": ai_data.get("security_risk", "Low"),
            "complexity": comp_str,
            "explanation": ai_data.get("explanation", "N/A"),
            "points": ai_data.get("points", []),
            "improved_code": ai_data.get("improved_code", ""),
            "unit_tests": ai_data.get("unit_tests", ""),
            "chat_intro": ai_data.get("chat_intro", "I've analyzed your code. How can I help?"),
            "speed": f"{tps} t/s"
        }

    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        return {
            "score": "Error",
            "complexity": "N/A",
            "security_risk": "N/A",
            "explanation": f"System Error: {str(e)}",
            "points": ["Make sure 'import time' is at the top of ai_reviewer.py", "Check your Groq API quota"],
            "improved_code": "",
            "unit_tests": "",
            "speed": "N/A"
        }