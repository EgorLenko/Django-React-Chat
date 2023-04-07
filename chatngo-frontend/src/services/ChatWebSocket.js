import { io } from 'socket.io-client';

class ChatWebSocket {
  constructor(chatroomId, onMessage) {
    this.socket = io(`http://localhost:8000`, {
      path: '/ws',
      query: {
        chatroomId,
      },
    });

    this.socket.on('connect', () => {
      console.log('Connected to the server');
    });

    this.socket.on('message', (data) => {
      onMessage(data);
    });

    this.socket.on('disconnect', () => {
      console.log('Disconnected from the server');
    });
  }

  sendMessage(message) {
    this.socket.emit('message', message);
  }

  close() {
    this.socket.disconnect();
  }
}

export default ChatWebSocket;