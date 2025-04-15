
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Static data for Alif Laam Meem Clinic
clinic_info = {
    "name": "Alif Laam Meem",
    "address": "PECHS, Karachi",
    "services": ["Hijama (Cupping Therapy)"],
    "hours": "Monday–Saturday 10am–7pm; Closed on Sunday",
    "contact": {
        "phone": "+92 300 0000000",
        "email": "info@aliflaammeem.com"
    },
    "language_support": "All languages supported",
    "voice_support": True
}

# Simple keyword-based response generator
def generate_response(message):
    message_lower = message.lower()
    
    if "appointment" in message_lower or "book" in message_lower:
        return "To book an appointment for Hijama, please tell us your preferred date and time."
    elif "address" in message_lower or "location" in message_lower or "where" in message_lower:
        return f"Our clinic is located at: {clinic_info['address']}."
    elif "service" in message_lower or "hijama" in message_lower or "offer" in message_lower:
        return f"We offer: {', '.join(clinic_info['services'])}."
    elif "time" in message_lower or "hours" in message_lower or "open" in message_lower:
        return f"Our operating hours are: {clinic_info['hours']}."
    elif "contact" in message_lower or "phone" in message_lower or "email" in message_lower:
        return f"Phone: {clinic_info['contact']['phone']}, Email: {clinic_info['contact']['email']}."
    elif "language" in message_lower:
        return clinic_info['language_support']
    elif "voice" in message_lower:
        return "Yes, voice input is supported! Click the 🎤 icon to speak."
    elif "whatsapp" in message_lower:
        return "You can also reach us on WhatsApp at +92 300 0000000."
    elif "hello" in message_lower or "hi" in message_lower or "salam" in message_lower:
        return "Welcome to Alif Laam Meem Clinic. How can I assist you today?"
    else:
        return "I'm here to assist with appointments, services, location, and contact details for Alif Laam Meem Clinic."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
