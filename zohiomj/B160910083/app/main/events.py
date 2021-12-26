from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('joined', namespace='/chat')
def joined(message):
    #Орон зайд орж ирсэнийг нь мэдээллэх
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' орон зайд орж ирлээ'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    #Орон зайд мсж бичсэнийг бүх хүнд мэдээллэх
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    #Орон зайгаас гарсныг мэдээллэх
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' орон зайгаас гарлаа.'}, room=room)

