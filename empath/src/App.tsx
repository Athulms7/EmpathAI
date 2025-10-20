import React, { useState } from "react";
import axios from "axios";
import SpeechInput from "./comp/speechinput";

interface NGO {
  name: string;
  contact: string;
}

interface ResponseData {
  category: string;
  legal_info: string;
  ngos: NGO[];
}

const App: React.FC = () => {
  const [textInput, setTextInput] = useState<string>("");
  const [response, setResponse] = useState<ResponseData | null>(null);

  const handleSubmit = async () => {
    if (!textInput) return;

    try {
      const res = await axios.post<ResponseData>("http://localhost:8000/analyze", {
        text: textInput,
      });
      setResponse(res.data);
    } catch (err) {
      console.error(err);
      alert("Error sending data to backend");
    }
    setTextInput("");
  };

  const handleSpeechResult = (transcript: string) => {
    setTextInput(transcript);
  };

  return (
    <div style={{ maxWidth: "600px", margin: "50px auto", fontFamily: "Arial, sans-serif" }}>
      <h2>Incident Assist App</h2>

      {/* Speech Input */}
      <SpeechInput onResult={handleSpeechResult} />

      {/* Text Input */}
      <textarea
        value={textInput}
        onChange={(e) => setTextInput(e.target.value)}
        rows={4}
        placeholder="Describe your incident..."
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <button onClick={handleSubmit} style={{ marginBottom: "20px" }}>
        Submit
      </button>

      {/* Display Response */}
      {response && (
        <div style={{ border: "1px solid #ccc", padding: "10px" }}>
          <h3>Analysis Result:</h3>
          <p><strong>Category:</strong> {response.category}</p>
          <p><strong>Legal Info:</strong> {response.legal_info}</p>
          <h4>NGO Contacts:</h4>
          <ul>
            {response.ngos.map((ngo, i) => (
              <li key={i}>{ngo.name} - {ngo.contact}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default App;
