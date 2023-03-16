class ChatngoWebSocket {
    constructor(onMessage) {
      this.socket = new WebSocket("ws://localhost:8000/ws/chat/");
      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        onMessage(data);
      };
    }
  
    sendMessage(message) {
      this.socket.send(JSON.stringify(message));
    }
  }
  
  export default ChatngoWebSocket;