import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def pca_analysis(file_path, correlation_vars):
    """
    Perform PCA on the specified variables and plot the result.
    
    :param file_path: The path to the dataset
    :param correlation_vars: The list of columns to include in PCA
    :return: PCA result (transformed data) and explained variance ratio
    """
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Standardize the data before PCA
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[correlation_vars])

    # Apply PCA
    pca = PCA(n_components=2)  # Reduce to 2 components for visualization
    pca_result = pca.fit_transform(scaled_data)

    # Print PCA results
    print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")
    print(f"Principal Components: \n{pca.components_}")

    # Plot the PCA results
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1])
    plt.title('PCA Result - Dimensionality Reduction')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()

    return pca_result, pca.explained_variance_ratio_, pca.components_
