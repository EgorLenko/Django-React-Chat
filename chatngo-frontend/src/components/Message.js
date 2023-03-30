import React from "react";
import { Card } from "react-bootstrap";

const Message = ({ message, isCurrentUser }) => {
  return (
    <div className={`message ${isCurrentUser ? "currentUser" : ""}`}>
      <Card>
        <Card.Body>
          <Card.Title>{message.username}</Card.Title>
          <Card.Text>{message.message}</Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
};

export default Message;
