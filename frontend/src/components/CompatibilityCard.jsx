import { useState } from "react";
import api from "../services/api";

function CompatibilityCard({ propertyId }) {
  const [result, setResult] = useState(null);

  const checkCompatibility = async () => {
    try {
      const res = await api.post("/compatibility/", {
        tenant_id: 1,
        property_id: propertyId,
      });

      setResult(res.data);
    } catch (err) {
      console.log(err);
      alert("Failed to calculate compatibility");
    }
  };

  return (
    <div style={{ marginTop: "10px" }}>
      <button
        onClick={checkCompatibility}
        style={{
          padding: "10px 20px",
          cursor: "pointer",
        }}
      >
        🤖 Check Compatibility
      </button>

      {result && (
        <div
          style={{
            marginTop: "10px",
            border: "1px solid green",
            padding: "10px",
            borderRadius: "8px",
          }}
        >
          <h4>Compatibility Score</h4>

          <p>
            <strong>{result.score}%</strong>
          </p>

          <p>{result.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default CompatibilityCard;