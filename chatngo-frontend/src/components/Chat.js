import React, { useState, useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap";
import ChatList from "./ChatList";
import SendMessage from "./SendMessage";
import ChatngoWebSocket from "../services/ChatngoWebSocket";

const Chat = () => {
  const [messages, setMessages] = useState([]);

  const addMessage = (message) => {
    setMessages((prevMessages) => [...prevMessages, message]);
  };

  const chatSocket = React.useRef(null);

  useEffect(() => {
    chatSocket.current = new ChatngoWebSocket(addMessage);
    return () => {
      chatSocket.current.socket.close();
    };
  }, []);

  const sendMessage = (message) => {
    const messageData = {
      text: message,
      timestamp: new Date().toISOString(),
      // TODO: Add metadata
    };
    chatSocket.current.SendMessage(messageData);
    addMessage(messageData);
  };

  return (
    <Container>
      <Row>
        <Col>
          <h1>Chat</h1>
          <ChatList chats={messages} />
          <SendMessage onSendMessage={sendMessage} />
        </Col>
      </Row>
    </Container>
  );
};

export default Chat;