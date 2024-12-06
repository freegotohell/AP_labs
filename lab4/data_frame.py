import pandas as pd
import cv2
import matplotlib.pyplot as plt


def create_and_augment_dataframe(csv_path: str) -> pd.DataFrame:
    """
    reads a csv, gets image dimensions, adds dimensions to Data_frame
    :param csv_path: path to annotation
    :return: DataFrame with three additional cols
    """
    try:
        df = pd.read_csv(csv_path)
        df.columns = ['absolute_path', 'relative_path']

        width = []
        height = []
        channels = []
        for path in df['absolute_path']:
            img = cv2.imread(path)
            if img is not None:
                width.append(img.shape[1])
                height.append(img.shape[0])
                channels.append(img.shape[2])
            else:
                width.append(0)
                height.append(0)
                channels.append(0)
                print(f"could not read image {path}")

        df['width'] = width
        df['height'] = height
        df['channels'] = channels
        return df
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_path}")
        return pd.DataFrame()


def compute_statistic(df: pd.DataFrame) -> None:
    """
    computes and prints statistics
    :param df: DataFrame
    """
    if not df.empty:
        stat = df[['width', 'height', 'channels']].describe()
        print(stat)
    else:
        print("DataFrame is empty")


def filter_width_height(df: pd.DataFrame, max_w: int, max_h: int) -> pd.DataFrame:
    """
    filters DataFrame based on width and height
    :param df: DataFrame
    :param max_w: max width parsed from cmd
    :param max_h: max height parsed from cmd
    :return: updated DataFrame
    """
    if not df.empty:
        new_df = df[((df['width'] <= max_w) & (df['height'] <= max_h))]
        return new_df
    else:
        print("DataFrame is empty")
        return pd.DataFrame()


def add_area_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """
    adds area col and sorts
    :param df: DataFrame
    :return: updated DataFrame
    """
    if not df.empty:
        df['area'] = df['width'] * df['height']
        return df.sort_values('area')
    else:
        print("DataFrame is empty")
        return pd.DataFrame()


def create_histogram(df: pd.DataFrame) -> None:
    """
    creates and displays a histogram
    :param df: DataFrame
    """
    if not df.empty:
        plt.figure(figsize=(10, 6))
        df['area'].hist(bins=len(df))
        plt.title('histogram by area')
        plt.xlabel('area')
        plt.ylabel('number of images')
        plt.grid(color='gray', linestyle='--', linewidth=0.1)
        plt.ticklabel_format(style='plain', axis='x')
        plt.show()
    else:
        print("DataFrame is empty")
