# Die Analyzer

This project solves a semiconductor die validation problem given as part of **UNHACK’25 by KLA Tencor**. It analyzes wafer die data, applies orientation transformations, validates each die using a reference mask, and generates a structured output indicating the number of good and bad dies.

## Problem Statement

Given:
- `INPUT.txt` – Contains wafer die layout, good/bad die codes, and orientation.
- `MATRIX.csv` – A binary mask (1 = valid die, 0 = invalid die).

The task is to:
- Rotate the die layout based on the specified orientation (0°, 90°, 180°, or 270°).
- Apply the mask to exclude invalid die positions.
- Count the number of good and bad dies.
- Generate a clean output file showing the final validated die map.

## Features

- Parses input files to extract die and layout information.
- Handles rotation of the die matrix.
- Overlays a mask to filter out invalid positions.
- Outputs die counts and the final matrix to `M1T1.txt`.

## Technologies Used

- Python (3.x)
- File Handling
- Matrix Operations and Transformations
- Data Validation and Mapping

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Mathruka-M/Die-Analyzer.git
2. Place INPUT.txt and MATRIX.csv in the project directory.

3. Open a terminal and run:
   python main.py
4. Check the output file: M1T1.txt
