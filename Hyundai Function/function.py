functions = [
    {
        "name": "inquire_car_models",
        "description": "Show available Hyundai car models to the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {"type": "string"},
                "preferred_type": {"type": "string", "description": "e.g., SUV, Sedan, Hatchback"},
                "budget_range": {"type": "string"}
            },
            "required": ["customer_name"]
        }
    },
    
    
    {
        "name": "schedule_test_drive",
        "description": "Schedule a test drive for the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {"type": "string"},
                "phone": {"type": "string"},
                "car_model": {"type": "string"},
                "date": {"type": "string"},
                "time": {"type": "string"},
                "location": {"type": "string"}
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
                "car_model": {"type": "string"},
                "location": {"type": "string"}
            },
            "required": ["car_model"]
        }
    },
    {
        "name": "generate_car_quote",
        "description": "Generate a price quote for a selected Hyundai car model.",
        "parameters": {
            "type": "object",
            "properties": {
                "car_model": {"type": "string"},
                "variant": {"type": "string"},
                "location": {"type": "string"}
            },
            "required": ["car_model", "variant"]
        }
    },
    {
        "name": "book_car_purchase",
        "description": "Book a car purchase for the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {"type": "string"},
                "phone": {"type": "string"},
                "car_model": {"type": "string"},
                "variant": {"type": "string"},
                "color": {"type": "string"},
                "payment_method": {"type": "string"},
                "preferred_delivery_date": {"type": "string"}
            },
            "required": ["customer_name", "phone", "car_model", "variant", "payment_method"]
        }
    },
    {
        "name": "apply_loan_finance",
        "description": "Help the customer apply for car loan or finance options.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {"type": "string"},
                "phone": {"type": "string"},
                "car_model": {"type": "string"},
                "loan_amount": {"type": "string"},
                "tenure_years": {"type": "integer"},
                "income_proof": {"type": "string", "description": "URL or document ID of proof"}
            },
            "required": ["customer_name", "phone", "car_model", "loan_amount", "tenure_years"]
        }
    },
    {
        "name": "submit_kyc_documents",
        "description": "Collect and submit customer's KYC documents for car purchase.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {"type": "string"},
                "phone": {"type": "string"},
                "aadhaar_number": {"type": "string"},
                "pan_number": {"type": "string"},
                "address_proof": {"type": "string", "description": "URL or document ID"},
                "id_proof": {"type": "string", "description": "URL or document ID"}
            },
            "required": ["customer_name", "phone", "aadhaar_number", "pan_number"]
        }
    }
]
