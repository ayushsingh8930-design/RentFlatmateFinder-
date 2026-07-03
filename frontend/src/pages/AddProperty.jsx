import { useState } from "react";
import api from "../services/api";

function AddProperty() {
  const [form, setForm] = useState({
    title: "",
    city: "",
    rent: "",
    description: "",
    available_from: "",
    room_type: "",
    furnishing_status: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const addProperty = async () => {
    try {
      await api.post("/properties/", form);
      alert("Property Added Successfully!");

      setForm({
        title: "",
        city: "",
        rent: "",
        description: "",
        available_from: "",
        room_type: "",
        furnishing_status: "",
      });
    } catch (err) {
      console.log(err);
      alert("Failed to add property");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Add Property</h1>

      <input
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="city"
        placeholder="City"
        value={form.city}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="rent"
        type="number"
        placeholder="Rent"
        value={form.rent}
        onChange={handleChange}
      />

      <br /><br />

      <textarea
        name="description"
        placeholder="Description"
        value={form.description}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="available_from"
        type="date"
        placeholder="Available From"
        value={form.available_from}
        onChange={handleChange}
      />

      <input
        name="room_type"
        placeholder="Room Type"
        value={form.room_type}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="furnishing_status"
        placeholder="Furnishing Status"
        value={form.furnishing_status}
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={addProperty}>
        Add Property
      </button>
    </div>
  );
}

export default AddProperty;