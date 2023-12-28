import React, { useState } from 'react';
import {ColorResult, SketchPicker} from 'react-color'

const ColorPicker: React.FC = () => {
    //fetch('http://pi4:8080/ryb?red=0&yellow=0&blue=0').then(r => console.log(r.statusText))
    let [color, setColor] = useState<ColorResult>({
        hex: "#000000",
        rgb: {r: 0, g: 0, b: 0, a: 1},
        hsl: {h: 0, s: 0, l: 0, a: 0}
    });

    const handleColor = function (color: ColorResult) {
        setColor(color)
        let plain_hex = color.hex.replace("#", "");
        fetch('http://pi4:8080/rgb?rgb=' + plain_hex).then(r => console.log(r.statusText))
    }

    return (<div><SketchPicker color={color.hsl} onChange={handleColor}/></div>);
};

export default ColorPicker;
