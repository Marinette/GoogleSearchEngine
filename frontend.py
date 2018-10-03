from bottle import *

history = dict()

@route('/')
def hello():
    output = template('homepage.tpl')
    return output

@route('/', method='POST')

def display_word_count():
    query = request.forms.get("keywords")
    query = query.lower()
    word_list = query.split(" ")
    d = dict()
    #history = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
        history[word] = history.get(word, 0) + 1

    #new_history = [(v, k) for k, v in history.items()]
    #new_history.sort()
    #new_history.reverse()             # so largest is first
    #new_history = [(k, v) for v, k in new_history]

    new_history = sorted(history, key=history.get, reverse=True)

    printWordCounter = """<table name = "results" class = "counter" text-align: center> <tr> <th>Word</th> <th>Count</th> </tr>"""
    printHistoryCounter = """<table name = "history" class = "historyt" text-align: center> <tr> <th>Word</th> <th>Count</th> </tr>"""

    key_list = d.keys()
    #key_list2 = new_history.keys()
    for key in key_list:
        #print (key, d[key])
        #print (key +"\t"+ str(d[key]))
        printWordCounter += ("<tr><td>" + key + "</td><td>" + str(d[key]) + "</td></tr>")
    count = 0;
    for key in new_history:
        if count == 20:
            break
        printHistoryCounter += ("<tr><td>" + key + "</td><td>" + str(history[key]) + "</td></tr>")
        count += 1
    #print (printWordCounter)

    return "%s \n \n  %s"  %(printWordCounter, printHistoryCounter)


run(host='localhost', port=8080, debug=True)
