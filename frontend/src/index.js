import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";

function App() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    fetch("/api")
      .then(res => res.json())
      .then(data => setMsg(data.message || data.error));
  }, []);

  return <h1>{msg}</h1>;
}

ReactDOM.render(<App />, document.getElementById("root"));
