# Banking-Chatbot
Developed a banking chatbot which can guide a person with any banking queries. 

## ChatBot with interactive UI using simple web socket server 
### Description of files
* Chatbot_train.py file trains the data available in the data folder. Once it is trained , the result will be stored as db.sqlite.
* Chatbot.py uses this db.sqlite to generate responses for user queries.
* server.py sends back message to the client.

### setup
1) after cloning repo, CD into CHATBOT folder
    -> cd chatbot

2) install virtualenv if you have not before
    -> pip install virtualenv

3) initialiize virtualenv for the project
    ->virtualenv -p python3 venv

4) activate virtualenv
    ->.\venv\Scripts\activate
    
5) install requirement.txt
    -> pip3 install -r .\requirement.txt

### How to run
1) make sure virtualenv is activated
    ->.\venv\Scripts\activate

2) start server
    -> python server.py

3) Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation and test.

