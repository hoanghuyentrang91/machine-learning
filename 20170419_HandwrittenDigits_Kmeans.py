# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:46:39 2017

@author: Kara

This code is used for K-means Clustering
"""

# %reset
# import needed libraries, especially "minst"
import numpy as np 
from mnist import MNIST
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
#from sklearn.preprocessing import normalize


from display_network import *

# load the handwritten digit images
mndata = MNIST('MNIST/')
mndata.load_testing()
X = mndata.test_images
X0 = np.asarray(X)[:1000,:]/256.0
X = X0

# there are 10 clusters for 10 numbers from 0 to 9 
K = 10
kmeans = KMeans(n_clusters=K).fit(X)

pred_label = kmeans.predict(X)



print(type(kmeans.cluster_centers_.T))
print(kmeans.cluster_centers_.T.shape)
A = display_network(kmeans.cluster_centers_.T, K, 1)

f1 = plt.imshow(A, interpolation='nearest', cmap = "jet")
f1.axes.get_xaxis().set_visible(False)
f1.axes.get_yaxis().set_visible(False)
plt.show()
# plt.savefig('a1.png', bbox_inches='tight')

# a colormap and a normalization instance
cmap = plt.cm.jet
norm = plt.Normalize(vmin=A.min(), vmax=A.max())

# map the normalized data to colors
# image is now RGBA (512x512x4) 
image = cmap(norm(A))

# This code is used to save the image
import scipy.misc
scipy.misc.imsave('aa.png', image)



print(type(pred_label))
print(pred_label.shape)
print(type(X0))




N0 = 20;
X1 = np.zeros((N0*K, 784))
X2 = np.zeros((N0*K, 784))


for k in range(K):
    Xk = X0[pred_label == k, :]

    center_k = [kmeans.cluster_centers_[k]]
    neigh = NearestNeighbors(N0).fit(Xk)
    dist, nearest_id  = neigh.kneighbors(center_k, N0)
    
    X1[N0*k: N0*k + N0,:] = Xk[nearest_id, :]
    X2[N0*k: N0*k + N0,:] = Xk[:N0, :]
       

# This code is used to display 20 random results of data with centers
plt.axis('off')
A = display_network(X2.T, K, N0)
f2 = plt.imshow(A, interpolation='nearest' )
plt.gray()
plt.show()
# This code is used to save the image
scipy.misc.imsave('bb.png', A)


# This code is used to display 20 nearest results of data with centers
plt.axis('off')
A = display_network(X1.T, 10, N0)
# This code is used to save the image
scipy.misc.imsave('cc.png', A)
f2 = plt.imshow(A, interpolation='nearest' )
plt.gray()
plt.show()