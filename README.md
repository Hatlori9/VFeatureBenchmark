# Video Query Processor Benchmark Tool


## Overview

This tool is designed to generate and execute queries on a dataset of video features, providing a benchmark for testing query processing systems in the context of video analysis. It allows for various modes and distributions for both operation types and features, enabling users to test system performance under different scenarios and loads.



## Copyright at PennState MicroDesignLab
https://mdl.cse.psu.edu/

## Prerequisites

- Python 3.x
- NumPy library
- (Optional for feature extraction) TensorFlow library
- (Optional for feature extraction) OpenCV library

Install the necessary libraries using pip:

```bash
pip install numpy tensorflow opencv-python
```

## Video Feature source
currently supported:

- EPIC-kitchen-100
- more later....


## Usage

### Basic Usage

Navigate to the script's directory and run:

```bash
python main.py
```

### Customization Options

Customize the script's behavior using various command-line arguments:

```bash
python main.py --file_path=mydata.csv --num_items=150 --num_queries=10 --op_mode=gaussian --feature_mode=zipfian --seed=42 --op_seed=43 --feature_seed=44
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

## Feature Extraction from Videos using feature_prepare.py

The feature extraction script utilizes the VGG16 model to extract features from video frames. It supports various video formats and extracts a feature vector for each frame, which is prepared for feature extraction.

### Example Usage
Update 'the video_folder_path' and 'csv_file_path' variables in the script:

```python
video_folder_path = "/path/to/videos"
csv_file_path = "output_features.csv"
```
## Structure of the CSV Output

The CSV file will contain the following columns:

- `video_id`: Identifier of the video.
- `feature_name`: Identifier of the extracted feature.
- `start_time`: Start time of the frame (in seconds).
- `end_time`: End time of the frame (in seconds).
- `start_frame`: Start frame number.
- `end_frame`: End frame number.
  
### Video Formats
The script supports various video formats, including but not limited to MP4, MKV, AVI, MOV, and FLV. Ensure the OpenCV library in your Python environment supports the formats you intend to use.





















## Data Storage Location

The data (CSV file) can be stored in any accessible location. Use the `--file_path` argument to specify the path to your data file when running the script.

### Example Usage

If your data is stored in a different directory, simply provide the full path:

```bash
python main.py --file_path=/path/to/your/data.csv
```

If your data is stored in a cloud storage or accessible via a URL, ensure your script is capable of handling URL file paths and provide the URL:

```bash
python main.py --file_path=http://url.to/your/data.csv
```

**Note**: Handling URLs might require additional libraries or modifications to the `read_processed_data` function to fetch and read data from the web. Ensure your Python environment and script are configured to handle such scenarios.

### Data Security

Ensure that the data storage location is secure and the path provided does not expose sensitive information. When using cloud storage or web URLs, ensure that the data is secured and accessed over a secure connection (e.g., HTTPS).


## Troubleshooting

- Ensure your CSV file is correctly formatted and accessible from the script's location.
- Ensure all provided seeds and mode selections are valid.
