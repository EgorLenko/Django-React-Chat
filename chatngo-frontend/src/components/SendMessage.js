import React, { useState } from "react";
import PropTypes from "prop-types";
import styles from './style/SendMessage.module.css';

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
        socket.send(JSON.stringify(messageObject));
      }

      setMessage("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <div className={styles.formGroup}>
        <input
          type="text"
          placeholder="Type your message ->"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className={styles.formControl}
        />
      </div>
      <button type="submit" className={styles.btnPrimary}>
        Send -&gt;
      </button>
    </form>
  );
};

SendMessage.propTypes = {
  currentUser: PropTypes.string.isRequired,
  socket: PropTypes.instanceOf(WebSocket).isRequired,
};
export default SendMessage;