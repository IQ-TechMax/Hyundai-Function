# initiate_cold_call
# collect_customer_preferences
# schedule_follow_up_call
# log_unanswered_call
# book_test_drive
# assign_agent_for_test_drive
# send_test_drive_reminder
# collect_test_drive_feedback
# provide_quotation_and_finance_options
# handle_price_negotiation
# suggest_accessories_and_insurance
# process_booking_documents
# schedule_pre_delivery_inspection
# arrange_vehicle_delivery
# send_delivery_notification
# post_delivery_follow_up
# generate_call_dashboard_report
# get_call_details_by_date
# log_call_duration_and_recording
# reschedule_customer_call

AI_SALES_FUNCTIONS = [

    {
        "name": "initiate_cold_call",
        "description": "Initiate a cold call to a potential customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer being contacted."
                },
                "phone": {
                    "type": "string",
                    "description": "Phone number of the customer."
                },
                "region": {
                    "type": "string",
                    "description": "Customer's geographical location or region."
                }
            },
            "required": ["customer_name", "phone", "region"]
        }
    },

    {
        "name": "collect_customer_preferences",
        "description": "Collect customer preferences for vehicle model, budget, and features.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "car_type": {
                    "type": "string",
                    "description": "Type of car the customer prefers (e.g., SUV, sedan)."
                },
                "budget_range": {
                    "type": "string",
                    "description": "Preferred budget range (e.g., ₹10L - ₹15L)."
                },
                "preferred_features": {
                    "type": "string",
                    "description": "Specific features the customer is looking for (e.g., sunroof, touchscreen)."
                }
            },
            "required": ["customer_name", "car_type", "budget_range", "preferred_features"]
        }
    },

    {
        "name": "schedule_follow_up_call",
        "description": "Schedule a follow-up call for further discussion or qualification.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "phone": {
                    "type": "string",
                    "description": "Customer's phone number."
                },
                "follow_up_date": {
                    "type": "string",
                    "description": "Date for the follow-up call (YYYY-MM-DD)."
                },
                "purpose": {
                    "type": "string",
                    "description": "Purpose of the follow-up call (e.g., explain pricing, test drive confirmation)."
                }
            },
            "required": ["customer_name", "phone", "follow_up_date", "purpose"]
        }
    },

    {
        "name": "log_unanswered_call",
        "description": "Log an unanswered customer call and schedule a callback.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer’s full name."
                },
                "phone": {
                    "type": "string",
                    "description": "Customer’s phone number."
                },
                "attempt_date": {
                    "type": "string",
                    "description": "Date of the attempted call (YYYY-MM-DD)."
                },
                "retry_time": {
                    "type": "string",
                    "description": "Proposed time for recalling the customer."
                }
            },
            "required": ["customer_name", "phone", "attempt_date", "retry_time"]
        }
    },

    {
        "name": "book_test_drive",
        "description": "Book a test drive for the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer."
                },
                "phone": {
                    "type": "string",
                    "description": "Customer’s contact number."
                },
                "car_model": {
                    "type": "string",
                    "description": "Car model requested for the test drive."
                },
                "date": {
                    "type": "string",
                    "description": "Preferred test drive date."
                },
                "time": {
                    "type": "string",
                    "description": "Preferred test drive time."
                },
                "location": {
                    "type": "string",
                    "description": "Test drive location (showroom/home)."
                }
            },
            "required": ["customer_name", "phone", "car_model", "date", "time", "location"]
        }
    },

    {
        "name": "assign_agent_for_test_drive",
        "description": "Assign a sales agent to handle the customer's test drive.",
        "parameters": {
            "type": "object",
            "properties": {
                "agent_name": {
                    "type": "string",
                    "description": "Name of the agent to be assigned."
                },
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer scheduled for the test drive."
                },
                "location": {
                    "type": "string",
                    "description": "Location of the test drive (showroom or customer address)."
                }
            },
            "required": ["agent_name", "customer_name", "location"]
        }
    },

    {
        "name": "send_test_drive_reminder",
        "description": "Send a test drive reminder to the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "phone": {
                    "type": "string",
                    "description": "Customer's contact number."
                },
                "date": {
                    "type": "string",
                    "description": "Date of the scheduled test drive."
                },
                "time": {
                    "type": "string",
                    "description": "Time of the scheduled test drive."
                }
            },
            "required": ["customer_name", "phone", "date", "time"]
        }
    },

    {
        "name": "collect_test_drive_feedback",
        "description": "Collect customer feedback after the test drive.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "rating": {
                    "type": "integer",
                    "description": "Customer rating from 1 to 5."
                },
                "feedback": {
                    "type": "string",
                    "description": "Customer's comments about the test drive experience."
                }
            },
            "required": ["customer_name", "rating", "feedback"]
        }
    },

    {
        "name": "provide_quotation_and_finance_options",
        "description": "Provide a quotation and available financing options to the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer’s full name."
                },
                "car_model": {
                    "type": "string",
                    "description": "Model for which quotation is shared."
                },
                "base_price": {
                    "type": "number",
                    "description": "Base price of the selected model."
                },
                "loan_options": {
                    "type": "string",
                    "description": "Available loan/EMI options."
                }
            },
            "required": ["customer_name", "car_model", "base_price", "loan_options"]
        }
    },

    {
        "name": "handle_price_negotiation",
        "description": "Handle price negotiation discussion with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer involved in negotiation."
                },
                "requested_discount": {
                    "type": "string",
                    "description": "Customer's discount request."
                },
                "final_offer": {
                    "type": "string",
                    "description": "Final offer provided by the dealership."
                }
            },
            "required": ["customer_name", "requested_discount", "final_offer"]
        }
    },

    {
        "name": "suggest_accessories_and_insurance",
        "description": "Suggest accessories and insurance packages to the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "car_model": {
                    "type": "string",
                    "description": "Selected car model."
                },
                "recommended_accessories": {
                    "type": "string",
                    "description": "List of recommended accessories."
                },
                "insurance_packages": {
                    "type": "string",
                    "description": "Available insurance options."
                }
            },
            "required": ["customer_name", "car_model", "recommended_accessories", "insurance_packages"]
        }
    },

    {
        "name": "process_booking_documents",
        "description": "Process and verify all booking-related documents.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "document_type": {
                    "type": "string",
                    "description": "Type of document (e.g., ID proof, loan form)."
                },
                "document_url": {
                    "type": "string",
                    "description": "Secure link to the uploaded document."
                }
            },
            "required": ["customer_name", "document_type", "document_url"]
        }
    },

    {
        "name": "schedule_pre_delivery_inspection",
        "description": "Schedule a pre-delivery inspection for the vehicle.",
        "parameters": {
            "type": "object",
            "properties": {
                "car_model": {
                    "type": "string",
                    "description": "Model of the vehicle to inspect."
                },
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "inspection_date": {
                    "type": "string",
                    "description": "Date scheduled for PDI."
                }
            },
            "required": ["car_model", "customer_name", "inspection_date"]
        }
    },

    {
        "name": "arrange_vehicle_delivery",
        "description": "Arrange vehicle delivery to the showroom or customer location.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "delivery_mode": {
                    "type": "string",
                    "description": "Mode of delivery (e.g., showroom, home)."
                },
                "delivery_date": {
                    "type": "string",
                    "description": "Scheduled delivery date."
                }
            },
            "required": ["customer_name", "delivery_mode", "delivery_date"]
        }
    },

    {
        "name": "send_delivery_notification",
        "description": "Send a notification to the customer about upcoming vehicle delivery.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer’s full name."
                },
                "delivery_date": {
                    "type": "string",
                    "description": "Date of delivery."
                },
                "location": {
                    "type": "string",
                    "description": "Delivery location."
                }
            },
            "required": ["customer_name", "delivery_date", "location"]
        }
    },

    {
        "name": "post_delivery_follow_up",
        "description": "Follow up with the customer after vehicle delivery.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "feedback_rating": {
                    "type": "integer",
                    "description": "Feedback rating from 1 to 5."
                },
                "additional_requests": {
                    "type": "string",
                    "description": "Any post-delivery queries or requests from the customer."
                }
            },
            "required": ["customer_name", "feedback_rating", "additional_requests"]
        }
    },

    {
        "name": "generate_call_dashboard_report",
        "description": "Generate a call activity report for the dashboard.",
        "parameters": {
            "type": "object",
            "properties": {
                "from_date": {
                    "type": "string",
                    "description": "Start date of the report (YYYY-MM-DD)."
                },
                "to_date": {
                    "type": "string",
                    "description": "End date of the report (YYYY-MM-DD)."
                }
            },
            "required": ["from_date", "to_date"]
        }
    },

    {
        "name": "get_call_details_by_date",
        "description": "Get detailed call logs for a specific date.",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Date for which to retrieve call details (YYYY-MM-DD)."
                }
            },
            "required": ["date"]
        }
    },

    {
        "name": "log_call_duration_and_recording",
        "description": "Log the duration and audio recording URL of a customer call.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer’s full name."
                },
                "call_duration": {
                    "type": "string",
                    "description": "Length of the call in minutes/seconds (e.g., '03:15')."
                },
                "recording_url": {
                    "type": "string",
                    "description": "URL of the recorded audio file."
                },
                "call_date": {
                    "type": "string",
                    "description": "Date of the call."
                }
            },
            "required": ["customer_name", "call_duration", "recording_url", "call_date"]
        }
    },

    {
        "name": "reschedule_customer_call",
        "description": "Reschedule a missed or postponed call with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer."
                },
                "old_time": {
                    "type": "string",
                    "description": "Previously scheduled time."
                },
                "new_time": {
                    "type": "string",
                    "description": "New proposed time for the call."
                }
            },
            "required": ["customer_name", "old_time", "new_time"]
        }
    }

]

