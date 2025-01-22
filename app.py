from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Mensaje recibido: {msg['message']} de {msg['username']}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5001, debug=True)
