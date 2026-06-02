# Font Triangulation Tool

A Python library that converts TrueType/OpenType font glyph outlines into triangular meshes.

## Features

- ✅ **Full Sample Point Triangulation**: All line points and quadratic/cubic curve sample points are added to the vertex set
- ✅ **No Additional Vertices**: Triangulation only uses contour sample points without adding any new vertices
- ✅ **Inner/Outer Contour Differentiation**: Outer contours displayed in red, inner contours (holes) in blue
- ✅ **Complete Vertex Display**: All sample points visualized

## Technical Principles

### Core Workflow

1. **Font Parsing**: Use `fontTools` to read font files and extract glyph outlines
2. **Contour Sampling**: Discretize Bezier curves into sample points
3. **Direction Detection**: Distinguish outer contours (counter-clockwise) from inner contours (clockwise) based on area sign
4. **Hierarchy Construction**: Establish parent-child relationships between outer and inner contours
5. **Triangulation**: Use `shapely` for polygon triangulation, ensuring triangles are within valid regions

### Contour Direction Convention

| Contour Type | Direction | Area Sign |
|--------------|-----------|-----------|
| Outer Contour | Counter-clockwise | Negative |
| Inner Contour (Hole) | Clockwise | Positive |

## Installation

```bash
pip install numpy matplotlib fonttools shapely
```

## Usage

### Method 1: Interactive Mode

```bash
python font2tri_lib.py
```

The program will automatically search for system fonts (KaiTi, Microsoft YaHei, SimSun), then you can input characters for triangulation.

### Method 2: Programmatic Call

```python
from font2tri_lib import FontTriangulator

# Initialize triangulator
ft = FontTriangulator(r"C:\Windows\Fonts\simkai.ttf")

# Process single character
ft.run('中')

# Batch process characters
for char in ['中', '国', '字', 'A', 'O']:
    ft.run(char)
```

### Method 3: Test Script

```bash
python test_all_chars.py
```

## Core Class Documentation

### FontTriangulator

The core class for font triangulation, providing glyph contour extraction and triangulation functionality.

#### Methods

| Method | Description | Parameters |
|--------|-------------|------------|
| `__init__(font_path)` | Initialize triangulator | `font_path`: Path to font file |
| `extract_sampled_contours(char, curve_steps=20)` | Extract character contour sample points | `char`: Single character; `curve_steps`: Curve sampling steps |
| `triangulate_from_contour_points(contours)` | Triangulate contours | `contours`: List of contour point arrays |
| `show(char, contours, vs, fs)` | Visualize results | character, contours, vertices, faces |
| `run(char, curve_steps=20)` | Complete execution flow | character and curve sampling steps |

## Output Example

The program displays three plots:

1. **Left**: Original contours (outer contours red, inner contours blue)
2. **Middle**: Triangulation result (light blue fill, blue edges)
3. **Right**: Vertex set (red dots showing all sample points)

Console output example:

```
【中】Done
  Contours: 1
  Vertices: 168 (lines + curve samples)
  Triangles: 324
```

## Supported Font Formats

- TrueType (.ttf)
- TrueType Collection (.ttc)
- OpenType (.otf)

## System Requirements

- Python 3.6+
- Windows (system font search path is Windows-specific)

## Project Structure

```
font2tri_outline/
├── font2tri_lib.py      # Core library file
├── test_all_chars.py    # Test script
├── README.md            # Documentation (Chinese)
└── readme_en.md         # Documentation (English)
```

## License

MIT License
