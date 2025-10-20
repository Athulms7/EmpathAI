import React, { useState } from "react";

interface SpeechInputProps {
  onResult: (transcript: string) => void;
}

const SpeechInput: React.FC<SpeechInputProps> = ({ onResult }) => {
  const [listening, setListening] = useState(false);

  const startListening = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Your browser does not support speech recognition");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "ml-IN";
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
      <button onClick={startListening}>
        {listening ? "Listening..." : "Speak Now"}
      </button>
    </div>
  );
};

export default SpeechInput;
