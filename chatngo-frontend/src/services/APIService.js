import axios from 'axios';

class APIService {
  constructor() {
    this.api = axios.create({
      baseURL: 'http://localhost:8000/chat/api/',
    });
  }

  async getRooms() {
    try {
      const response = await this.api.get('rooms');
      return response.data;
    } catch (error) {
      console.error('Error fetching chat rooms:', error);
      return [];
    }
  }

  async createRoom(roomName) {
    try {
      const response = await this.api.post('rooms', { name: roomName });
      return response.data;
    } catch (error) {
      console.error(`Error creating chat room <${roomName}>:`, error);
      return null;
    }
  }

}

const apiService = new APIService();
export default apiService;
