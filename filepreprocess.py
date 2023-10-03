import csv


def extract_and_write_data(input_file_path, output_file_path):
    with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ["video_id", "feature_name", "start_time", "end_time", "start_frame", "end_frame"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            new_row = {
                "video_id": row["video_id"],
                "feature_name": row["noun"],  # assuming feature name is in 'noun' column
                "start_time": row["start_timestamp"],
                "end_time": row["stop_timestamp"],
                "start_frame": row["start_frame"],
                "end_frame": row["stop_frame"]
            }
            writer.writerow(new_row)


extract_and_write_data('EPIC_100_retrieval_test.csv', 'processed_file.csv')
