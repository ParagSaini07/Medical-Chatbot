# Medical Chatbot

A medical chatbot that allows users to input one or more medical conditions and get medication, precautions, and diet suggestions tailored to each condition. The chatbot ensures that the suggested medications do not conflict with one another and also provides recommendations to prevent any possible side effects.

## Features
- **Multi-condition Handling**: Users can enter multiple medical conditions, and the chatbot will provide relevant medications, precautions, and diet suggestions for all of them.
- **Non-reactive Medications**: The chatbot suggests medications that do not react with each other.
- **Precautions and Diet**: The chatbot offers precautions and dietary advice based on the entered conditions.
- **Preventive Care**: The chatbot recommends preventive care options, such as vitamins and probiotics, to help avoid reactions between medications.

## Project Structure
/your_project_directory /app.py # Flask server code /templates/ /index.html # HTML for frontend


### Technologies Used:
- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript (AJAX)
- **Libraries**: 
  - `flask`: For handling web requests and serving the web interface.
  - `Jinja2`: For rendering HTML templates.

## Installation

1. Clone the repository:
   ```bash
   git clone  https://github.com/rkyadav3/Medical-Chatbot.git
2. Navigate to the project directory:
    ```bash
    cd medical-chatbot
3. Install the required dependencies:
   ```bash
    pip install flask
4. Run the Flask server:
    ```bash
    python app.py
5. Open your web browser and navigate to http://127.0.0.1:5000/.

## Usage

1. Go to the web interface where you can type one or more medical conditions (comma-separated).
2. Click the "Ask Chatbot" button.
3. The chatbot will display:
   - Medications for each condition.
   - Precautions to take.
   - Dietary advice.
   - Preventive medications to avoid any side effects.

### Example

- Enter conditions like: `fever, cold, headache`.
- The chatbot will respond with relevant medications, precautions, and dietary suggestions for all conditions without conflicting the medicines.

### Sample Conditions Supported

Here are some conditions supported by the chatbot:

- **Fever**
- **Cold**
- **Headache**
- **Cough**
- **Stomach Pain**
- **Diarrhea**
- **Constipation**
- **Hypertension**
- **Diabetes**
- **Asthma**
- **Allergies**
- **Migraine**
- **Acid Reflux**
- **Anxiety**
- **Depression**
- **Back Pain**
- **Skin Rash**
- **High Cholesterol**
- **Insomnia**
- **Arthritis**
- **Gout**
- **Anemia**
- **Sinusitis**

You can add more conditions as needed by updating the chatbot's condition dictionary.

### Future Enhancements

- **User Authentication**: Add login and user history for tracking previous medical conditions and treatments.
- **Medication Interaction Checking**: Use an external API or database to check for possible interactions between medications.
- **Expand Medical Knowledge**: Add more medical conditions and more detailed medication advice.

## Contributing
If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
3. Make your changes and commit them:
    ```bash
    git commit -m "Added new feature"
4. Push your changes:
    ```bash
    git push origin feature-branch
5. Open a Pull Request.


### License
This project is licensed under the MIT License. See the LICENSE file for details.







