import React, { useState } from "react";
import { useSelector } from "react-redux";
import TaskApp from "./task/TaskApp";
import SignIn from "./login/SignIn";   // fixed import
import Logout from "./login/Logout";   // fixed import
import Signup from "./login/Signup";   // new Signup component

function App() {
  const token = useSelector(state => state.auth.token);
  const [showSignup, setShowSignup] = useState(false); // toggle between Signin and Signup

  if (token) {
    return (
      <div>
        <Logout />
        <TaskApp />
      </div>
    );
  }

  return (
    <div>
      {showSignup ? (
        <Signup />   // show Signup form
      ) : (
        <SignIn />   // show Signin form
      )}

      {/* Toggle button to switch forms */}
      <div style={{ marginTop: "10px" }}>
        <button onClick={() => setShowSignup(!showSignup)}>
          {showSignup ? "Already have an account? Sign In" : "New user? Sign Up"}
        </button>
      </div>
    </div>
  );
}

export default App;
