import numpy as np
import matplotlib.pyplot as plt

def hamming_distance(point1, point2):
    return np.sum(point1 != point2)

def sammons_mapping2(data, num_dims=2, max_iter=500, epsilon=1e-3, learning_rate=0.001):

    num_samples, num_features = data.shape

    # Compute pairwise Hamming distances between data points
    pairwise_distances = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        for j in range(i+1, num_samples):
            pairwise_distances[i, j] = hamming_distance(data[i], data[j])
            pairwise_distances[j, i] = pairwise_distances[i, j]

    # Initialize the low-dimensional embedding randomly
    embedding = np.random.randn(num_samples, num_dims)

    # Initialize stress
    prev_stress = None
    stress = 0

    # Perform iterations
    for iter in range(max_iter):
        # Compute pairwise distances between embedded points
        embedded_distances = np.zeros((num_samples, num_samples))
        for i in range(num_samples):
            for j in range(i+1, num_samples):
                embedded_distances[i, j] = np.linalg.norm(embedding[i] - embedding[j])
                embedded_distances[j, i] = embedded_distances[i, j]

        # Compute the gradient of the stress function
        gradient = np.zeros((num_samples, num_dims))
        for i in range(num_samples):
            for j in range(num_samples):
                if i != j:
                    projectedDistance = embedded_distances[i, j]
                    originalDistance = pairwise_distances[i, j]
                    for k in range(num_dims):
                        gradient[i, k] += (projectedDistance - originalDistance) * \
                                          (embedding[i, k] - embedding[j, k]) / \
                                          (projectedDistance * originalDistance * (originalDistance - projectedDistance))

        # Update the coordinates of the embedded points
        embedding -= learning_rate * gradient

        # Compute the stress function
        prev_stress = stress
        stress = np.sum((pairwise_distances - embedded_distances) ** 2) / np.sum(pairwise_distances ** 2)

        # Check for convergence
        if prev_stress is not None and np.abs(prev_stress - stress) < epsilon:
            break

    return embedding

data3 = np.loadtxt('2\\chacha20.txt')  # Load your data from a file
data4 = np.loadtxt('2\\blowfish.txt')
embedding3 = sammons_mapping2(data3)  # Perform Sammon's NLM
embedding4 = sammons_mapping2(data4)
plt.scatter(embedding3[:, 0],embedding3[ :, 1], color='red',label = 'chacha20')# Plot the low-dimensional embedding
plt.scatter(embedding4[:,0],embedding4[:,1],color='blue',label='blowfish')
plt.legend()
plt.title("The White Variation")
plt.show()

