import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ChatRoom from "./components/ChatRoom";
import ChatRoomList from "./components/ChatRoomList";
import Login from "./components/Login";

const App = () => {
  const [currentUser, setCurrentUser] = useState(null);
  const [token, setToken] = useState(null);

  const handleLogin = (username, token) => {
    setCurrentUser(username);
    setToken(token);
  };

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route
          path="/"
          element={
            currentUser ? <ChatRoomList currentUser={currentUser} /> : <Login onLogin={handleLogin} />
          }
        />
        <Route
          path="/chat/:roomId"
          element={currentUser ? <ChatRoom currentUser={currentUser} /> : <Login onLogin={handleLogin} />}
        />
      </Routes>
    </Router>
  );
};

export default App;
