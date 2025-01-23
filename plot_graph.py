import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(data_path, output_path):
    """
    Plot and save the class distribution.
    
    Args:
        data_path (str): Path to the preprocessed label file
        output_path (str): Path to save the plot
    """
    # Read data
    data = pd.read_csv(data_path)
    class_counts = data['label'].value_counts().sort_index()
    
    # Define class names
    class_names = [
        "Neutral", "Happiness", "Surprise", "Sadness",
        "Anger", "Disgust", "Fear", "Contempt"
    ]
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.bar(class_names, class_counts.values, color='skyblue', edgecolor='black')
    
    # Customize plot
    plt.xlabel("Emotion Class")
    plt.ylabel("Number of Images")
    plt.title("FERPlus Dataset Class Distribution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save and display plot
    plt.savefig(output_path, dpi=300, bbox_inches='tight')