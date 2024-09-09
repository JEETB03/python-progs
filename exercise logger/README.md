

---

# 🏋️‍♂️ Exercise Logger

The **Exercise Logger** is a Python application that helps you log and track your exercise data in a Google Sheet. It utilizes the **Nutritionix API** to retrieve detailed exercise information based on your input and automatically records the data using the **Sheety API**. With this app, you can easily keep track of your workout sessions, including the type of exercise, duration, and calories burned.

## 💻 Technologies Used

- **Python**: Core language for the app.
- **Nutritionix API**: Fetches exercise details via natural language input.
- **Sheety API**: Sends the exercise data to a Google Sheet.
- **Requests Library**: For handling HTTP requests.
- **Datetime Module**: For formatting and retrieving current date and time.

## 🚀 Features

- Natural language input to log exercises (e.g., "Ran for 30 minutes").
- Automatically logs exercise details including name, duration, and calories burned.
- Data is recorded in a Google Spreadsheet via Sheety API.
- Easy to set up and use.

## 📋 Prerequisites

Before running the app, you need:

1. **Python 3.x** installed on your system.
2. **Nutritionix API credentials**: 
   - Get your **App ID** and **API Key** from [Nutritionix](https://www.nutritionix.com/business/api).
3. **Sheety API endpoint**: 
   - Set up a Google Sheet and integrate it with [Sheety](https://sheety.co/).
4. **Requests Library**: Install it by running:
   ```bash
   pip install requests
   ```

## ⚙️ Setup and Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/exercise-logger.git
   ```

2. Navigate to the project directory:
   ```bash
   cd exercise-logger
   ```

3. Install the necessary Python dependencies:
   ```bash
   pip install requests
   ```

4. Replace the placeholders in the script with your actual credentials:
   - **APP_ID** and **API_KEY** from Nutritionix.
   - **sheety_endpoint**: Your Sheety POST endpoint.
   - **Authorization**: Your Sheety Basic Auth token.

5. Run the script:
   ```bash
   python exercise_logger.py
   ```

## 📝 How It Works

1. The user inputs the exercise they performed (e.g., "Cycling for 20 minutes").
2. The script sends the input to the **Nutritionix API**, which returns the exercise name, duration, and calories burned.
3. The app retrieves the current date and time and formats them.
4. The data is sent to the **Sheety API**, logging the exercise details into your Google Spreadsheet.
5. A success message is printed with the logged data.

## 📊 Example

Here’s a sample interaction:

```bash
What exercise did you do today? Running for 20 minutes
{
    "workout": {
        "date": "08/09/2024",
        "time": "12:35:00",
        "exercise": "Running",
        "duration": 20,
        "calories": 180
    }
}
```

This data will then appear in your Google Sheet.

## 🛠️ API Integration Details

### Nutritionix API
- **Endpoint**: `/v2/natural/exercise`
- **Method**: POST
- **Headers**:
  - `x-app-id`: Your Nutritionix App ID.
  - `x-app-key`: Your Nutritionix API Key.
  - `Content-Type`: `application/json`
- **Body**:
  - `"query"`: A natural language string (e.g., "Ran for 30 minutes").

### Sheety API
- **Endpoint**: Your Sheety Google Sheet POST URL.
- **Method**: POST
- **Headers**:
  - `Authorization`: Your Sheety Basic Auth token.

## 🚨 Error Handling

Make sure to:
- Handle invalid API credentials properly.
- Ensure valid responses from the Nutritionix API.
- Consider potential API rate limits.



---

### 📣 Contribute
Feel free to open issues or submit pull requests for improvements!

---

Now, your **Exercise Logger** is all set up and ready to help you keep track of your workouts! 💪

--- 

