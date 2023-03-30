import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import PropTypes from "prop-types";

const SendMessage = ({ currentUser, socket }) => {
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      const messageObject = {
        message: message.trim(),
        username: currentUser,
      };

      if (socket.readyState === WebSocket.OPEN) {
        // console.log(JSON.stringify(messageObject));
        socket.send(JSON.stringify(messageObject));
      }

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
        Send -&gt;
      </Button>
    </Form>
  );
};

SendMessage.propTypes = {
  currentUser: PropTypes.string.isRequired,
  socket: PropTypes.instanceOf(WebSocket).isRequired,
};
export default SendMessage;
