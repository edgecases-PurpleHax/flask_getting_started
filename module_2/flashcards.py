from flask import Flask
import datetime

app = Flask(__name__)

count = 0

@app.route("/")
def welcome():
    """
    Route for the welcome page.

    Returns:
        str: A welcome message.
    """
    return "Welcome to my Flash Cards application"

@app.route("/date")
def date():
    """
    Route to display the current date and time.

    Returns:
        str: The current date and time.
    """
    return f"This page was served at {datetime.datetime.now()}"

@app.route("/view_count")
def views():
    """
    Route to display the view count.

    Returns:
        str: The number of times the page has been viewed.
    """
    global count  # Use the global keyword to modify the global variable
    count += 1
    return f"This page has been viewed {count} times"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

