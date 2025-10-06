# Recursion Tree & Recurrence Relation Analyzer

This project provides a comprehensive tool for visualizing and analyzing recurrence relations, particularly useful for understanding the complexities of algorithms. It includes functionalities to generate recursion trees, apply the Master Theorem, and visualize the results through various plots.

## Project Structure

```
recursion-tree-recurrence-analyzer
├── src
│   ├── main.py               # Entry point of the application
│   ├── analyzer.py           # Contains analysis functions
│   ├── visualizer.py         # Visualization functions
│   ├── utils.py              # Utility functions
│   └── types
│       └── __init__.py       # Package initialization
├── requirements.txt          # Required Python libraries
├── setup.py                  # Project packaging and metadata
└── README.md                 # Project documentation
```

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

1. **Run the Application**: Execute the main script to start the analysis.
   ```
   python src/main.py
   ```

2. **Analyze Recurrence Relations**: Input the parameters for your recurrence relation (a, b, f(n), n) to analyze and visualize the recursion tree.

3. **Visualize Results**: The application will generate plots to help you understand the costs at each level of the recursion tree.

## Examples

Example data for common algorithms can be found in the `src/examples` directory:

- **Merge Sort**: `mergesort.json`
- **Binary Search**: `binarysearch.json`
- **Strassen’s Matrix Multiplication**: `strassen.json`

Feel free to modify the example files or create your own to test different recurrence relations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.