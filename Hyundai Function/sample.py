import os
import google.generativeai as genai
from google.generativeai.types import Tool

# === Step 1: Load API Key ===

api_key = "AIzaSyCAQoIw6PfyKFCH7Yc4q6u6BL_5-bgbs30"

if not api_key:
    raise ValueError("Google API Key not found in .env or hardcoded.")

genai.configure(api_key=api_key)

# === Step 2: Function Declarations ===

CHECK_CAR_AVAILABILITY = {
    "name": "check_car_availability",
    "description": "Check if the specific Hyundai car model is available in the stock.",
    "parameters": {
        "type": "object",
        "properties": {
            "car_model": {
                "type": "string",
                "description": "The Hyundai car model to check for availability."
            },
            "location": {
                "type": "string",
                "description": "Location to check availability of the car model."
            }
        },
        "required": ["car_model"]
    }
}

SCHEDULE_TEST_DRIVE = {
    "name": "schedule_test_drive",
    "description": "Schedule a test drive for the customer.",
    "parameters": {
        "type": "object",
        "properties": {
            "customer_name": {
                "type": "string",
                "description": "The name of the customer making the enquiry."
            },
            "phone": {
                "type": "string",
                "description": "The phone number of the customer to schedule test drive."
            },
            "car_model": {
                "type": "string",
                "description": "Customer preferred car model for test drive."
            },
            "date": {
                "type": "string",
                "description": "Specific date for the customer to do test drive."
            },
            "time": {
                "type": "string",
                "description": "Customer preferred time to test drive the car."
            },
            "location": {
                "type": "string",
                "description": "Available location to test drive the car."
            }
        },
        "required": ["customer_name", "phone", "car_model", "date", "time", "location"]
    }
}

# === Step 3: Python Functions ===

def check_car_availability(car_model: str, location: str = "default showroom"):
    available_cars = ["creta", "venue", "i20", "verna", "tucson"]
    if car_model.lower() in available_cars:
        return f" The {car_model.title()} is available at {location}."
    else:
        return f" Sorry, the {car_model.title()} is not available currently at {location}."

def schedule_test_drive(customer_name, phone, car_model, date, time, location):
    return (
        f" Test drive scheduled successfully!\n"
        f" Name: {customer_name}\n"
        f" Phone: {phone}\n"
        f" Car Model: {car_model}\n"
        f" Date: {date} at {time}\n"
        f" Location: {location}"
    )

# === Step 4: Register Functions ===

tool = Tool(function_declarations=[CHECK_CAR_AVAILABILITY, SCHEDULE_TEST_DRIVE])
model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools=[tool])

functions = {
    "check_car_availability": check_car_availability,
    "schedule_test_drive": schedule_test_drive
}

# === Step 5: Chat Loop ===

chat = model.start_chat()
print("Hyundai Chatbot (Gemini)")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        part = response.candidates[0].content.parts[0]

        # Handle function calls
        if hasattr(part, "function_call") and part.function_call:
            fn = part.function_call
            name = fn.name or ""
            args = fn.args or {}

            if name in functions:
                result = functions[name](**args)

                # Send back result to Gemini
                response = chat.send_message({
                    "function_response": {
                        "name": name,
                        "response": {"result": result}
                    }
                })
                part = response.candidates[0].content.parts[0]
                print(f"Bot: {part.text}\n")
            else:
                print(f" Unknown function '{name}'\n")
        else:
            print(f"Bot: {part.text}\n")

    except Exception as e:
        print(f"Error: {e}\n")
