# Import Flask library
from flask import Flask, render_template, request

# Create Flask application
app = Flask(_name_)

# Function to process user prompt
def process_prompt(prompt):
    # Convert text to lowercase for easy matching
    prompt = prompt.lower()

    # If user asks to explain cloud computing
    if "explain cloud computing" in prompt:
        return "Cloud computing is the delivery of computing services like storage, servers, and software over the internet."

    # If user asks to generate project ideas
    elif "generate project ideas" in prompt:
        return """Here are some project ideas:
1. Cloud File Storage System
2. Online Attendance System
3. E-Learning Platform
4. Weather Information App"""

    # If user asks to summarize text
    elif "summarize" in prompt:
        # Remove the word 'summarize' from input
        text = prompt.replace("summarize this text:", "")
        
        # Simple summary logic (first sentence only)
        return "Summary: " + text.strip().split(".")[0]

    # If greeting
    elif "hello" in prompt or "hi" in prompt:
        return "Hello! Welcome to the Cloud-Based Prompt System."

    # Default response
    else:
        return "Sorry, I cannot understand your prompt."

# Route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    # If user submits form
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        response = process_prompt(user_prompt)

    # Send response to HTML page
    return render_template("index.html", response=response)

# Run the app
if _name_ == "_main_":
    app.run(debug=True)