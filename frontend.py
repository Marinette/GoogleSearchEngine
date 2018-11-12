from bottle import *
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import httplib2
import redis
import json
import yaml
import ast

#-------------------- Beaker Stuff ---------------------------------------------
import bottle
from beaker.middleware import SessionMiddleware

read_file = open('dump.json', 'r')
data = json.load(read_file)
read_file.close()

page_ranks = data[0]['pageranks']
inverted_index = data[0]['invertedIndex']
document_index = data[0]['documentIndex']
lexicons = data[0]['lexicon']

inverted_index = inverted_index.replace("set(", "")
inverted_index = inverted_index.replace(")", "")

lexicons = yaml.load(lexicons)
inverted_index = ast.literal_eval(inverted_index)
document_index = ast.literal_eval(document_index)
page_ranks = ast.literal_eval(page_ranks)

#print(type(page_ranks))
#print(type(document_index))
#print(type(inverted_index))
#print(inverted_index)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True
}
#request handler
sessionApp = SessionMiddleware(bottle.app(), session_opts)
#-------------------Beaker End--------------------------------------------------

##-------------GLOBAL VARIABLES FOR HOMEPAGE----------------------------------##
history_counter = """ """
word_counter = """ """
history = dict()
query = ""

pageranked_urls = []

PER_PAGE = 5

num_pages = 0
## ---------------------------------------------------------------------------##

#------------------- R O U T E S ----------------------------------------------#
#------------------------------------------------------------------------------#
@route('/', 'GET')
def homepage():
    output = 0
    session = request.environ.get('beaker.session')
    print (session)

    try: # Check logged in info
        email = session['email']
        profilePicture = session['picture']
        userName = session['name']
        output = template('homepage.tpl', history = "Top 20 Words", table = history_counter, profilePicture = profilePicture , Name = userName, Email = email)
    except: # runs if no login info
        output = template('homepageanon.tpl')

    return output

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

@error(404)
def error404(error):
    output = template('error.tpl')
    return output

@route('/search', method='POST')
def search_keyword():
    # get input string/keywords
    global query
    query = request.forms.get("keywords")
    query_lower = query.lower()
    # split the string and create a list of all words in string
    word_list = query_lower.split(" ")
    # dictionary to store word count

    global lexicons
    global inverted_index
    global document_index
    global page_ranks

    # get search results
    key_word = word_list[0]
    urls = []
    global pageranked_urls
    pageranked_urls = []

    key_word = "u'" + key_word + "'"

    if key_word in lexicons:
        key_word_value = lexicons[key_word]
        url_id_list = inverted_index[key_word_value]
        for url, url_id in document_index.items():
            if url_id in url_id_list:
                urls.append(url)
        for pr, rank in page_ranks:
            if pr in urls:
                pageranked_urls.append(pr)

    key_word = word_list[0]

    d = dict()
    global history
    global word_counter
    # stores word count and word history in dictionaries
    for word in word_list:
        d[word] = d.get(word, 0) + 1
        history[word] = history.get(word, 0) + 1
    # list of words storted in descending order based on values
    new_history = sorted(history, key=history.get, reverse=True)
    # word count html table
    word_counter = """<table class="table table-bordered one-edge-shadow" name = /"results/"> <tr> <th>Word</th> <th>Count</th> </tr>"""
    # updating word history html table
    global history_counter
    history_counter = """<table class="table table-bordered one-edge-shadow" name = /"history/"> <tr> <th>Word</th> <th>Count</th> </tr>"""
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

    """session = request.environ.get('beaker.session')
    output = 0;
    # Check logged in info
    try:
        profilePicture = session['picture']
        userName = session['name']
        email = session['email']
        output = template('table.tpl', keyword = query, table = word_counter, profilePicture = profilePicture, Name = userName, Email = email)
    except: # runs if no login info
        output = template('tableAnon.tpl', keyword = query, table = word_counter, url_table = url_counter)
    return output"""

    rd = ("/search/%s/1" %(key_word))
    redirect(rd)

@route("/search//<page>")
@route("/search/<keyword>/<page>")
def pagination(keyword="nothing", page = '1'):

    global history_counter
    global word_counter
    global pageranked_urls
    global query

    page = int(page)

    global PER_PAGE
    start = (page - 1) * PER_PAGE
    end = page * PER_PAGE

    parameters = {
            'page': page,
            'keyword': keyword,
            'query': query,
            'pageranked_urls': pageranked_urls,
            'start': start,
            'end': end,
            }

    session = request.environ.get('beaker.session')
    output = 0;
    # Check logged in info
    try:
        profilePicture = session['picture']
        userName = session['name']
        email = session['email']
        output = template('pagination.tpl', key_word = query, table = word_counter, profilePicture = profilePicture, Name = userName, Email = email, **parameters)
    except: # runs if no login info
        output = template('paginationAnon.tpl', key_word = query, table = word_counter, **parameters)
    return output

@route('/login')
def logIn():
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

    saveSession(user_document)
    # after successfully entering information, redirect to the home page
    redirect('/')

@route('/logout')
def logout():
    session = request.environ.get('beaker.session')
    session.delete()
    redirect('/')

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
## ------Functions-------------------------------------------------------------
#Function saves the session information
def saveSession(user_document):
        #save session
        print (user_document) # checks the keys for user doc
        session = request.environ.get('beaker.session')
        try:
            if user_document['name'] is '':
                session['name'] = 'Acrobatic Armadillo'
            else:
                session['name'] = user_document['name']
        except:
            session['name'] = ""
        try:
            session['email'] = user_email
        except:
            session['email'] = ""
        try:
            session['picture'] = user_document['picture']
        except:
            session['picture'] = "https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg?auto=compress&cs=tinysrgb&h=350"

        session.save()
        print ("/redirect: session ", session)



#run the app
bottle.run(app=sessionApp)
