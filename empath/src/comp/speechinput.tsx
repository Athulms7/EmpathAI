// import React, { useState } from "react";

// interface SpeechInputProps {
//   onResult: (transcript: string) => void;
// }

// const SpeechInput: React.FC<SpeechInputProps> = ({ onResult }) => {
//   const [listening, setListening] = useState(false);

//   const startListening = () => {
//     const SpeechRecognition =
//       window.SpeechRecognition || window.webkitSpeechRecognition;

//     if (!SpeechRecognition) {
//       alert("Your browser does not support speech recognition");
//       return;
//     }

//     const recognition = new SpeechRecognition();
//     recognition.lang = "ml-IN";
//     recognition.interimResults = false;
//     recognition.maxAlternatives = 1;

//     recognition.onstart = () => setListening(true);
//     recognition.onend = () => setListening(false);

//     recognition.onresult = (event: SpeechRecognitionEvent) => {
//       const transcript = event.results[0][0].transcript;
//       onResult(transcript);
//     };

//     recognition.start();
//   };

//   return (
//     <div style={{ marginBottom: "10px" }}>
//       <button onClick={startListening}>
//         {listening ? "Listening..." : "Speak Now"}
//       </button>
//     </div>
//   );
// };

// export default SpeechInput;


import React, { useState } from "react";

interface SpeechInputProps {
  onResult: (transcript: string) => void;
}

const SpeechInput: React.FC<SpeechInputProps> = ({ onResult }) => {
  const [listening, setListening] = useState(false);
  const [showPopup, setShowPopup] = useState(false);
  const [language, setLanguage] = useState<string>("en-US"); // default

  const openPopup = () => setShowPopup(true);

  const selectLanguage = (lang: string) => {
    setLanguage(lang);
    setShowPopup(false);
    startListening(lang);
  };

  const startListening = (lang: string) => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Your browser does not support speech recognition");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = lang; // set language
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = () => setListening(true);
    recognition.onend = () => setListening(false);

    recognition.onresult = (event: SpeechRecognitionEvent) => {
      const transcript = event.results[0][0].transcript;
      onResult(transcript);
    };

    recognition.start();
  };

  return (
    <div style={{ marginBottom: "10px" }}>
      <button onClick={openPopup}>
        {listening ? "Listening..." : "Speak Now"}
      </button>

      {/* Language Selection Popup */}
      {showPopup && (
        <div
          style={{
            position: "absolute",
            top: "100px",
            left: "50%",
            transform: "translateX(-50%)",
            background: "white",
            border: "1px solid #ccc",
            padding: "20px",
            zIndex: 1000,
            boxShadow: "0px 0px 10px rgba(0,0,0,0.2)",
          }}
        >
          <h4>Select Language</h4>
          <button onClick={() => selectLanguage("en-US")} style={{ marginRight: "10px" }}>
            English
          </button>
          <button onClick={() => selectLanguage("ml-IN")}>Malayalam</button>
        </div>
      )}
    </div>
  );
};

export default SpeechInput;
