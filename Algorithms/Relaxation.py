
import numpy as np
import matplotlib.pyplot as plt

def nlm_mapping(data, num_dims=2, max_iter=1500, epsilon=1e-7, learning_rate=0.01):
    num_samples, num_features = data.shape

    # Scale down the data matrix otherwise I encountered an overflow msg which i don't know why
    data = data / np.max(data)

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

        # Update the coordinates of the embedded points using the relaxation method
        for i in range(num_samples):
            for j in range(num_samples):
                if i != j:
                    diff = embedding[i] - embedding[j]
                    factor = (1 - np.sqrt((embedded_distances[i, j] / pairwise_distances[i, j]))) / (1 + embedded_distances[i, j])
                    scale = 0.1
                    embedding[i] -= diff * scale * factor
                    embedding[j] -= diff * factor * scale

        # Compute the stress function
        stress = np.sum((pairwise_distances - embedded_distances) ** 2) / np.sum(pairwise_distances ** 2)

        # Check for convergence
        if iter > 0 and np.abs(stress - prev_stress) < epsilon:
            break

        prev_stress = stress

    return embedding

data1 = np.loadtxt('6\\rc4.txt')  # Load your data from a file
data2 = np.loadtxt('6\\sasla20.txt')
embedding5 = nlm_mapping(data1)  # Perform Sammon's NLM
embedding6 = nlm_mapping(data2)
plt.scatter(embedding5[:, 0],embedding5[ :, 1], color='red',label = 'RC4')# Plot the low-dimensional embedding
plt.scatter(embedding6[:,0],embedding6[:,1],color='blue',label='Salsa20')
plt.legend()
plt.title("NLM Relaxation")
plt.show()