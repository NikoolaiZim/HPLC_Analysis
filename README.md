# HPLC Data Evaluation Tool using Python Dash

## Overview

This Python Dash project is a web-based HPLC (High-Performance Liquid Chromatography) data evaluation tool. It allows users to visualize HPLC measurements, identify peaks, and perform various analyses on the data. The dashboard provides interactive features such as peak prominence adjustment, table filtering, and saddle point calculation.

## Features

### 1. Graph Visualization

The dashboard displays the HPLC measurement data graphically, making it easy for users to analyze and interpret the chromatogram.

### 2. Peak Detection and Table

The tool automatically detects peaks in the chromatogram and presents them in a table. Users can adjust the peak prominence parameter to fine-tune the peak detection process based on their specific requirements.

### 3. Interval Slider

An interval slider is provided to allow users to shrink the table view based on a specified retention time interval. This feature enhances the ability to focus on specific regions of interest in the chromatogram.

### 4. Saddle Point Calculation

Users can input two boundary values, and the tool will calculate the saddle point within that range. This functionality aids in further analysis and characterization of peaks.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/NikoolaiZim/HPLC_Analysis.git

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Run the application:**
   python main.py

## Usage

1. **Adjust Peak Prominence:**
   - Fine-tune peak detection by adjusting the peak prominence parameter.

2. **Use Interval Slider:**
   - Utilize the interval slider to focus on specific retention time intervals in the table.

3. **Input Saddle Point Boundary Values:**
   - Select two points in the graph to define the boundaries, between which the saddlepoint should be found. Start the calculation with the provided button.

## Screenshots

![overall](https://github.com/NikoolaiZim/HPLC_Analysis/assets/102020689/550c9d70-4bfa-4de4-8a19-a332dc495057)

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

No license.

## Acknowledgments

- Special thanks to [Dash](https://dash.plotly.com/) for providing an excellent framework for building interactive web applications with Python.

## Author

Nikolai Zimmermann

