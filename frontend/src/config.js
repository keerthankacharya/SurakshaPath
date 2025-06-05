const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://surakshapath-safe.vercel.app/api'  // Replace with your Vercel deployment URL
  : 'http://localhost:5000/api';

export const API_ENDPOINTS = {
  alerts: `${API_BASE_URL}/alerts`,
  news: `${API_BASE_URL}/news`,
  // Add other endpoints as needed
}; 