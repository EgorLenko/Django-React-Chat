import React from "react";
import PropTypes from 'prop-types';
import styles from './style/Message.module.css';

const Message = ({ message, isCurrentUser }) => {
  return (
    <div className={`${styles.message} ${isCurrentUser ? styles.currentUser : ''}`}>
      <div className={styles.card}>
        <div className={styles.cardBody}>
          <h5 className={styles.cardTitle}>{message.username}</h5>
          <p className={styles.cardText}>{message.message}</p>
        </div>
      </div>
    </div>
  );
};

Message.propTypes = {
  message: PropTypes.shape({
    username: PropTypes.string.isRequired,
    message: PropTypes.string.isRequired,
  }).isRequired,
  isCurrentUser: PropTypes.bool.isRequired,
};

export default Message;