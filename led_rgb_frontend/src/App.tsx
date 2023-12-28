import React from 'react';
import './App.css';
import ColorPicker from "./ColorPicker";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ColorPicker initial_rgb="000000"/>
      </header>
    </div>
  );
}

export default App;
