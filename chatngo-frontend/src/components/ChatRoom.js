import React, { useState, useEffect } from "react";
import { Container, Button, Form, InputGroup } from "react-bootstrap";
import { useParams, useNavigate } from "react-router-dom";
import io from "socket.io-client";

const ChatRoom = () => {
  const { roomId } = useParams();
  const navigate = useNavigate();
  const [socket, setSocket] = useState(null);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const newSocket = io("http://localhost:8000", {
      path: `/ws/chat/${roomId}/`,
      // query: { roomId },
    });
    setSocket(newSocket);

    return () => {
      newSocket.disconnect();
    };
  }, [roomId]);

  useEffect(() => {
    if (!socket) return;
    socket.on("message", (newMessage) => {
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    });
  }, [socket]);

  const handleSendMessage = (event) => {
    event.preventDefault();
    if (message.trim()) {
      socket.emit("send_message", message);
      setMessage("");
    }
  };

  const handleLeaveRoom = () => {
    if (socket) {
      socket.disconnect();
      setSocket(null);
    }
    navigate("/");
  };

  return (
    <Container>
      <div className="chat-room">
        {/* Display chat messages */}
        {messages.map((msg, index) => (
          <div key={index}>{msg}</div>
        ))}

        {/* Input for sending messages */}
        <Form onSubmit={handleSendMessage}>
        <InputGroup>
            <Form.Control
              type="text"
              placeholder="Type your message here"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
            />
            <InputGroup.Append>
              <Button type="submit">Send</Button>
            </InputGroup.Append>
          </InputGroup>
        </Form>
      </div>
      <Button variant="danger" onClick={handleLeaveRoom}>
        Leave Room
      </Button>
    </Container>
  );
};

export default ChatRoom;
