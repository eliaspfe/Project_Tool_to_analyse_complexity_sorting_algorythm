# Tool to analyse the complexity of Algorithms
This project was created as part of the lecture “Theoretical Computer Science” at the DHBW.
The implemented tool helps to analyze and determine the Big O notation (time and space complexity) for algorithms in any programming language. It offers a user friendly GUI, allowing you to quickly evaluate your code.

## Table of Contents
1. Features
2. Getting Started
3. Usage of the Tool
4. Troubleshooting
5. Testing

## Features
- **Supports multiple languages:** Analyze algorithms written in various programming languages.
- **Big O Notation Calculation:** Automatically determine the time and space complexity of algorithms.
- **GUI:** graphical user interface to make it easy accessible for non technical users.
- **Communication with OpenAI:** The Tool communicates with the OpenAI API to access the LLMs provided by OpenAI.
- **Chat History:** The Langchain Framework provides features like chat History, that gives the LLM the ability to react to previously sent requests.

## Getting Started
- python version: 3.12.2
### 1. Clone the Repository
Clone the project to your local Computer by pasting this command into the terminal: `git clone https://github.com/eliaspfe/Project_Tool_to_analyse_complexity_sorting_algorythm.git`
### 2. Create virtual Environement
- Unix/MacOS `python3 -m venv .venv`
- Windows `py -m venv .venv`
### 3. Activate virtual Environement
- Unix/MacOs `source .venv/bin/activate`
- Windows `.venv\Scripts\activate`
### 4. Install required Packages
- `pip install -r requirements.txt`
### 5. Create .env file from template
- Create a file named `.env`
- Paste the text from `env_template.txt` into the `.env`file
- Change the API Key inside the `.env` file
### 6. Run the GUI
To run the Tool run the `GUI.py` file.

## Usage of the Tool
- **Example Buttons:** Use the buttons at the top to paste some exmaple algorithms into the code field.
- **Code field:** The Code field can be used to paste in your own code
- **Calculate Button:** The Calculate button is used to start an API request. It takes the Code from the Code field as Input for the LLM.
- **Clear Code Button:** This button clears the Code field.

## Troubleshooting
- **Missing API Key:** Ensure that your `.env` file is correctly set up with a valid API key.
- **Dependency Issues:** If packages are missing, try re-running `pip install -r requirements.txt`.
- **Wrong Python version:** Make sure you are using the right version of python (version 3.12.2 should work fine).

## Testing
The implemented Test `Test_procedure.py` is there to test the quality of the system prompt and shows how well the LLM can determine space- and time-complexity of certain algorithms.