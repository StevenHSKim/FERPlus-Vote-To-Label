import pandas as pd
import argparse
from pathlib import Path
from class_count import count_classes
from plot_graph import plot_distribution

def parse_arguments():
    """Command line argument parser for label preprocessing method."""
    parser = argparse.ArgumentParser(description="FERPlus Label Preprocessing")
    parser.add_argument(
        "--method",
        type=str,
        default='select_last',
        choices=['select_first', 'select_last'],
        help="Method for handling tied maximum scores"
    )
    return parser.parse_args()

def preprocess_data(data_path, method):
    """
    Preprocess FERPlus dataset labels.
    
    Args:
        data_path (str): Path to the original FERPlus label file
        method (str): Method for handling tied maximum scores
        
    Returns:
        pd.DataFrame: Preprocessed data with image names and labels
    """
    # Read the original label file
    data = pd.read_csv(data_path)
    
    # Remove unnecessary columns
    data = data.drop(columns=['Usage', 'unknown', 'NF'])
    
    # Remove rows where all emotion scores are 0
    data = data[(data.iloc[:, 1:] != 0).any(axis=1)]
    
    # Assign labels based on maximum emotion scores
    if method == 'select_first':
        # Select first maximum (favors Neutral class)
        data['label'] = data.iloc[:, 1:].apply(lambda row: row.values.argmax(), axis=1)
    else:
        # Select last maximum (reduces Neutral class)
        data['label'] = data.iloc[:, 1:].apply(
            lambda row: len(row) - 1 - row[::-1].values.argmax(), axis=1
        )
    
    # Keep only necessary columns
    return data[['Image name', 'label']]

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Define paths
    data_path = Path('path/to/fer2013new.csv')  ### Todo: Change this path
    output_path = Path(f'result/FERPlus_Label_modified_{args.method}.csv')
    plot_path = Path('img')
    
    # Create output directories if they don't exist
    plot_path.mkdir(exist_ok=True)
    
    # Preprocess data
    processed_data = preprocess_data(data_path, args.method)
    
    # Save processed data
    processed_data.to_csv(output_path, index=False)
    
    # Count classes and plot distribution
    class_counts = count_classes(output_path)
    plot_distribution(output_path, plot_path / f'class_distribution_{args.method}.png')

if __name__ == "__main__":
    main()
