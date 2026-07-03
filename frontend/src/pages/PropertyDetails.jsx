import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

function PropertyDetails() {
  const { id } = useParams();

  const [property, setProperty] = useState(null);

  useEffect(() => {
    fetchProperty();
  }, []);

  const fetchProperty = async () => {
    try {
      const res = await api.get(`/properties/${id}`);
      setProperty(res.data);
    } catch (err) {
      console.log(err);
      alert("Property not found");
    }
  };

  if (!property) {
    return <h2 style={{ padding: "40px" }}>Loading...</h2>;
  }

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>{property.title}</h1>

      <p><b>Location:</b> {property.city}</p>

      <p><b>Rent:</b> ₹{property.rent}</p>

      <p><b>Description:</b> {property.description}</p>

      <p><b>Room Type:</b> {property.room_type}</p>

      <p><b>Furnishing:</b> {property.furnishing_status}</p>
    </div>
  );
}

export default PropertyDetails;