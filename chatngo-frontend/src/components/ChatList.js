import React from "react";
import Message from "./Message";
import styles from './style/ChatList.module.css';

const ChatList = ({ chats }) => {
  return (
    <ul className={styles.listGroup}>
      {chats.map((message, index) => (
        <li key={index} className={styles.listGroupItem}>
          <Message message={message} isCurrentUser="currentUser" />
        </li>
      ))}
    </ul>
  );
};

export default ChatList;
