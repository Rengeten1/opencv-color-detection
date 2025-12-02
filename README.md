# Real-Time Color Detection

A simple color detection program that uses your webcam to identify colors in real-time using Python and OpenCV.

## Features

- Detects 11 different colors: Red, Orange, Yellow, Green, Cyan, Blue, Purple, Pink, White, Gray, and Black
- Real-time detection from webcam
- Shows detection area with a green box
- Displays HSV values for debugging

## Requirements

- Python 3.7+
- Webcam

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Use

1. Run the program:
```bash
python color_detection.py
```

2.  Place a colored object in the green box shown on screen

3. The detected color name will appear at the top

4. Press 'q' to quit

## How It Works

The program uses HSV color space instead of RGB because it's better at detecting colors under different lighting conditions. It samples the center area of the webcam feed and compares the color values against predefined ranges to identify the color.

## Customization

You can adjust the detection area size by changing this line:
```python
sample_size = 100  # Make this bigger or smaller
```

To modify which colors are detected or their ranges, edit the `colors` list in the `detect_color()` function. 

## Troubleshooting

- **Camera won't open**: Make sure no other program is using your webcam
- **Wrong colors detected**: Try better lighting or adjust the color ranges in the code
- **Slow performance**: Reduce the `sample_size` value

## Author

Rownak Deb Kabya  
AI Student at Deggendorf Institute of Technology

## License

MIT License - feel free to use and modify! 