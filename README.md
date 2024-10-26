# Text Generation Bot

This project is a simple text generation chatbot web application built with Streamlit that utilizes the GPT-2 model for text generation. Users can input a text prompt and receive generated text based on their input. 

## Technologies Used

- [Streamlit](https://streamlit.io/) - A framework for building web applications in Python.
- [Transformers](https://huggingface.co/transformers/) - A library for state-of-the-art natural language processing.

---

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-generation-bot.git
   cd text-generation-bot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
  - On Windows
     ```bash
     venv\Scripts\activate
     ```
  - On Linux/MacOS
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
    ```bash
    pip install streamlit transformers
    ```

5. Run the application:
    ```bash
    streamlit run app.py
    ```

6. Open your web browser and go to http://localhost:8501 to access the app.


---

## Usage

1. Enter your text prompt in the provided text area. For example:
  ```sql
  As the sun set over the horizon, the explorers gathered around the campfire and shared tales of their latest adventure. One of them said,
  ```
2. Click the "Generate Text" button.
   
4. The generated text will be displayed below the button.

## Screenshots

![image](https://github.com/user-attachments/assets/2c155c01-c603-4bac-bfd7-24b2cc5349aa)
![image](https://github.com/user-attachments/assets/716872d5-f182-46fd-a233-8edf63e3b044)


