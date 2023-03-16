import React from "react";
import { ListGroup } from "react-bootstrap";

const ChatList = ({ chats }) => {
  return (
    <ListGroup>
      {chats.map((chat, index) => (
        <ListGroup.Item key={index}>
          {chat.username}: {chat.message}
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default ChatList;