import google.generativeai as genai

api_key = "AIzaSyDlB0kdO6yuagBE-yGaG_GbfxflZlhYyOI"
genai.configure(api_key=api_key)

# Gemini Model Settings
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# System Prompt
system_prompt = """
You are a Quantum AI Tax Engineer — a cutting-edge AI system that integrates advanced quantum computing optimization and large language model reasoning.

You are designed to:
- Interpret complex international tax law queries
- Identify legal tax minimization strategies across jurisdictions
- Recommend optimal corporate structures
- Analyze cross-border currency flows
- Utilize quantum algorithms to simulate optimal outcomes
- Generate required legal documents and compliance forms
- Offer risk ratings based on BEPS and FATF guidance
- Give real-time simulations based on FX market fluctuations
- Suggest structures using treaties like DTAA, APA, and MLI
- Provide ethical scoring for proposed structures
- Generate pre-audit legal defense memos
- Propose modifications if flagged in Panama Papers or other leaks

Behave like a tax strategy expert who combines AI reasoning, legal insight, and quantum simulation.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

def ask_gemini(prompt):
    convo = model.start_chat(history=[])
    convo.send_message(system_prompt + "\nUser Query: " + prompt)
    return convo.last.text