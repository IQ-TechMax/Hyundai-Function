
from google import genai
from google.genai import types

# Define the function declaration for the model
inquire_car_models_function = {
    "name": "inquire_car_models",
    "description": "Show available Hyundai car models to the customer.",
    "parameters": {
        "type": "object",
        "properties": {
            "customer_name": {
                "type": "string",
                "description": "The name of the customer making the inquiry."
            },
            "preferred_type": {
                "type": "string",
                "description": "e.g., SUV, Sedan, Hatchback"
            },
            "budget_range": {
                "type": "string",
                "description": "The budget range the customer is interested in (e.g., '10-15 lakhs')"
            },
        },
        "required": ["customer_name"]
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[inquire_car_models_function])
config = types.GenerateContentConfig(tools=[tools])

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config=config,
    )

    # Check for a function call
    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        print(f"Function to call: {function_call.name}")
        print(f"Arguments: {function_call.args}")
        #  In a real app, you would call your function here:
        #  result = schedule_meeting(**function_call.args)
    else:
        print("No function call found in the response.")
        print(response.text)