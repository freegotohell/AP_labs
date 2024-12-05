import argparse
from data_frame import *


def parse() -> tuple[str, int, int]:
    """
    Parse arguments from terminal
    :return:Tuple of parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=str, help="Path to the annotation file")
    parser.add_argument("max_width", type=int, help="Max width of image")
    parser.add_argument("max_height", type=int, help="Max height of image")
    args = parser.parse_args()
    return args.csv_path, args.max_width, args.max_height


def main():
    csv_path, max_width, max_height = parse()
    try:
        data_frame = create_and_augment_dataframe(csv_path)
        if data_frame.empty:
            print("error during creation DataFrame, exited")
            return
        compute_statistic(data_frame)
        new_data_frame = filter_width_height(data_frame, max_width, max_height)
        print("\n\nfiltered DataFrame:\n", new_data_frame)
        add_area_and_sort(data_frame)  # updates existing data_frame
        print("\n\nDataFrame sorted by area:\n", data_frame)
        create_histogram(data_frame)
    except FileNotFoundError:
        print(f"no csv file at {csv_path}")
    except Exception as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
