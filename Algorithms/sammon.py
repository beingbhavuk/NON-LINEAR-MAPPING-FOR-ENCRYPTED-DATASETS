import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

# Function to calculate the Euclidean distance between two points
def euclideanDistance(point1, point2):
    distance = np.linalg.norm(point1 - point2)
    return distance

# Function to perform Sammon's mapping using MDS
def sammonsMapping(data, targetDimension):
    # Compute pairwise distance matrix
    distanceMatrix = np.zeros((len(data), len(data)))
    for i in range(len(data)):
        for j in range(len(data)):
            distanceMatrix[i][j] = euclideanDistance(data[i], data[j])

    # Perform MDS on the distance matrix
    mds = MDS(n_components=targetDimension, metric=True, max_iter=100, eps=1e-9, random_state=0)
    coordinates = mds.fit_transform(distanceMatrix)

    return coordinates


data1 = np.loadtxt('1\\aes.txt')
data2 = np.loadtxt('1\\des.txt')
# Assign labels to each class
labels1 = np.zeros(data1.shape[0])
labels2 = np.ones(data2.shape[0])

# Combine the data and labels
combined_data = np.concatenate((data1, data2), axis=0)
combined_labels = np.concatenate((labels1, labels2), axis=0)

# Create the custom dataset
custom_dataset = {'data': combined_data, 'target': combined_labels}
data = custom_dataset['data']

# Perform Sammon's mapping
targetDimension = 2
coordinates = sammonsMapping(data, targetDimension)

# Plotting
plt.scatter(coordinates[:, 0], coordinates[:, 1], c=custom_dataset['target'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Sammon's Mapping")

# Add legend with label names
plt.scatter([], [], c='k')  # Create empty scatter plot for each label
plt.legend()

plt.show()
