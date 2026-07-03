import { useState } from "react";
import api from "../services/api";

function Login() {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const login = async () => {
    try {
      const res = await api.post("/users/login", form);

      alert("Login Successful!");
      console.log(res.data);
    } catch (err) {
      console.log(err);
      alert("Login Failed");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>Login</h2>

      <input
        type="email"
        name="email"
        placeholder="Email"
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="password"
        name="password"
        placeholder="Password"
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={login}>
        Login
      </button>
    </div>
  );
}

export default Login;