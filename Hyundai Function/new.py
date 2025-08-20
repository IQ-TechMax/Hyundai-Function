import google.generativeai as genai
from google.generativeai.types import FunctionDeclaration

# Step 1: Configure your Gemini API key
genai.configure(api_key="AIzaSyCfUPSW-R2NHUFPHAW2xZUIRtocfwMnrZc")  # Replace with your actual key

# Step 2: Define function schema
functions = [
    FunctionDeclaration(
        name="book_car_service",
        description="Book a car service appointment for the customer",
        parameters={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "car_model": {"type": "string"},
                "car_number": {"type": "string"},
                "service_type": {"type": "string"},
                "date": {"type": "string"},
                "time": {"type": "string"},
                "phone": {"type": "string"},
            },
            "required": ["name", "car_model", "car_number", "service_type", "date", "time", "phone"]
        }
    )
]

# Step 3: Your local function to handle booking
def book_car_Service(name, car_model, car_number, service_type, date, time, phone):
    print("\n Calling 'book_car_service' function...")
    print(f"Name: {name}")
    print(f"Car Model: {car_model}")
    print(f"Car Number: {car_number}")
    print(f"Service Type: {service_type}")
    print(f"Date: {date}, Time: {time}")
    print(f"Phone: {phone}")
    
    return {
        "status": "success",
        "message": f"Thank you {name}, your {service_type} for {car_model} is booked on {date} at {time}."
    }

# Step 4: Handle the user input and AI response
def car_service(user_input):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        tools=functions
    )

    # Generate Gemini response with tool auto selection
    response = model.generate_content(
        user_input,
        tool_config={"function_calling_config": "AUTO"}
    )

    parts = response.candidates[0].content.parts
    if parts and hasattr(parts[0], "function_call"):
        call = parts[0].function_call
        if call.name == "book_car_service":
            args = call.args
            result = book_car_Service(
                name=args["name"],
                car_model=args["car_model"],
                car_number=args["car_number"],
                service_type=args["service_type"],
                date=args["date"],
                time=args["time"],
                phone=args["phone"]
            )

            # Send confirmation message to Gemini
            follow_up = model.generate_content(
                f"Here is the booking confirmation: {result['message']}. Please confirm."
            )
            print("\n", follow_up.text.strip())
        else:
            print(" Unknown function call.")
    else:
        print("\n", response.text.strip())

# Step 5: Simple chat loop
def start_chat():
    print(" Gemini Car Service Chatbot Started. Type 'exit' to quit.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        car_service(user_input)

# Entry point
if __name__ == "__main__":
    start_chat()
