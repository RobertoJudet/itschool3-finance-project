# Finance API

Final project for ItSchool course, Python - Intro To Programming.

For Windows, steps for deploy:
``````
git clone <git_repo_url> 
cd itschool3-finance-project
python3 -m venv env/
.\env\Scripts\activate 
pip install --upgrade pip
pip install -r requirements.txt

``````

This project uses FastAPI and uvicorn 
The project start from main.py file

This project offers the possibility to:
- create, edit and delete a user having a UUID format for regarding ID
- assign a ticker to a user
- have a history for a ticker (current price, historical price, price evolution, etc)
- have a sqlite database with users created and the details regarding
- have a historical charts

FastAPI docs: https://fastapi.tiangolo.com/