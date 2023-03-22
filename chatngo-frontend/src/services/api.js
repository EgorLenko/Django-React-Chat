import axios from "axios";

// Not Deprecated because of "Proxy" parameter in Package.js NOT WORKING!
const api = axios.create({
  baseURL: "http://localhost:8000/chat/api/", 
});

export default api;