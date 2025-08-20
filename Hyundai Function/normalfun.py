all_model = {
    "Creta": {"type": "SUV", "price": "15 lakhs"},
    "Venue": {"type": "SUV", "price": "10 lakhs"},
    "i20": {"type": "Hatchback", "price": "9 lakhs"},
    "Verna": {"type": "Sedan", "price": "13 lakhs"}
}

def inquire_car_models(preferred_car_model,budget_range):
    if preferred_car_model in all_model:
        if budget_range in all_model[preferred_car_model]["price"]:
            print("You order has confirmed:")
            print(f"Prefeered car Model:{preferred_car_model}")
            print(f"Final Budget:{budget_range}")
            
def start_chat():
    print("Chat Started. Type 'exit' to quit chat")
    while True:
        customer_name=input("Enter the customer name: ")
        if customer_name.lower() == "exit":
            break  
        print(f"Hello {customer_name}.Here are the Hyundai car models")
        print(all_model)
        preferred_car_model=input("Enter the prefered type: ")
        budget_range=input("Enter the budget: ")
        inquire_car_models(preferred_car_model,budget_range)
    
    
    
if __name__ == "__main__":
    start_chat()
    
    
    
###############################################################################################
   
functions =[
    {"name":"schedule_test_drive",
     "description":"schedule a test drive for the customer.",
     "parameters":
        {
         "type": "object",
         "properties":
             {
             "customer_name":
                {
                    "type":"string",
                    "description":"The name of the customer making the enquire."
                },
             "phone":{"type":"string",
                      "description":"The phone number of the customer to schedule test drive."},
             "car_model":{"type":"string",
                          "description":"customer preferred car model for test drive."},
             "date":{"type":"string",
                     "description":"specific date for the customer to do test drive."},
             "time":{"type":"string",
                     "description":"customer preferred time for test drive the car."},
             "location":{"type":"string",
                         "description":"available location to test drive the car."}
            },
         "required":["customer_name","phone","car_model","date","time","location"]
        }  
    },
    
    {"name":"check car availability",
     "description":"check if the specific Hyundai car model is available in the stock",
     "parameters":{"type":"object",
                   "properties":{"car_model":{"type":"string",
                                              "description":"check the car model available in the stock"},
                                 "location":{"type":"string",
                                             "description":"available location to buy the car model available in the stock"}
                                 },
                   "required":["car_model"]
                   }
     
    },
    
    {
        "name":"book_car_purchase",
        "description":"Book a car purchase for the customer.",
        "parameters":
            {
                "type":"object",
                "Properties":
                    {
                    "customer_name":
                        {
                            "type":"string",
                            "description":"The name of the customer to purchase the hyundai car."
                        },
                    "Phone":
                        {
                            "type":"object",
                            "description":"The phone number of the customer purchasing hyundai car."
                        },
                    "car-model":
                        {
                            "type":"string",
                            "description":"model of the hyundai car purchasing by the customer"
                        },
                    "variant":
                        {
                            "type":"string",
                            "description":"-------------"
                        },
                    "color":
                        {
                            "type":"string",
                            "description":"color of the hyundai car customer purchasing"
                        },
                    "payment_method":
                        {
                            "type":"string",
                            "description":"payment method of the customer purchasing hyundai car"
                        },
                    "preferred_delivery_date":
                        {
                            "type":"string",
                            "description":"customer preferred deliver date for hyundai car"
                        }
                    },
                "required":["customer_name","phone","car_model","variant","payment_method"]
                    
            }
    },
    
    {
        "name":"apply_loan_finance",
        "description":"Help the customer apply for car loan or finance options.",
        "parameters":
            {
                "type":"object",
                "properties":
                    {
                        "customer_name":
                            {
                                "type":"string",
                                "description":"name of the customer applying for loan to buy hundai car."
                            },
                        "phone":
                            {
                                "type":"string",
                                "description":"phone number of the customer applying loan to buy hyundai car"
                            },
                        "car_model":
                            {
                                "type":"string",
                                "description":"car model choose by customer applying loan"
                            },
                        "loan_amount":
                            {
                                "type":"string",
                                "description":"loan amount to purchase hyundai car"
                            },
                        "tenure_years":
                            {
                                "type":"string",
                                "description":"total number of tenure years to pay loan applying to buy hyundai car"
                            },
                        "income_proof":
                            {
                                "type":"string",
                                "description":"customer income document proof to pay loan applying to buy hyundai car."
                            }
                    },
                "required":["customer_name","phone","car_model","loan_amount","tenure_year"]
            }
    },
    
    {
        "name":"sumbit_kyc_documents",
        "description":"collect and submit customer's KYC documents for car purchase.",
        "parameters":
            {
                "type":"object",
                "properties":{
                    "customer_name":
                        {
                            "type":"string",
                            "description":"name of the customer purchasing car"
                        },
                    "phone":
                        {
                            "type":"string",
                            "description":"phone number of the customer purchasing car"
                        },
                    "aadhar_number":
                        {
                            "type":"string",
                            "description":"12 digit aadhar card number of the customer purchasing car"
                        },
                    "pan_number":
                        {
                            "type":"string",
                            "description":"pan card number of the customer purchasing hyundai car"
                        },
                    "id_proof":
                        {
                            "type":"string",
                            "description":"id proof of the customer purchasing hyundai car or summiting KYC document"
                        }
                },
                "required":["customer_name","phone","aadhaar_number","pan_number"]
            }
    },

    {
        "name": "schedule_car_delivery",
        "description": "Schedule delivery of the purchased car.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer who purchased the car."
                },
                "car_model": {
                    "type": "string",
                    "description": "The model name of the purchased car to be delivered."
                },
                "delivery_address": {
                    "type": "string",
                    "description": "The complete address where the car should be delivered."
                },
                "preferred_delivery_date": {
                    "type": "string",
                    "format": "date",
                    "description": "The date the customer prefers for car delivery (YYYY-MM-DD)."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Customer's mobile number for delivery updates or contact."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "delivery_address",
                "preferred_delivery_date",
                "contact_number"
            ]
        }
    },
    {
        "name": "track_car_delivery_status",
        "description": "Track the status of car delivery.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The unique order ID provided during car purchase."
                },
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer who placed the car order."
                }
            },
            "required": [
                "order_id",
                "customer_name"
            ]
        }
    },
    
    {
        "name": "register_car_rto",
        "description": "Register the purchased car with the RTO (Regional Transport Office) and generate the official number plate.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the car owner."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model of the car to be registered."
                },
                "chassis_number": {
                    "type": "string",
                    "description": "Unique chassis number of the car."
                },
                "rto_location": {
                    "type": "string",
                    "description": "City or region of the RTO office where registration will take place."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Phone number of the customer for RTO communication and updates."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "chassis_number",
                "rto_location",
                "contact_number"
            ]
        }
    },
    {
        "name": "add_car_accessories",
        "description": "Allow the customer to choose and book additional car accessories.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model of the car for which accessories are being added."
                },
                "accessories_list": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of accessories the customer wants to add (e.g., floor mats, fog lamps, infotainment system)."
                },
                "preferred_installation_date": {
                    "type": "string",
                    "format": "date",
                    "description": "Date preferred by the customer for accessory installation (YYYY-MM-DD)."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "accessories_list",
                "preferred_installation_date"
            ]
        }
    },
    {
        "name": "apply_insurance_policy",
        "description": "Help the customer apply for or activate a car insurance policy.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer applying for insurance."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model of the car to be insured."
                },
                "insurance_type": {
                    "type": "string",
                    "description": "Type of insurance the customer wants (e.g., third-party, comprehensive)."
                },
                "insurance_provider": {
                    "type": "string",
                    "description": "Name of the insurance company the customer prefers."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Customer’s contact number for policy updates and verifications."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "insurance_type",
                "insurance_provider",
                "contact_number"
            ]
        }
    },
    
    {
        "name": "book_car_service",
        "description": "Book a car service appointment at an authorized service center.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the car owner booking the service."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model of the car that needs servicing."
                },
                "service_type": {
                    "type": "string",
                    "description": "Type of service requested (e.g., general service, engine check, oil change)."
                },
                "preferred_date": {
                    "type": "string",
                    "format": "date",
                    "description": "Preferred date for the service appointment (YYYY-MM-DD)."
                },
                "pickup_required": {
                    "type": "boolean",
                    "description": "Whether the customer wants home pickup for the car."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Phone number of the customer for service-related communication."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "service_type",
                "preferred_date",
                "pickup_required",
                "contact_number"
            ]
        }
    },
    {
        "name": "track_service_status",
        "description": "Check the live status of a car that is currently undergoing service.",
        "parameters": {
            "type": "object",
            "properties": {
                "service_id": {
                    "type": "string",
                    "description": "Unique service ID provided during booking."
                },
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer who booked the service."
                }
            },
            "required": [
                "service_id",
                "customer_name"
            ]
        }
    },
    {
        "name": "request_roadside_assistance",
        "description": "Call for emergency roadside support for breakdowns, flat tires, or towing.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer requesting assistance."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model of the car needing assistance."
                },
                "location": {
                    "type": "string",
                    "description": "Current location or address of the car."
                },
                "issue_description": {
                    "type": "string",
                    "description": "Brief description of the issue (e.g., flat tire, engine failure)."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Customer’s phone number for assistance coordination."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "location",
                "issue_description",
                "contact_number"
            ]
        }
    },
    {
        "name": "schedule_maintenance_reminder",
        "description": "Set a reminder for future car maintenance or service.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the car owner."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model of the car for which the reminder is being set."
                },
                "reminder_date": {
                    "type": "string",
                    "format": "date",
                    "description": "Date on which the reminder should be triggered (YYYY-MM-DD)."
                },
                "service_type": {
                    "type": "string",
                    "description": "Type of maintenance or service the reminder is for (e.g., oil change, brake check)."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Customer's phone number to receive the reminder notification."
                }
            },
            "required": [
                "customer_name",
                "car_model",
                "reminder_date",
                "service_type",
                "contact_number"
            ]
        }
    },
    
    {
        "name": "submit_customer_feedback",
        "description": "Log customer feedback, suggestions, or complaints related to their experience.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer submitting the feedback."
                },
                "feedback_type": {
                    "type": "string",
                    "description": "Type of feedback (e.g., complaint, suggestion, appreciation)."
                },
                "feedback_message": {
                    "type": "string",
                    "description": "Detailed message or description of the feedback."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Customer’s phone number in case follow-up is needed."
                }
            },
            "required": [
                "customer_name",
                "feedback_type",
                "feedback_message",
                "contact_number"
            ]
        }
    },
    {
        "name": "connect_customer_support",
        "description": "Connect the customer to a live support agent for assistance.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer seeking support."
                },
                "query_topic": {
                    "type": "string",
                    "description": "Brief description of the issue or query topic (e.g., billing, service delay, technical support)."
                },
                "preferred_language": {
                    "type": "string",
                    "description": "Preferred language for communication with the support agent."
                },
                "contact_number": {
                    "type": "string",
                    "description": "Phone number where the customer can be contacted."
                }
            },
            "required": [
                "customer_name",
                "query_topic",
                "preferred_language",
                "contact_number"
            ]
        }
    },
    {
    "name": "collect_customer_details",
    "description": "Collect and save new customer profile information.",
    "parameters": {
        "type": "object",
        "properties": {
            "customer_name": {
                "type": "string",
                "description": "Full name of the customer (e.g., Rahul Sharma)."
            },
            "phone": {
                "type": "string",
                "description": "Customer's mobile phone number (e.g., +91XXXXXXXXXX)."
            },
            "email": {
                "type": "string",
                "description": "Customer's email address for communication and updates."
            },
            "address": {
                "type": "string",
                "description": "Customer's full residential address including street, city, and state."
            },
            "preferred_contact_time": {
                "type": "string",
                "description": "Time range when the customer prefers to be contacted (e.g., 10 AM - 1 PM)."
            }
        },
        "required": [
            "customer_name",
            "phone"
        ]
    }
},
    
{
    "name": "schedule_maintenance_reminder",
    "description": "Set up a reminder for periodic car maintenance or service.",
    "parameters": {
        "type": "object",
        "properties": {
            "car_number": {
                "type": "string",
                "description": "Registered number of the customer's car (e.g., TN07AB1234)."
            },
            "customer_name": {
                "type": "string",
                "description": "Full name of the customer who owns the vehicle."
            },
            "service_type": {
                "type": "string",
                "description": "Type of service to be reminded for (e.g., general service, oil change)."
            },
            "reminder_date": {
                "type": "string",
                "description": "Scheduled date for the reminder in YYYY-MM-DD format."
            },
            "phone": {
                "type": "string",
                "description": "Customer's phone number for sending reminder alerts."
            }
        },
        "required": [
            "car_number",
            "customer_name",
            "service_type",
            "reminder_date"
        ]
    }
}
    
] 