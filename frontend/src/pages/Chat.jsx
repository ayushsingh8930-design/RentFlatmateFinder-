import { useState } from "react";

function Chat() {
  const [message, setMessage] = useState("");

  const sendMessage = () => {
    alert("Chat UI ready. WebSocket connection next.");
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Chat</h1>

      <textarea
        rows="5"
        cols="50"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br />
      <br />

      <button onClick={sendMessage}>
        Send Message
      </button>
    </div>
  );
}

export default Chat;