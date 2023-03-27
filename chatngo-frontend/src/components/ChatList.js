import React from "react";
// import PropTypes from 'prop-types';
import { ListGroup } from "react-bootstrap";
import Message from "./Message";


const ChatList = ({ chats }) => {
  return (
    <ListGroup>
      {chats.map((message, index) => (
        <ListGroup.Item key={index}>
          <Message key={index} message={message} isCurrentUser='currentUser'/>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};  

export default ChatList;