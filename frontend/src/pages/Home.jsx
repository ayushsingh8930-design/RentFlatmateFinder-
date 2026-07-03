import { Link } from "react-router-dom";

function Home() {
  return (
    <div
      style={{
        textAlign: "center",
        padding: "80px",
        fontFamily: "Arial",
      }}
    >
      <h1>🏠 Rent & Flatmate Finder</h1>

      <p>
        Find verified rooms, compatible flatmates and AI-powered compatibility
        score.
      </p>

      <br />

      <Link to="/signup">
        <button
          style={{
            padding: "12px 25px",
            marginRight: "10px",
            cursor: "pointer",
          }}
        >
          Sign Up
        </button>
      </Link>

      <Link to="/login">
        <button
          style={{
            padding: "12px 25px",
            cursor: "pointer",
          }}
        >
          Login
        </button>
      </Link>

      <br />
      <br />

      <Link to="/properties">
        <button
          style={{
            padding: "12px 25px",
            cursor: "pointer",
          }}
        >
          Browse Properties
        </button>
      </Link>
    </div>
  );
}

export default Home;