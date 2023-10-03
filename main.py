# This is a sample Python script.
import csv
import random
import re
import argparse
import numpy as np


def read_processed_data(file_path, num_items):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i >= num_items:
                break
            data.append(row)
    return data


def parse_and_execute_query(data, query):
    # Extract the operator and conditions from the query string
    operator_match = re.match(r'(\w+)\((.*)\)', query)
    if not operator_match:
        raise ValueError("Invalid query format")

    operator, conditions_str = operator_match.groups()

    # Extract key-value pairs from the conditions string
    conditions = re.findall(r'(\w+)=(\w+)', conditions_str)

    # Execute the query based on the operator
    if operator == "AND":
        result = data
        for key, value in conditions:
            result = [item for item in result if item[key] == value]
    elif operator == "OR":
        result = []
        for key, value in conditions:
            result += [item for item in data if item[key] == value]
    elif operator == "NOT":
        if len(conditions) != 1:
            raise ValueError("NOT operator requires exactly one condition")
        key, value = conditions[0]
        result = [item for item in data if item[key] != value]
    elif operator == "COUNT":
        if len(conditions) != 1:
            raise ValueError("COUNT operator requires exactly one condition")
        key, value = conditions[0]
        result = len([item for item in data if item[key] == value])
    else:
        raise ValueError("Invalid operator")

    return result


def generate_query(data, op_mode="random", feature_mode="random", custom_query=None, seed=None, op_seed=None, feature_seed=None, single_op_type="AND", single_key="feature_name", single_value="plate"):
    keys = ["video_id", "start_time", "end_time", "start_frame", "end_frame"]
    operators = ["AND", "OR", "NOT", "COUNT"]
    features = [item["feature_name"] for item in data]

    # Generate operator
    random.seed(op_seed)
    if op_mode == "random":
        operator = random.choice(operators)
    elif op_mode == "gaussian":
        operator = operators[int(np.clip(np.random.normal(loc=1.5, scale=0.5), 0, 3))]
    elif op_mode == "zipfian":
        operator = operators[int(np.clip(np.random.zipf(1.5), 0, 3)) % 4]
    elif op_mode == "single":
        operator = single_op_type
    else:
        raise ValueError("Invalid op_mode")

    # Generate feature
    np.random.seed(feature_seed)
    if feature_mode == "random":
        feature = random.choice(features)
    elif feature_mode == "gaussian":
        feature = features[int(np.clip(np.random.normal(loc=len(features)/2, scale=len(features)/4), 0, len(features)-1))]
    elif feature_mode == "zipfian":
        feature = features[int(np.clip(np.random.zipf(1.5), 0, len(features)-1)) % len(features)]
    elif feature_mode == "single":
        feature = single_value
    else:
        raise ValueError("Invalid feature_mode")

    # Generate key
    random.seed(seed)
    key = random.choice(keys)

    return f"{operator}({key}={feature})"


def main(args):
    # Load the specified number of items from the CSV file
    data = read_processed_data(args.file_path, args.num_items)

    # Execute each query
    for _ in range(args.num_queries):
        query = generate_query(data, seed=args.seed, op_seed=args.op_seed, single_op_type=args.single_op_type, single_key=args.single_key, single_value=args.single_value)
        print("Generated query:", query)

        # Parse and execute the query, then display the result
        try:
            result = parse_and_execute_query(data, query)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Query Processor')
    parser.add_argument('--file_path', type=str, default='processed_file.csv', help='Path to the CSV file.')
    parser.add_argument('--num_items', type=int, default=100, help='Number of items to read from the file.')
    parser.add_argument('--num_queries', type=int, default=5, help='Number of queries.')
    parser.add_argument('--op_mode', type=str, choices=['random', 'gaussian', 'zipfian', 'single'], default='random', help='Operation type generation mode.')
    parser.add_argument('--feature_mode', type=str, choices=['random', 'gaussian', 'zipfian', 'single'], default='random', help='Feature generation mode.')
    parser.add_argument('--seed', type=int, default=None, help='Seed for key selection.')
    parser.add_argument('--op_seed', type=int, default=None, help='Seed for operation type selection.')
    parser.add_argument('--feature_seed', type=int, default=None, help='Seed for feature selection.')
    parser.add_argument('--single_op_type', type=str, choices=['AND', 'OR', 'NOT', 'COUNT'], default='AND', help='Operation type for single mode.')
    parser.add_argument('--single_key', type=str, default='feature_name', help='Key for single mode.')
    parser.add_argument('--single_value', type=str, default='plate', help='Value for single mode.')

    args = parser.parse_args()
    main(args)



