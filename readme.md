## Overview

This project automates the retrieval of flashcard data (favorites) from Reverso using Selenium with an existing Chrome session, then processes the resulting JSON to display question-answer pairs in the console.

## Requirements
Python 3.8+ (earlier versions may work, but are untested)
Google Chrome installed
ChromeDriver compatible with your installed Chrome version
Selenium library:
bash
Copy
Edit
pip install selenium
json and html are standard libraries in Python 3, so no separate installation needed.
Files
selenium_scrape.py: Contains the scrape_flashcards function that launches Chrome with your existing profile and navigates to Reverso favorites pages.
json_processing.py: Uses scrape_flashcards to retrieve JSON data, parse it, and display output in the terminal.
## Setup
Close all running Chrome instances. The selenium_scrape.py script accesses your Default Chrome profile. Running Chrome on the same profile while Selenium is also using it can cause conflicts.

Verify the Chrome profile path in selenium_scrape.py:

By default, it points to
sql
Copy
Edit
C:\Users\PC\AppData\Local\Google\Chrome\User Data
and the PROFILE_DIR is set to "Default".
If you use a different Windows username or a different Chrome profile, update these values in the code accordingly.
Make sure ChromeDriver is installed and is on your system path (or specify its location). Download ChromeDriver here and ensure it matches your Chrome browser version.

## Usage
Run the script json_processing.py:

bash
Copy
Edit
python json_processing.py
You will be prompted to choose flashcard options:

Press ENTER for English
Press 1 for Dutch (NL)
Press 0 for ALL
After you make a choice, the script will:

Call scrape_flashcards to load each relevant “favorites” page from Reverso.
Parse the returned JSON.
Print out the question-answer pairs in the terminal.
If the script encounters a 403 Forbidden, it will attempt to visit the Reverso "Manage" account page to re-authenticate and then try again.
