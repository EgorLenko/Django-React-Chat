import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";

const SendMessage = ({ onSendMessage }) => {
  const [message, setMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    if (message.trim() !== "") {
      onSendMessage(message);
      setMessage("");
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="message">
        <Form.Control
          type="text"
          placeholder="Type your message ->"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Send ->
      </Button>
    </Form>
  );
};

export default SendMessage;