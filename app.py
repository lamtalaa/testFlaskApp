import openai
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_openai():
    user_input = request.form['user_input']
    
    try:
        # Use the correct method for chat models
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )

        # Extract the assistant's reply from the response
        answer = response.choices[0].message.content

        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
