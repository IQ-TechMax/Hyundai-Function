import google.generativeai as genai
from google.generativeai.types import Tool

# Step 1: Configure Gemini API
genai.configure(api_key="AIzaSyCAQoIw6PfyKFCH7Yc4q6u6BL_5-bgbs30")  #  Replace with your actual API key

# Step 2: Define Tool Functions
functions = [
    {
        "name": "schedule_test_drive",
        "description": "Schedule a test drive for the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {"type": "string", "description": "Customer name"},
                "phone": {"type": "string", "description": "Phone number"},
                "car_model": {"type": "string", "description": "Preferred car model"},
                "date": {"type": "string", "description": "Test drive date"},
                "time": {"type": "string", "description": "Preferred time"},
                "location": {"type": "string", "description": "Test drive location"}
            },
            "required": ["customer_name", "phone", "car_model", "date", "time", "location"]
        }
    },
    {
        "name": "check_car_availability",
        "description": "Check if a specific Hyundai car model is available in stock.",
        "parameters": {
            "type": "object",
            "properties": {
                "car_model": {"type": "string", "description": "Car model to check"},
                "location": {"type": "string", "description": "Location to check availability"}
            },
            "required": ["car_model"]
        }
    }
]

# Step 3: Load the model with tools
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # or gemini-2.5-flash
    tools=[Tool(function_declarations=functions)]
)

# Step 4: Start a chat session
chat = model.start_chat()

print("Chatbot Ready. Type your query or 'exit' to quit.")

# Step 5: CLI loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)

        function_handled = False
        for part in response.parts:
            if hasattr(part, "function_call"):
                fn = part.function_call
                print(f"\nFunction to call: {fn.name}")
                print(f"Arguments: {fn.args}")
                function_handled = True
            elif hasattr(part, "text"):
                print(f"\n Bot: {part.text}")
                function_handled = True

        if not function_handled:
            print("\n Bot: No response or unknown format.")
    except Exception as e:
        print(f"\n Error: {e}")

