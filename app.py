from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up the OpenAI API key
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        topic = request.form['topic']
        num_questions = int(request.form['num_questions'])

        prompt = f"Generate {num_questions} multiple-choice questions about the topic '{topic}'. Provide the questions only, without options or correct answers."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150*num_questions,
            n=1,
            stop=None,
            temperature=0.5,
        )

        questions = response.choices[0].text.strip().split('\n')
        questions = [q for q in questions if q]  # Filter out empty lines

        return jsonify({'questions': questions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
