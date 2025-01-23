import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(data_path, output_path):
    """
    Plot and save the class distribution with fixed y-axis range.
    
    Args:
        data_path (str): Path to the preprocessed label file
        output_path (str): Path to save the plot
    """
    data = pd.read_csv(data_path)
    class_counts = data['label'].value_counts().sort_index()
    
    class_names = [
        "Neutral", "Happiness", "Surprise", "Sadness", "Anger", "Disgust", "Fear", "Contempt"
    ]
    
    plt.figure(figsize=(10, 6))
    plt.bar(class_names, class_counts.values, color='skyblue', edgecolor='black')
    
    plt.xlabel("Emotion Class")
    plt.ylabel("Number of Images")
    plt.title("FERPlus Dataset Class Distribution")
    plt.xticks(rotation=45)
    
    # Set fixed y-axis range based on the maximum count across both methods
    plt.ylim(0, 14000)  # Adjusted based on provided data
    
    # Add value labels on top of each bar
    for i, v in enumerate(class_counts.values):
        plt.text(i, v, str(v), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')