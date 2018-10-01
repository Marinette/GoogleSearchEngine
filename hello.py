from bottle import *

@route('/')
def hello():
    return '''<h1> Search </h1>
			  <form action = "/" method = "post">
					<input type = "text" name = "keywords" placeholder = "Enter search query"/>
					<input value = "Search" type="submit" />
			  </form>
    '''

@route('/', method='POST')
def display_word_count():
    query = request.forms.get("keywords")
    query = query.lower()
    word_list = query.split(" ")
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1

    printWordCounter = """<table> <tr> <th>Word</th> <th>Count</th> </tr>"""
    key_list = d.keys()
    for key in key_list:
        #print (key, d[key])
        print (key +"\t"+ str(d[key]))
        printWordCounter += ("<tr><td>" + key + "</td><td>" + str(d[key]) + "</td></tr>")

    #print (printWordCounter)

    return "%s"  %(printWordCounter)


run(host='localhost', port=8080, debug=True)
