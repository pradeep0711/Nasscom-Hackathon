import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyDxTjNoyTRiHcIQsN0YHtEWwTP4XAjSpaU")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")
class EmailGenerator:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! I am {self.name}, your AI assistant. How can I assist you with generating personalized emails today?"

    def generate_email(self, recipient_name, event_name, special_instructions=""):
        """Generates a personalized email using Gemini AI."""
        prompt = f"""
        Compose a professional and personalized email for {recipient_name} regarding the event: {event_name}.
        Special Instructions: {special_instructions}
        """
        response = model.generate_content(prompt)
        return response.text if response else "I'm not sure, but I'm learning!"