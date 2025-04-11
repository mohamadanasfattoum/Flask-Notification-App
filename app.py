from flask import Flask, render_template
from flask_socketio import SocketIO , emit


app = Flask(__name__)
socketio = SocketIO(app) # run flask as parameter in SocketIo 


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_notification') # event name
def handel_notification(message):
    emit('new_notification',{'message':message},broadcast=True) # broadcast : für alle
    

if __name__ == '__main__':
    socketio.run(app,debug=True)