const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://surakshapath-backend.onrender.com/api'  // We'll deploy the backend to Render
  : 'http://localhost:5000/api';

export const API_ENDPOINTS = {
  alerts: `${API_BASE_URL}/alerts`,
  news: `${API_BASE_URL}/news`,
  // Add other endpoints as needed
}; 