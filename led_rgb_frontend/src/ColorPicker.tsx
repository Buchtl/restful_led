import React, {useEffect, useState} from 'react';
import {ColorResult, SketchPicker} from 'react-color'

const URL_BASE = 'http://pi4b:8080'
const URL_RGB = URL_BASE + "/rgb"

interface ColorPickerProps {
    initial_rgb: string;
}

function  generate_color_result_by_hex(hex: string) :ColorResult {
    return {
        hex: hex, rgb: {r: 0, g: 0, b: 0, a: 0}, hsl: {h: 0, s: 0, l: 0, a: 0}
    }
}

const ColorPicker: React.FC<ColorPickerProps> = (props) => {

    let initial_color: ColorResult = generate_color_result_by_hex("#000000")

    let [color, setColor] = useState<ColorResult>(initial_color);
    const fetchColor = async (): Promise<ColorResult> => {
        let response = await fetch(URL_RGB)
        let rgb_str = await response.text()
        return generate_color_result_by_hex(rgb_str.replace("0x", "#"))
    }

    useEffect(() => {
        fetchColor().then(r => setColor(r))
    }, []);

    const handleColor = function (color: ColorResult) {
        setColor(color)
        let plain_hex = color.hex.replace("#", "");
        fetch(URL_RGB + "/" + plain_hex).then(r => console.log(r.statusText))
    }

    return (<div><SketchPicker width='300px'  color={color.hex} onChange={handleColor}/></div>);
};

export default ColorPicker;
