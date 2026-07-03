import { useState } from "react";
import api from "../services/api";

function Signup() {
  const [form, setForm] = useState({
    full_name: "",
    email: "",
    phone: "",
    password: "",
    role: "tenant",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const signup = async () => {
    try {
      const res = await api.post("/users/signup", form);
      alert("Signup Successful!");
      console.log(res.data);
    } catch (err) {
      console.log(err);
      alert("Signup Failed");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>Signup</h2>

      <input
        type="text"
        name="full_name"
        placeholder="Full Name"
        onChange={handleChange}
      />
      <br /><br />

      <input
        type="email"
        name="email"
        placeholder="Email"
        onChange={handleChange}
      />
      <br /><br />

      <input
        type="text"
        name="phone"
        placeholder="Phone"
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

      <select name="role" onChange={handleChange}>
        <option value="tenant">Tenant</option>
        <option value="owner">Owner</option>
      </select>

      <br /><br />

      <button onClick={signup}>Sign Up</button>
    </div>
  );
}

export default Signup;