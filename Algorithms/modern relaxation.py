import numpy as np
import matplotlib.pyplot as plt

def relaxation_frame_algorithm(data, num_dims=2, max_iter=200, epsilon=1e-6, learning_rate=0.07):
    num_samples, num_features = data.shape

    # Compute pairwise Euclidean distances between data points
    pairwise_distances = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        for j in range(i+1, num_samples):
            pairwise_distances[i, j] = np.linalg.norm(data[i] - data[j])
            pairwise_distances[j, i] = pairwise_distances[i, j]
    
    # Define reference points as a subset of the data points
    reference_points = data[:num_samples, :num_dims]

    # Initialize the low-dimensional embedding randomly
    embedding = np.random.randn(num_samples, num_dims)

    # Perform iterations
    for iter in range(max_iter):
        # Compute pairwise distances between embedded points and reference points
        embedded_distances = np.zeros((num_samples, num_samples))
        for i in range(num_samples):
            for j in range(num_dims):
                embedded_distances[i, j] = np.linalg.norm(embedding[i] - reference_points[j])

        # Update the coordinates of the embedded points using the relaxation algorithm
        for i in range(num_samples):
            for j in range(num_samples):
                if i != j:
                    diff = embedding[i] - embedding[j]
                    if i >= num_dims: i = num_dims - 1
                    if j >= num_dims: j = num_dims - 1
                    factor = (pairwise_distances[i, j] - embedded_distances[i, :].sum() + embedded_distances[i, j]) \
                                 / pairwise_distances[i, j] if pairwise_distances[i, j] != 0 else 0
                    embedding[i] -= diff * learning_rate * factor    
        # Compute the stress function        
        stress = np.sum((pairwise_distances - embedded_distances) ** 2) / np.sum(pairwise_distances ** 2)
        # Check for convergence
        if iter > 0 and np.abs(stress - prev_stress) < epsilon:
            break

        prev_stress = stress

    return embedding


def relaxation_perturbation_algorithm(data, num_dims=2, max_iter=10, epsilon=1e-9, learning_rate=0.5, perturbation_scale=0.1):
    num_samples, num_features = data.shape

    # Compute pairwise Euclidean distances between data points
    pairwise_distances = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        for j in range(i+1, num_samples):
            pairwise_distances[i, j] = np.linalg.norm(data[i] - data[j])
            pairwise_distances[j, i] = pairwise_distances[i, j]

    # Initialize the low-dimensional embedding randomly
    embedding = np.random.randn(num_samples, num_dims)

    # Perform iterations
    for iter in range(max_iter):
        # Compute pairwise distances between embedded points
        embedded_distances = np.zeros((num_samples, num_samples))
        for i in range(num_samples):
            for j in range(i+1, num_samples):
                embedded_distances[i, j] = np.linalg.norm(embedding[i] - embedding[j])
                embedded_distances[j, i] = embedded_distances[i, j]

        # Update the coordinates of the embedded points using the relaxation algorithm with perturbations
        for i in range(num_samples):
            for j in range(num_samples):
                if i != j:
                    diff = embedding[i] - embedding[j]
                    perturbation = np.random.randn(num_dims) * perturbation_scale
                    embedding[i] -= diff * learning_rate + perturbation
                    embedding[j] += diff * learning_rate + perturbation

        # Compute the stress function
        stress = np.sum((pairwise_distances - embedded_distances) ** 2) / np.sum(pairwise_distances ** 2)

        # Check for convergence
        if iter > 0 and np.abs(stress - prev_stress) < epsilon:
            break

        prev_stress = stress
    return embedding
data1 = np.loadtxt('1\\sasla20.txt')
data2=  np.loadtxt('1\\chacha20.txt')
embedding_frame_algo = relaxation_frame_algorithm(data1)
embedding_perturbation_algo= relaxation_perturbation_algorithm(data2)
# Plotting
plt.scatter(embedding_frame_algo[:, 0], embedding_frame_algo[:, 1], color='red', label='salsa20')
plt.scatter(embedding_perturbation_algo[:, 0], embedding_perturbation_algo[:, 1], color='blue', label='chacha20')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Advanced Relaxation Algorithms')
plt.show()