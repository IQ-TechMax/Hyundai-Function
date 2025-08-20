# send_service_reminder
# schedule_service_appointment
# confirm_service_appointment
# remind_appointment_day_of
# update_service_status
# upsell_service_addons
# send_invoice_and_payment_link
# collect_service_feedback
# handle_service_complaint
# initiate_loyalty_program_call
# send_thank_you_and_referral_message
# generate_service_call_report
# log_service_call_recording
# reschedule_service_appointment
# escalate_service_issue
# confirm_additional_service
# remind_pending_payment
# follow_up_post_service
# offer_extended_warranty
# close_service_ticket


AI_SERVICE_FUNCTIONS = [

    {
        "name": "send_service_reminder",
        "description": "Send a service reminder based on purchase date, mileage, or last service.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer."
                },
                "vehicle_registration": {
                    "type": "string",
                    "description": "Vehicle registration number."
                },
                "last_service_date": {
                    "type": "string",
                    "description": "Date of the last completed service."
                },
                "next_due_date": {
                    "type": "string",
                    "description": "Estimated due date for the next service."
                }
            },
            "required": ["customer_name", "vehicle_registration", "last_service_date", "next_due_date"]
        }
    },

    {
        "name": "schedule_service_appointment",
        "description": "Schedule a service appointment for the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "vehicle_registration": {
                    "type": "string",
                    "description": "Registration number of the vehicle."
                },
                "preferred_date": {
                    "type": "string",
                    "description": "Preferred date for the service appointment."
                },
                "preferred_time": {
                    "type": "string",
                    "description": "Preferred time slot for the service."
                },
                "service_type": {
                    "type": "string",
                    "description": "Type of service requested (e.g., general service, oil change, full checkup)."
                }
            },
            "required": ["customer_name", "vehicle_registration", "preferred_date", "preferred_time", "service_type"]
        }
    },

    {
        "name": "confirm_service_appointment",
        "description": "Confirm a scheduled service appointment with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "vehicle_registration": {
                    "type": "string",
                    "description": "Vehicle registration number."
                },
                "appointment_date": {
                    "type": "string",
                    "description": "Confirmed service appointment date."
                },
                "appointment_time": {
                    "type": "string",
                    "description": "Confirmed service appointment time."
                }
            },
            "required": ["customer_name", "vehicle_registration", "appointment_date", "appointment_time"]
        }
    },

    {
        "name": "remind_appointment_day_of",
        "description": "Send a reminder on the day of service appointment.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "appointment_date": {
                    "type": "string",
                    "description": "Date of the service appointment."
                },
                "appointment_time": {
                    "type": "string",
                    "description": "Time of the service appointment."
                }
            },
            "required": ["customer_name", "appointment_date", "appointment_time"]
        }
    },

    {
        "name": "update_service_status",
        "description": "Provide status updates on the ongoing service.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer."
                },
                "vehicle_registration": {
                    "type": "string",
                    "description": "Registration number of the vehicle."
                },
                "status": {
                    "type": "string",
                    "description": "Current status (e.g., 'In Progress', 'Ready for Delivery')."
                },
                "additional_recommendation": {
                    "type": "string",
                    "description": "Any recommended additional services or repairs."
                }
            },
            "required": ["customer_name", "vehicle_registration", "status", "additional_recommendation"]
        }
    },

    {
        "name": "upsell_service_addons",
        "description": "Suggest additional service add-ons based on vehicle condition or service history.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "vehicle_model": {
                    "type": "string",
                    "description": "Model of the vehicle."
                },
                "recommended_addons": {
                    "type": "string",
                    "description": "Suggested services like engine cleaning, AC disinfection, wheel alignment."
                }
            },
            "required": ["customer_name", "vehicle_model", "recommended_addons"]
        }
    },

    {
        "name": "send_invoice_and_payment_link",
        "description": "Send the final invoice and payment options to the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Customer's full name."
                },
                "invoice_url": {
                    "type": "string",
                    "description": "Secure link to the digital invoice."
                },
                "amount_due": {
                    "type": "number",
                    "description": "Total amount to be paid for the service."
                },
                "payment_options": {
                    "type": "string",
                    "description": "Accepted payment methods (e.g., UPI, card, net banking)."
                }
            },
            "required": ["customer_name", "invoice_url", "amount_due", "payment_options"]
        }
    },

    {
        "name": "collect_service_feedback",
        "description": "Collect customer feedback after service is completed.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "rating": {
                    "type": "integer",
                    "description": "Customer's rating on a scale of 1 to 5."
                },
                "comments": {
                    "type": "string",
                    "description": "Customer's detailed feedback or suggestions."
                },
                "follow_up_required": {
                    "type": "boolean",
                    "description": "Indicates if a follow-up call is needed based on the feedback."
                }
            },
            "required": ["customer_name", "rating", "comments", "follow_up_required"]
        }
    },

    {
        "name": "handle_service_complaint",
        "description": "Handle customer complaints about the service experience.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer lodging the complaint."
                },
                "complaint_details": {
                    "type": "string",
                    "description": "Description of the customer's issue."
                },
                "complaint_date": {
                    "type": "string",
                    "description": "Date the complaint was received."
                },
                "escalate_to_manager": {
                    "type": "boolean",
                    "description": "Whether the complaint should be escalated to the service manager."
                }
            },
            "required": ["customer_name", "complaint_details", "complaint_date", "escalate_to_manager"]
        }
    },

    {
        "name": "initiate_loyalty_program_call",
        "description": "Contact eligible customers about loyalty or referral programs.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "loyalty_offer": {
                    "type": "string",
                    "description": "Type of offer (e.g., 15% discount, free wheel alignment)."
                },
                "eligibility_reason": {
                    "type": "string",
                    "description": "Why the customer qualifies for the program (e.g., 3rd service, positive feedback)."
                }
            },
            "required": ["customer_name", "loyalty_offer", "eligibility_reason"]
        }
    },

    {
        "name": "send_thank_you_and_referral_message",
        "description": "Send a thank-you message after service completion and ask for referrals.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer."
                },
                "referral_code": {
                    "type": "string",
                    "description": "Referral code or link to share with friends or family."
                },
                "message_channel": {
                    "type": "string",
                    "description": "Preferred channel to send the message (e.g., SMS, WhatsApp, email)."
                }
            },
            "required": ["customer_name", "referral_code", "message_channel"]
        }
    },

    {
        "name": "generate_service_call_report",
        "description": "Generate a dashboard report for service-related calls.",
        "parameters": {
            "type": "object",
            "properties": {
                "from_date": {
                    "type": "string",
                    "description": "Start date for the report (YYYY-MM-DD)."
                },
                "to_date": {
                    "type": "string",
                    "description": "End date for the report (YYYY-MM-DD)."
                },
                "filter_type": {
                    "type": "string",
                    "description": "Optional filter (e.g., 'missed_calls', 'feedback_calls', 'reminders')."
                }
            },
            "required": ["from_date", "to_date"]
        }
    },

    {
        "name": "log_service_call_recording",
        "description": "Log call duration and recording link for a completed service call.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Name of the customer on the call."
                },
                "call_date": {
                    "type": "string",
                    "description": "Date of the call."
                },
                "call_duration": {
                    "type": "string",
                    "description": "Duration of the call (e.g., 03:12)."
                },
                "recording_url": {
                    "type": "string",
                    "description": "Secure URL for the recorded call audio."
                }
            },
            "required": ["customer_name", "call_date", "call_duration", "recording_url"]
        }
    }

]
