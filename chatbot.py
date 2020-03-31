from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd

import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import datetime

stop_words = set(stopwords.words('english'))
#print(stop_words)

def cleanup(sentence):




    word_tok = nltk.word_tokenize(sentence)
    stemmed_words = [w for w in word_tok if not w in stop_words]
    #print(stemmed_words)

    #stemmed_words = [stemmer.stem(w) for w in word_tok]



    return ' '.join(stemmed_words)


le = LE()

tfv = TfidfVectorizer(min_df=1, stop_words='english')

data = pd.read_csv("C:\\Users\\Rohit\\Desktop\\BankFAQs.csv")

questions = data['Question'].values

X = []

for question in questions:
    X.append(cleanup(question))



tfv.fit(X)
le.fit(data['Class'])

X = tfv.transform(X)

y = le.transform(data['Class'])

trainx, testx, trainy, testy = tts(X, y, test_size=.3, random_state=42)


model = SVC(kernel='linear')
model.fit(trainx, trainy)


class_=le.inverse_transform(model.predict(X))

#print("SVC:", model.score(testx, testy))


def get_max5(arr):
    ixarr = []
    for ix, el in enumerate(arr):
        ixarr.append((el, ix))


    ixarr.sort()

    ixs = []
    for i in ixarr[-5:]:

        ixs.append(i[1])

    return ixs[::-1]




def get_response(usrText):





    while True:











        if usrText.lower() == "bye":
            return "Bye"



        GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey","hiii","hii","yo"]

        a = [x.lower() for x in GREETING_INPUTS]

        sd=["Thanks","Welcome"]

        d = [x.lower() for x in sd]


        am=["OK"]

        c = [x.lower() for x in am]

       # ty = ["getting"]
       # r = [x.lower() for x in ty]



        t_usr = tfv.transform([cleanup(usrText.strip().lower())])
        class_ = le.inverse_transform(model.predict(t_usr))

        questionset = data[data['Class'].values == class_]

        cos_sims = []
        for question in questionset['Question']:
            sims = cosine_similarity(tfv.transform([question]), t_usr)

            cos_sims.append(sims)

        ind = cos_sims.index(max(cos_sims))

        b = [questionset.index[ind]]









        if usrText.lower() in a:

            return ("Hi, I'm Emily!\U0001F60A")


        if usrText.lower() in c:
            return "Ok...Alright!\U0001F64C"

        if usrText.lower() in d:
            return ("My pleasure! \U0001F607")



        if max(cos_sims) > [[0.]]:
            a = data['Answer'][questionset.index[ind]]+"   "
            return a


        elif max(cos_sims)==[[0.]]:
           return "sorry! \U0001F605"



def get_response2(usr):
    if usr.lower() == "bye":
        return "Thanks for having conversation! \U0001F60E"

    GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey","hii","hiii","hiiiii","yo","Hey there"]

    a = [x.lower() for x in GREETING_INPUTS]

    sd = ["Thanks", "Welcome"]

    d = [x.lower() for x in sd]

    am = ["OK"]

    c = [x.lower() for x in am]



    t_usr = tfv.transform([cleanup(usr.strip().lower())])
    class_ = le.inverse_transform(model.predict(t_usr))

    questionset = data[data['Class'].values == class_]

    cos_sims = []
    for question in questionset['Question']:
        sims = cosine_similarity(tfv.transform([question]), t_usr)

        cos_sims.append(sims)

    ind = cos_sims.index(max(cos_sims))

    b = [questionset.index[ind]]

    if usr.lower() in a:
        return ("you can ask me questions related to: Accounts, Investments, Funds, etc.")

    if usr.lower() in c:
        return " Cool! \U0001f604"

    if usr.lower() in d:
        return ("\U0001F44D")




    if max(cos_sims) == [[0.]]:
        return "I'm not able to solve this question at this moment. You can call to customer support 1860 999 9999 \U0001F615"

    if max(cos_sims) > [[0.]]:

        inds = get_max5(cos_sims)
        print(inds)

        b = "(1)" + data['Question'][questionset.index[0]]
        c = "(2)" + data['Question'][questionset.index[1]]
        d = "(3)" + data['Question'][questionset.index[2]]
        e = "(4)" + data['Question'][questionset.index[3]]
        f = "(5)" + data['Question'][questionset.index[4]]

        return "Following are the Recommended Questions----->" + b + c + d + e + f

