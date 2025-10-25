import React, { useState } from "react";
import axios from "axios";
import { useDispatch } from "react-redux";
import { setAuth } from "../redux/authSlice";
import { useNavigate } from "react-router-dom";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await axios.post(
        "http://localhost:5001/signup",
        { email, password },
        { withCredentials: true } // allows httpOnly cookie
      );

      // Update Redux authSlice
      dispatch(setAuth({ token: res.data.token, user: { email } }));

      // Redirect to Todo app
      navigate("/todos");
    } catch (err) {
      if (err.response?.status === 409) {
        // User already exists → redirect to Signin
        navigate("/signin");
      } else {
        setError(err.response?.data?.error || "Signup failed");
      }
    }
  };

  return (
    <div className="auth-container">
      <h2>Sign Up</h2>
      <form onSubmit={handleSignup}>
        <input
          type="email"
          placeholder="Email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Sign Up</button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
