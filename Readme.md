# 🌧️ Rain Alert – Weather Notification System

A Python-based weather monitoring application that checks upcoming weather forecasts and automatically sends SMS notifications when rain is expected.

Built as part of **Day 35 of Angela Yu's 100 Days of Code – The Complete Python Pro Bootcamp**.

## 🚀 Project Overview

Rain Alert is an automated weather notification system that uses the OpenWeatherMap API to retrieve weather forecast data for a specified location.

The application analyzes upcoming weather conditions and checks whether rain is expected.

If rain is detected, it uses the Twilio API to send an SMS notification reminding the user to carry an umbrella.

## ✨ Features

- 🌦️ Retrieves weather forecast data
- 🌐 Integrates with OpenWeatherMap API
- 🔐 Secure API key management
- ☔ Automatically detects rainy weather conditions
- 📊 Processes JSON API responses
- ⚙️ Uses environment variables for credentials
- 🤖 Automates weather alerts

## 🛠️ Technologies Used

- Python
- Requests
- OpenWeatherMap API
- JSON
- Environment Variables
- os module

## 🌐 APIs Used

### 1. OpenWeatherMap API

Used to retrieve weather forecast information based on geographical coordinates.


## ⚙️ How It Works

1. The application retrieves weather forecast data from OpenWeatherMap.
2. API credentials are accessed securely through environment variables.
3. The program processes the JSON response.
4. It checks upcoming weather conditions using weather condition IDs.
5. If rain is expected, the application triggers an notification.

## 🔐 Environment Variables

The project uses environment variables to protect sensitive information.

Example configuration:

```env
OPENWEATHER_API_KEY=your_api_key
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

Never upload your actual API keys, authentication tokens, or personal credentials to GitHub.

Add `.env` to your `.gitignore` file.

## 📂 Project Structure

```text
Rain-Alert/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the project folder

```bash
cd YOUR-REPOSITORY
```

### 3. Install dependencies

```bash
pip install requests twilio python-dotenv
```

### 4. Configure environment variables

Create a `.env` file and add your OpenWeatherMap and Twilio credentials.

### 5. Run the application

```bash
python main.py
```

## 🎯 Learning Objectives

This project helped me understand:

- API keys and authentication
- Environment variables
- Secure credential management
- HTTP requests
- JSON data processing
- Weather API integration
- Python list slicing
- Conditional statements
- Automation using external APIs

## 🔮 Future Improvements

- 📍 Automatically detect user location
- 🌍 Support multiple locations
- 📱 Add WhatsApp notifications
- 📧 Add email alerts
- ⏰ Schedule automatic weather checks
- 🌡️ Include temperature and weather summaries
- 🖥️ Develop a graphical user interface
- 📊 Display weather forecast statistics

## 👨‍💻 Author

**Akash**

Engineering Student | Python Learner | AI & Data Science Enthusiast

## 📚 Course

100 Days of Code – The Complete Python Pro Bootcamp

Instructor: Angela Yu

**Day 35 – Keys, Authentication & Environment Variables: Send SMS**

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!