import os
import random
# Using the import style from the latest documentation
from google import genai
from google.generativeai import types

# --- Function Definitions & Declarations ---
# In this pattern, we need both the Python function and a JSON-like
# declaration for the model to understand the function.

def get_weather(city: str):
    """
    Gets the current weather for a specified city. Dummy function.
    """
    print(f"--- Executing Python function get_weather(city='{city}') ---")
    forecasts = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
    temp = random.randint(0, 35)
    return {
        "city": city,
        "forecast": random.choice(forecasts),
        "temperature": f"{temp}°C"
    }

# This is the declaration the model will see.
get_weather_declaration = {
    "name": "get_weather",
    "description": "Gets the current weather for a specified city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city to get the weather for (e.g., 'Paris', 'Tokyo')."
            }
        },
        "required": ["city"]
    }
}

# --- Main Application Logic ---

def main():
    """
    Main function to run the interactive CLI using the genai.Client pattern.
    """
    # 1. Initialize the Client
    # The Client automatically finds the GOOGLE_API_KEY from your environment variables.
    try:
        client = genai.Client()
    except Exception:
        print("\nERROR: Could not initialize client. Is the GOOGLE_API_KEY environment variable set?")
        return

    # 2. Define available tools
    # This maps the function name (string) to the actual Python function object.
    available_python_functions = {
        "get_weather": get_weather,
    }
    # This is the tool definition that will be sent to the API.
    tools = types.Tool(function_declarations=[get_weather_declaration])
    
    # The model name must be prefixed with "models/".
    model = f"gemini-2.0-flash"

    # 3. History Management for Interactive Chat
    # Since the client is stateless, we must manually keep track of the conversation.
    history = []

    print("--- Gemini CLI (Client Pattern) ---")
    print("Ask me something! Try 'What's the weather like in San Francisco?'.")
    print("Type 'quit' or 'exit' to end the chat.\n")

    # 4. Start the interactive loop
    while True:
        try:
            prompt = input("You: ")
            if prompt.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break

            # Append the user's message to the history
            history.append(types.Content(role="user", parts=[types.Part(text=prompt)]))

            # 5. Send the request to the model with the full conversation history
            response = client.generate_content(
                model=model,
                contents=history,
                tools=[tools],
            )
            
            message = response.candidates[0].content
            
            # 6. Check if the model wants to call a function
            if message.parts and message.parts[0].function_call:
                # Add the model's function call request to history before executing
                history.append(message)
                
                fc = message.parts[0].function_call
                func_name = fc.name
                func_args = fc.args
                
                print(f"🤖 Model wants to call: {func_name}({', '.join(f'{k}={v}' for k, v in func_args.items())})")

                # 7. Execute the corresponding Python function
                function_to_call = available_python_functions[func_name]
                function_response_data = function_to_call(**func_args)

                # 8. Send the function's result back to the model
                # Append the function result to history for the next turn
                function_response_part = types.Part.from_function_response(
                    name=func_name,
                    response={"result": function_response_data}
                )
                history.append(types.Content(role="user", parts=[function_response_part]))

                # Make a second API call with the function result included
                response_after_function_call = client.generate_content(
                    model=model,
                    contents=history,
                    tools=[tools],
                )
                
                # Get the final text and print it
                final_message = response_after_function_call.candidates[0].content
                print(f"Gemini: {final_message.parts[0].text}")
                # Add the final response to history
                history.append(final_message)

            else:
                # If no function call, just print the response and add it to history
                print(f"Gemini: {message.parts[0].text}")
                history.append(message)

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    main()