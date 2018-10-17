from bottle import *
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import httplib2

@route('/', 'GET')
def home():
    flow = flow_from_clientsecrets("client_secret_346297252987-gessg0ftmins8qrsdkkh8lgv9ask1occ.apps.googleusercontent.com.json", scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email', redirect_uri = "http://localhost:8080/redirect")
    uri = flow.step1_get_authorize_url()
    redirect(str(uri))

@route('/redirect')
def redirect_page():
    code = request.query.get('code','')
    flow = OAuth2WebServerFlow(client_id="346297252987-gessg0ftmins8qrsdkkh8lgv9ask1occ.apps.googleusercontent.com", client_secret = "oJVewakqwN7qzgX7J4Xh889P", scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email', redirect_uri = "http://localhost:8080/redirect")
    credentials = flow.step2_exchange(code)
    token = credentials.id_token['sub']

    http = httplib2.Http()
    http = credentials.authorize(http)

    #get user email
    users_service = build('oauth2','v2', http=http)
    user_document = users_service.userinfo().get().execute()
    user_email = user_document['email']



# global variables for keyword history
history_counter = """ """
top = """ """
history = dict()

def homepage():
    output = template('homepage.tpl', history = top, table = history_counter)
    return output

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

@route('/search', method='POST')
def display_word_count():
    # get input string/keywords
    query = request.forms.get("keywords")
    query_lower = query.lower()
    # split the string and create a list of all words in string
    word_list = query_lower.split(" ")
    # dictionary to store word count
    d = dict()
    global history
    # stores word count and word history in dictionaries
    for word in word_list:
        d[word] = d.get(word, 0) + 1
        history[word] = history.get(word, 0) + 1
    # list of words storted in descending order based on values
    new_history = sorted(history, key=history.get, reverse=True)
    # word count html table
    word_counter = """<table name = /"results/"> <tr> <th>Word</th> <th>Count</th> </tr>"""
    # updating word history html table
    global history_counter
    global top
    history_counter = """<table name = /"history/"> <tr> <th>Word</th> <th>Count</th> </tr>"""
    top = """ <h4> Top 20 Keywords </h4> """
    # updating word count table
    key_list = d.keys()
    count = 0
    for key in key_list:
        word_counter += ("<tr><td>" + key + "</td><td>" + str(d[key]) + "</td></tr>")
        count += 1
    if count == 1:
        word_counter = """ """
    # updating word history html table with top 20 keywords
    count = 0
    for key in new_history:
        if count == 20:
            break
        history_counter += ("<tr><td>" + key + "</td><td>" + str(history[key]) + "</td></tr>")
        count += 1

    table_output = template('table.tpl', keyword = query, table = word_counter)

    return table_output


run(host='localhost', port=8080, debug=True)
#run(host='0.0.0.0', port=8080)
#http://your_ip:8080/
