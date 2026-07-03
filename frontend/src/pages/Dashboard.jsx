import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../services/api";
import CompatibilityCard from "../components/CompatibilityCard";

function Dashboard() {
  const navigate = useNavigate();

  const [properties, setProperties] = useState([]);

  const fetchProperties = async () => {
    try {
      const res = await api.get("/properties/");
      setProperties(res.data);
    } catch (err) {
      console.log(err);
      alert("Failed to load properties");
    }
  };

  const sendInterest = async (propertyId) => {
    try {
      await api.post("/interest/", {
        tenant_id: 1,
        property_id: propertyId,
      });

      alert("Interest Sent Successfully!");
    } catch (err) {
      console.log(err);
      alert("Failed to send interest");
    }
  };

  useEffect(() => {
    fetchProperties();
  }, []);

  return (
    <div
      style={{
        padding: "40px",
        fontFamily: "Arial",
      }}
    >
      <h1>🏠 Rent & Flatmate Finder</h1>

      <h2>Dashboard</h2>

      <hr />

      <h2>Available Properties</h2>

      {properties.length === 0 ? (
        <p>No properties available.</p>
      ) : (
        properties.map((property) => (
          <div
            key={property.id}
            style={{
              border: "1px solid #ccc",
              borderRadius: "10px",
              padding: "20px",
              marginBottom: "20px",
            }}
          >
            <h3>{property.title}</h3>

            <p>
              <strong>Location:</strong> {property.city}
            </p>

            <p>
              <strong>Rent:</strong> ₹{property.rent}
            </p>

            <p>
              <strong>Description:</strong> {property.description}
            </p>

            <p>
              <strong>Room Type:</strong> {property.room_type}
            </p>

            <p>
              <strong>Furnishing:</strong> {property.furnishing_status}
            </p>

            <button
              onClick={() => navigate(`/property/${property.id}`)}
              style={{
                padding: "10px 20px",
                marginRight: "10px",
                cursor: "pointer",
              }}
            >
              View Details
            </button>

            <button
              onClick={() => sendInterest(property.id)}
              style={{
                padding: "10px 20px",
                cursor: "pointer",
              }}
            >
              ❤️ Interested
            </button>

            <CompatibilityCard propertyId={property.id} />
          </div>
        ))
      )}
    </div>
  );
}

export default Dashboard;