# Query Processor Benchmark Tool

## Overview

This tool is designed to generate and execute queries on a dataset of video features, providing a benchmark for testing query processing systems in the context of video analysis. It allows for various modes and distributions for both operation types and features, enabling users to test system performance under different scenarios and loads.

##Copyright_at_PennState MicroDesignLab

## Prerequisites

- Python 3.x
- NumPy library

Install NumPy using pip:

```bash
pip install numpy
```

## Usage

### Basic Usage

Navigate to the script's directory and run:

```bash
python script_name.py
```

### Customization Options

Customize the script's behavior using various command-line arguments:

```bash
python script_name.py --file_path=mydata.csv --num_items=150 --num_queries=10 --op_mode=gaussian --feature_mode=zipfian --seed=42 --op_seed=43 --feature_seed=44
```

#### Arguments

- `--file_path`: Path to the CSV file.
- `--num_items`: Number of items to read from the file.
- `--num_queries`: Number of queries.
- `--op_mode`: Operation type generation mode (random, gaussian, zipfian, single).
- `--feature_mode`: Feature generation mode (random, gaussian, zipfian, single).
- `--seed`: Seed for key selection.
- `--op_seed`: Seed for operation type selection.
- `--feature_seed`: Seed for feature selection.
- `--single_op_type`: Operation type for single mode (AND, OR, NOT, COUNT).
- `--single_key`: Key for single mode.
- `--single_value`: Value for single mode.

### Query Modes

- **Random**: Selects random keys, features, and operation types.
- **Gaussian**: Selects keys, features, and operation types based on a normal distribution.
- **Zipfian**: Selects keys, features, and operation types based on a Zipf distribution.
- **Single**: Uses a single specified key, feature, or operation type.

## Example Data Format

Ensure your CSV file adheres to the following format:

```plaintext
video_id,start_time,end_time,start_frame,end_frame,feature_name,...
```

## Troubleshooting

- Ensure your CSV file is correctly formatted and accessible from the script's location.
- Ensure all provided seeds and mode selections are valid.
