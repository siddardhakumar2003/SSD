import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { setAuth } from "../redux/authSlice";
import axios from "axios";

const SignIn = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();

  const handleSignIn = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        "http://localhost:5001/signin",
        { email, password },
        { withCredentials: true }
      );

      dispatch(setAuth({ token: res.data.token, user: { email } }));
    } catch (err) {
      console.error("Signin failed:", err);
      alert("Invalid credentials");
    }
  };

  return (
    <div className="signin-container">
      <h2>Sign In</h2>
      <form onSubmit={handleSignIn}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <button type="submit">Sign In</button>
      </form>
    </div>
  );
};

export default SignIn;
