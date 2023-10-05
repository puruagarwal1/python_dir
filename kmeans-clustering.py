import numpy as np

def kmeans(X, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    
    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
        # Check for convergence
        if np.all(new_centroids == centroids):
            break
        
        centroids = new_centroids
    
    return centroids, labels
