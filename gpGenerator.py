#%% Importing 
import numpy as np 
from scipy.sparse.linalg import eigs
import matplotlib.pyplot as plt

#%% Writing covariance functions
def covgp(x,y,sigma):
    x=np.reshape(x,(np.size(x),1))
    y=np.reshape(y,(np.size(y),1))
    return np.exp(-1/2*(x-y).T@(x-y)/sigma**2)


#%% Functions to find the eigenfunctions/values
def geneigen(x,Neig,sigma,dx):
    # x contains the the grid points with (N,1) shape
    # NNeig is the number of eigenvectors that we want to keep
    # dx is the length of mesh in 1D and Area in the 2D case
    A=np.zeros((len(x),len(x)))
    for index1 in range(len(x)):
        for index2 in range(len(x)):
            A[index1,index2]=covgp(x[index1],x[index2],sigma)*dx
    eigenvalues,eigenvectors=eigs(A,Neig)
    return  np.real(eigenvalues),np.real(eigenvectors),A
  



#%%
# function to generate 1D gp field
def gengpprocess(eigenvalues,eigenvectors,Neig,scale):
    # x is the input grid
    zeta=np.random.normal(loc=0,scale=scale,size=(Neig,))
    gp=(zeta*np.sqrt(eigenvalues)).reshape(1,Neig)@(eigenvectors.T)

    return gp
