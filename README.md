☂️ Rain Alert System

🌟 Overview

    The Rain Alert System is a Python-based application that checks the weather forecast and sends a WhatsApp notification to inform you if it's likely to rain. This system integrates the OpenWeatherMap API for weather data and Twilio's WhatsApp API for messaging.

🛠 Features

    - Real-time weather monitoring: Retrieves weather forecasts based on your location.
    - Rain alert: Notifies you if rain is expected.
    - Custom messaging: Sends personalized WhatsApp messages for both rain and clear weather scenarios.
🎯 Why This Project?

    This project serves as a practical example of building automation tools that interact with APIs and send real-time notifications. It demonstrates:

    - How to use environment variables to secure sensitive API keys.
    - Integration of weather APIs for data retrieval.
    - Automation of WhatsApp notifications using Twilio.
📂 Project Structure

    .
    ├── main.py                # Main application logic
    ├── requirements.txt       # Dependencies
    └── README.md              # Project documentation
🔧 Setup Guide
    Prerequisites

        - Python 3.x installed.
        - API keys for:
            - OpenWeatherMap
            - Twilio
        - Twilio WhatsApp account for sending messages.
Installation
Clone this repository:

    git clone https://github.com/matanohana433/rain_alert.git
    cd rain_alert
Install dependencies:


    pip install -r requirements.txt
Configure environment variables: Create a .env file and add:

    OWM_API_KEY=your_openweathermap_api_key
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE=whatsapp:+14155238886
    MY_PHONE=whatsapp:+1234567890
🚀 Usage

1. Run the script:


    python main.py
What the script does:

    - Fetches the weather forecast for the specified location.
    - Checks for rain in the next forecast periods.
    - Sends a WhatsApp message with either:
        - "It's going to rain today. Remember to bring an umbrella ☂️"
        - "Sky looks clear have a nice day."
📊 Example Output

WhatsApp Notification
Rain Alert:

    It's going to rain today. Remember to bring an umbrella ☂️
Clear Weather Alert:

    Sky looks clear have a nice day.
🔍 Key Learnings

    - API Integration: Demonstrates the use of REST APIs for weather data.
    - Automation: Automates notification delivery with Twilio's WhatsApp API.
    - Secure Coding: Protects sensitive credentials with environment variables.
🤔 FAQs


    Q: How do I get my OpenWeatherMap API key?
    A: Sign up at OpenWeatherMap, and retrieve your API key from your account.
    Q: What is the free tier limit for Twilio?
    A: Twilio's free tier allows limited WhatsApp message sends. Upgrade your plan for higher limits.
🚀 Future Enhancements

    - Support for additional weather conditions (e.g., snow, storms).
    - Add user-configurable locations and notifications.
    - Implement error handling for API failures.
🤝 Contributing

    Contributions are welcome! Feel free to submit a pull request or open an issue.

📬 Contact
Have questions? Feel free to reach out:

    Email: matanohana433@gmail.com
    GitHub: matanohana433