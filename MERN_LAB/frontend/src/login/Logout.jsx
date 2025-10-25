import React from "react";
import { useDispatch } from "react-redux";
import { clearAuth } from "../redux/authSlice";
import axios from "axios";

const Logout = () => {
  const dispatch = useDispatch();

  const handleLogout = async () => {
    try {
      await axios.post("http://localhost:5001/logout", {}, { withCredentials: true });
      dispatch(clearAuth());
    } catch (err) {
      console.error("Logout failed:", err);
    }
  };

  return <button onClick={handleLogout}>Logout</button>;
};

export default Logout;
