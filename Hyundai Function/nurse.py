import os
import pandas as pd
from difflib import get_close_matches
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the Excel file
data_path = 'data/Copy of LLM Sample Data_Phase 1.xlsx'
data = pd.ExcelFile(data_path)

# Mapping event types to intended sheet names
event_sheets = {
    "conference": "Conf. Iperson  Live",
    "webinar": "Conf. Live Webinar",
    "webcast": "Conf. Webcast",
    "journals": "Conf. Journals",
    "text-based": "Conf. Text based",
    "podcast": "Conf. Podcast"
}

# Additional sheets (if needed)
cme_df = data.parse('CME Credits')
specialty_df = data.parse('Professions & Specialties')

# Load Gemini API Key from .env
api_key = os.getenv("GOOGLE_API_KEY")

# Define a system prompt for fallback responses
system_prompt = (
    "You are a specialized medical event recommendation assistant. "
    "Answer solely using details available in the provided dataset. "
    "Do not provide generic responses outside the dataset context."
)

# AI Model Setup (fallback for non-dataset queries)
ai_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=api_key,
    google_api_key=api_key,
    verbose=True
)

def get_sheet(sheet_name):
    """
    Return the closest matching sheet name from the Excel file.
    """
    available = data.sheet_names
    if sheet_name in available:
        return sheet_name
    matches = get_close_matches(sheet_name, available, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    else:
        raise ValueError(f"Worksheet named '{sheet_name}' not found.")

def extract_city_from_text(query, df):
    """
    Extract a city name from the query by comparing with the 'City' column
    of the provided DataFrame.
    """
    if "City" not in df.columns:
        return None
    available_cities = df['City'].dropna().unique().tolist()
    available_cities_lower = [c.lower() for c in available_cities if isinstance(c, str)]
    query_lower = query.lower()
    for city in available_cities_lower:
        if city in query_lower:
            # Return the city name as stored in the dataset (case sensitive)
            for orig_city in available_cities:
                if orig_city.lower() == city:
                    return orig_city
    # Alternatively, use fuzzy matching:
    matches = get_close_matches(query_lower, available_cities_lower, n=1, cutoff=0.6)
    if matches:
        for orig_city in available_cities:
            if orig_city.lower() == matches[0]:
                return orig_city
    return None

def recommend_courses():
    # Standard recommendation session using CLI inputs.
    profession = input("Enter your profession (Doctor/Nurse/Physician): ").strip()
    domain = input("Enter your specialty (e.g., Cardiology, Neurology): ").strip()
    event_type = input("What do you want? (Conference, Webinar, Webcast, Journals, Text-based, Podcast): ").strip().lower()
    
    if event_type not in event_sheets:
        print("❌ Invalid event type. Please choose from the given options.")
        return
    
    try:
        sheet_to_use = get_sheet(event_sheets[event_type])
    except ValueError as e:
        print(e)
        return
    
    events_df = data.parse(sheet_to_use)
    events_df.fillna('', inplace=True)
    
    # For conferences, filter by location; for other types, filter by specialty.
    if event_type == "conference":
        country = input("Enter your country: ").strip()
        state = input("Enter your state: ").strip()
        city = input("Enter your city: ").strip()
        recommended = events_df[
            (events_df['Country'].str.contains(country, case=False)) &
            (events_df['State'].str.contains(state, case=False)) &
            (events_df['City'].str.contains(city, case=False))
        ]
    else:
        recommended = events_df[events_df['Specialty'].str.contains(domain, case=False)]
    
    if recommended.empty:
        print("\n❌ No Events Found for Your Criteria.")
        return
    
    print("\n✅ Recommended Events for s for You:\n")
    for _, row in recommended.iterrows():
        print(f"🎓 Title: {row['Title']}")
        print(f"📅 Start Date: {row.get('Start Date', 'N/A')}")
        print(f"📅 End Date: {row.get('End Date', 'N/A')}")
        print(f"📍 Location: {row.get('City', '')}, {row.get('State', '')}, {row.get('Country', '')}")
        print(f"📊 Event Type: {row.get('Event Type', 'N/A')}")
        print(f"👥 Target Audience: {row.get('Target Audience', 'N/A')}")
        print(f"💸 Price: {row.get('Price', 'N/A')}")
        print(f"🎓 CME Credits: {row.get('Credits', 'N/A')}")
        print(f"🔗 Conference URL: {row.get('Conference URL', 'N/A')}")
        print("--------------------------------------------------")