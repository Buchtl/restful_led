import React, { useEffect } from 'react';

const ColorPicker: React.FC = () => {
    fetch('http://pi4:8080/ryb?red=0&yellow=0&blue=0').then(r => console.log(r.statusText))
    return (<div>Colorpicker</div>);
};

export default ColorPicker;
