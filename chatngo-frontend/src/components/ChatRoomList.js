import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";
import styles from './style/ChatRoomList.module.css';

const ChatRoomList = () => {
  const [rooms, setRooms] = useState([]);

  useEffect(() => {
    async function fetchRooms() {
      try {
        const response = await api.get("rooms");
        setRooms(response.data);
      } catch (error) {
        console.error("Error fetching chat rooms:", error);
      }
    }

    fetchRooms();
  }, []);

  return (
    <ul className={styles.listGroup}>
      {rooms.map((room) => (
        <li key={room.id} className={styles.listGroupItem}>
          {room.name}
          <Link
            to={`/chat/${room.id}`}
            className={styles.btnPrimary}
          >
            Join &ldquo;{room.name}&rdquo;
          </Link>
        </li>
      ))}
    </ul>
  );
};

export default ChatRoomList;
