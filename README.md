# Popular Movies Checker

This is a simple GUI application to assist users in checking popular movies for a specified year. 
The application uses **Tkinter** for the graphical user interface, **JSON** file for database management, and web scraping with **Beautiful Soup** and **Playwright** for data retrieval.

---

## Features
- **Check popular movies**: View a list of popular movies for a speciefied year. Displays a list in JSON format containg the movie name, type, duration, and genre.

---

## Prerequisites
- **Python** should be installed on your PC.

---

## Installation 

1. Clone the repository:
```
git clone https://github.com/Mariana-Oleinic/Odyssey_Homework_Project.git
```

2. Navigate to the project directory:
```
cd Odyssey_Homework_Project
```
3. Create and activate a virtual environment:

For Mac/Linux:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
For Windows:
```
python -m venv venv
```
```
.\venv\Scripts\activate  
```
4. Install the required Python dependencies:

For Mac/Linux:
```
pip3 install -r requirements.txt 
```
For Windows:
```
pip install -r requirements.txt 
```
5. Install the necessary browser binaries for Playwright to function:

For Mac/Linux/Windows:
```
playwright install
```

6. Run the application:

For Mac/Linux:
```
python3 app.py 
```
For Windows:
```
python app.py 
```

---

## Usage

1. Check Hot Offers:

- Enter a year.
- Click the "Check" button to view the list of popular movies for that year.
- **Note**: If an empty list is displayed as result, click Reset button, and try again.
---
