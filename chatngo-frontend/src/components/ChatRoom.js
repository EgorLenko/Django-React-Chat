import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
// import { Container } from "react-bootstrap";
import Message from "./Message";
import SendMessage from "./SendMessage";
import { Button } from "react-bootstrap";

const ChatRoom = ({ currentUser }) => {
  const { roomId } = useParams();
  const navigate = useNavigate();
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const newSocket = new WebSocket(`ws://localhost:8000/ws/chat/${roomId}/`);
    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [roomId]);

  useEffect(() => {
    if (!socket) return;
    socket.onmessage = (event) => {
      const newMessage = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    };
  }, [socket]);

  const handleLeaveRoom = () => {
    if (socket) {
      socket.close();
      setSocket(null);
    }
    navigate("/");
  };

  return (
    <div className="chat-room">
      <div className="messages-container">
        {messages.map((message, index) => (
          <Message
            key={index}
            message={message}
            isCurrentUser={message.username === currentUser}
          />
        ))}
      </div>
      <SendMessage currentUser={currentUser} socket={socket} />
      <Button variant="danger" onClick={handleLeaveRoom}>
        Leave Room
      </Button>
    </div>
  );
};

export default ChatRoom;
