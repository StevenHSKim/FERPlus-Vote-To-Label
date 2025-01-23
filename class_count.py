import pandas as pd

def count_classes(data_path):
    """
    Count the number of samples in each class.
    
    Args:
        data_path (str): Path to the preprocessed label file
        
    Returns:
        pd.Series: Class distribution
    """
    data = pd.read_csv(data_path)
    class_counts = data['label'].value_counts().sort_index()
    
    # Print class distribution
    for label, count in class_counts.items():
        print(f"Class {label}: {count} samples")
    
    return class_counts