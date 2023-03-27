import React, { useState, useEffect } from "react";
import { ListGroup, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import api from "../services/api";

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
    <ListGroup>
      {rooms.map((room) => (
        <ListGroup.Item key={room.id}>
          {room.name}
          <Link
            to={`/chat/${room.id}`}
            className="btn btn-primary"
            style={{ marginLeft: "10px" }}
          >
            Join &ldquo;{room.name}&rdquo;
          </Link>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default ChatRoomList;
