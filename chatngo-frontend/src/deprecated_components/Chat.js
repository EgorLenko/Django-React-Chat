import React, { useState, useEffect } from "react";
import ChatList from "../components/ChatList";
import SendMessage from "../components/SendMessage";
import Message from "../components/Message";
import { Container, Row, Col } from "react-bootstrap";
import api from "../services/api";
import ChatWebSocket from "../services/ChatngoWebSocket";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [ws, setWs] = useState(null);

  useEffect(() => {
    const fetchMessages = async () => {
      const response = await api.get("messages/");
      setMessages(response.data);
    };

    fetchMessages();

    const websocket = new ChatWebSocket((message) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    setWs(websocket);

    return () => {
      websocket.socket.close();
    };
  }, []);

  const handleSendMessage = (message) => {
    ws.sendMessage(message);
  };

  return (
    <Container>
      <Row>
        <Col md={3}>
          <ChatList />
        </Col>
        <Col md={9}>
          <div>
            {messages.map((message, index) => (
              <Message key={index} message={message} />
            ))}
          </div>
          <SendMessage onSendMessage={handleSendMessage} />
        </Col>
      </Row>
    </Container>
  );
}

export default Chat;