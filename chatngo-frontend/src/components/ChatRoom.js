import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import PropTypes from "prop-types";
import Message from "./Message";
import SendMessage from "./SendMessage";
import styles from './style/ChatRoom.module.css';

const ChatRoom = ({ currentUser }) => {
  const { roomId } = useParams();
  const navigate = useNavigate();
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const newSocket = new WebSocket(`ws://localhost:8000/ws/chat/${roomId}/`);
    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [roomId]);

  useEffect(() => {
    if (!socket) return;
    socket.onmessage = (event) => {
      const newMessage = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    };
  }, [socket]);

  const handleLeaveRoom = () => {
    if (socket) {
      socket.close();
      setSocket(null);
    }
    navigate("/");
  };

  return (
    <div className={styles.chatRoom}>
      <div className={styles.messagesContainer}>
        {messages.map((message, index) => (
          <Message
            key={index}
            message={message}
            isCurrentUser={message.username === currentUser}
          />
        ))}
      </div>
      <SendMessage currentUser={currentUser} socket={socket} />
      <button className={styles.leaveRoomBtn} onClick={handleLeaveRoom}>
        Leave Room
      </button>
    </div>
  );
};

ChatRoom.propTypes = {
  currentUser: PropTypes.string.isRequired,
};
export default ChatRoom;
