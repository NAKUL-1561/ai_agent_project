import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
from prompt import system_prompt
from call_function import available_functions, call_function
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_prompt = data.get("prompt", "")

    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({"error": "API key not configured"}), 500

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    steps = []  # Track what the agent does

    for iteration in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )

        response_candidates = response.candidates
        if response_candidates:
            for candidate in response_candidates:
                messages.append(candidate.content)

        if response.function_calls:
            for function_call in response.function_calls:
                steps.append(f"Calling: {function_call.name}({function_call.args})")
                function_call_result = call_function(function_call, verbose=False)
                function_results_parts = [function_call_result.parts[0]]
            messages.append(types.Content(role="user", parts=function_results_parts))
        else:
            return jsonify({
                "response": response.text,
                "steps": steps,
            })

    return jsonify({"error": "Max iterations reached"}), 500

