
import base64
import os
from google import genai
from google.genai import types

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



def generate(user_input,api_key):
    client = genai.Client(
        api_key
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input),
            ],
        ),
    ]
    tools = [
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
    

def start_chat():
    
    api_key = "AIzaSyCAQoIw6PfyKFCH7Yc4q6u6BL_5-bgbs30"
    if not api_key:
        raise ValueError("Google API Key not found in .env or hardcoded.")

    print("Chat Bot Started. Type 'exit' or 'quit' to stop chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        
        generate(user_input)
        


if __name__ == "__main__":
    start_chat()