# Banking-Chatbot
Developed a banking chatbot which can guide a person with any banking queries. 

## ChatBot with interactive UI using simple web socket server 

### Description of files
* Chatbot_train.py file trains the data available in the data folder. Once it is trained , the result will be stored as db.sqlite.
* Chatbot.py uses this db.sqlite to generate responses for user queries.
* server.py sends back message to the client.

### setup
1) After cloning repo, CD into CHATBOT folder
    ``` cd chatbot ```

2) Install virtualenv if you have not before
    ``` pip install virtualenv ```

3) Initialiize virtualenv for the project
    ``` virtualenv -p python3 venv ```

4) Activate virtualenv
    ``` .\venv\Scripts\activate ```
    
5) Install requirement.txt
    ``` pip3 install -r .\requirement.txt ```

6) Install pandas separately (This is because of dependencies conflict between ChatterBot and Pandas):
    ``` pip install pandas  ```
    NOTE : ignore and error related to ```python-dateutil``` version conflict.

### How to run
1) Make sure virtualenv is activated
    ``` .\venv\Scripts\activate ```

2) Start server
    ``` python server.py ```

3) Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation and test.

