from flask import Flask, request, render_template
from waitress import serve
from paste.translogger import TransLogger
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

from Utility.autocomplete_sentence import AutcompleteSentence

from flask_cors  import CORS


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/')
def openchatbot():  # put application's code here
    return render_template('chatbot.html')

@app.route('/auto-complete', methods=['POST'])
def translate():
    body = request.get_json()
    sentence = body.get('sentence')
    context =  body.get('context')
    t = AutcompleteSentence(sentence,context)
    response = t.get_autcompleteSentence()
    return response


if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=8080)
    serve(TransLogger(app, setup_console_handler=False), host='127.0.0.1', port=8080)


    app.run()
