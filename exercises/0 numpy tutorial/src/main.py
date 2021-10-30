import numpy as np

# Empty np array
empty_array = np.array(None)
print(empty_array)

# Array filled with zeroes
filled_with_zeros = np.zeros(3, dtype=int)
print(filled_with_zeros)

# Array filled with ones
filled_with_ones = np.ones(3, dtype=int)
print(filled_with_ones)

# Array filled with lists
np_full_array = np.full((3, 2), 2)
print(np_full_array)

# If np array contains given row
np_full_array[1] = [3, 1]
print([3, 2] in np_full_array.tolist())

# Generating string np array to value (integers)
number = 10
array_with_str = np.genfromtxt(np.array([10, 'alelo', number, 1.3]))
print(array_with_str)

# Removing NaN values from array
without_nan_values = array_with_str[np.logical_not(np.isnan(array_with_str))]
print(without_nan_values)

# Remove single dimensional entries from the shape of an array
arr = [[1, 4, 2, 3, 3, 1, 2, 3, 1, 3, 3, 3]]
messed_dimensions = np.array(arr)
print(messed_dimensions.squeeze())

# Finding the occurencies of a sequence in np array
print(repr(messed_dimensions).count('2, 3'))

# Finding the most frequent value in np array
curarr = messed_dimensions.squeeze()
print(np.bincount(curarr).argmax())

# Combining a two and one dimensional np array
one_dim = np.array([1])
two_dim = np.array([1, 2])
print(np.concatenate([one_dim, two_dim]))

# Create combinatory interpolation from two np arrays
first_array = np.array([1, 3, 4])
second_array = np.array([6, 7])
fulled_array = np.array(np.meshgrid(second_array, first_array))
fulled_array = fulled_array.reshape(-1, fulled_array[0].size).T
print(fulled_array)

# Adding border around np array
border_array = np.ones((2,2))
border_array = np.pad(border_array, pad_width=1, mode='constant', constant_values=0)
print(border_array)

# How to compare two np arrays
first_array = np.ones(3)
second_array = np.ones(3)
second_array[1] = -1
print(np.array_equal(first_array, second_array))

# Wether values ara in array
print(-1 in second_array)

# Get 2D diagonals from 3D array
arr = np.arange(3 * 3 * 3).reshape(3, 3, 3)
diag_arr = np.diagonal(arr, axis1 = 1, axis2 = 2)
print(diag_arr)

# Flatten matrix into array
m = np.matrix([[1,2,3], [4,5,6]])
print(m.flatten())

# Flatten 2d np array into 1d array
flatten_arr = arr.reshape(1, -1)
print(flatten_arr)

# Move axes of an array to new position
arr = np.zeros((2, 2, 1))
print(arr)
print(np.moveaxis(arr, 0, -1))

# Interchange two axis of an array
arr = np.ones((2, 2, 1))
changed_axis = np.swapaxes(arr, 0, -1)
print(arr)
print(changed_axis)

# First 10 numbers using binet formula to find fibonacci
sqrt5 = np.sqrt(5)
alpha = (1 + sqrt5) / 2
beta = (1 - sqrt5) / 2
arrn = np.arange(1, 11)
Fn = ((alpha ** arrn) - (beta ** arrn)) / sqrt5
print(Fn)

# Count the number of non-zero values in the array
first = np.ones(11)
first[6:9] = 0
print(np.count_nonzero(first))

# Counts the number of elements to a given axis
axis = 0
arr = np.array([[1, 2, 3], [3, 4, 5]])
print(np.size(arr, axis))

# Trim the trailing zeros from 1d array
print(first)
first[:2] = 0
first[8:] = 0
print(np.trim_zeros(first))

# Change datatype for a given np array
first.dtype = int
print(first.dtype)
first.dtype = float

# Reverse a numpy array
print(first[::-1])

# Make np array read only
first.flags.writeable = False
print(first)



###### Matrices ######

# Getting the maximum value for a given matrix
np.random.seed(0)
mat = np.matrix(np.random.randint(24, size=12).reshape(3, 4))
print(mat.max())

# Getting the minimun value for a given matrix
print(mat.min())

# Finding the number of rows and columns for a given matrix
print('rows=', mat.shape[0], 'columns=', mat.shape[1])

# Create a slice from a given matrix
s_slice = mat[2,2:]
print(s_slice)

# Finding the sum of values of a matrix
print(mat.sum())

# Finding the sum of diagonal of a matrix
print(mat.diagonal().sum())

# Adding or subtracting matrices in python
mat2 = np.matrix(np.random.randint(24, size=12).reshape(3, 4))
mat3 = mat + mat2
print(mat3)

# Ways to add row/column in np array
mat = np.concatenate((mat, np.array([[1,2,3,4]])))
mat = np.concatenate((mat, np.vstack([1,2,3,4])), axis=1)
print(mat)

# Multiply matrices in python
mat2 = mat2.T * mat3
print(mat2)

# Get aigen values for a given matrix
print(np.linalg.eigvals(mat2))

# Determinant of matrix using np
print(np.linalg.det(mat2))

# Inverse of matrix using np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
print(np.linalg.inv(A))

# Frequency of unique values inside of matrix
mat2 = np.matrix(np.random.randint(4, size=12).reshape(3, 4))
unique = np.unique(mat2)
print(unique)

# Multiply matrices of complex numbers using NumPy in Python
first = np.array([[2 + 1j, 1 + 2j], [1, 2 + 4j]])
second = np.array([[1 + 2j, 2 + 1j], [2 - 1j, 2 - 2j]])
third = np.dot(first, second)
print(third)

# Outer product of two given vectors using NumPy
first = np.arange(4)
second = np.random.randint(3, size=4)
third = np.outer(first, second)
print(third)

# Inner, outer and cross product
mat = np.matrix(np.arange(16).reshape(4, 4))
print('Different products mats')
print(mat, '\n', third)
print(np.inner(mat, third))
print(np.cross(mat.reshape(-1, 2), third.reshape(-1, 2)))

# Calculate the covariance matrix from two given arrays
print(first, second)
cov_mat = np.cov(first, second)
print(cov_mat)

# Convert covariance matrix to correlation matrix
print(np.corrcoef(cov_mat))

# Compute the kronecker product of two multidimension matrix
print(np.kron(mat, np.corrcoef(cov_mat)))

# Convert matrix into a list
first_list = mat2.ravel().tolist()
print(first_list)

##### Numpy Indexing #####

# Convert all values that doesn't satisfy the rule
first[first < 2] = 0
print(first)

# Return the indices of elements where the given condition is satisfied
indices = np.where(first > 2)[0]
print(indices)

# Replace NaN values with mean values of columns
first = np.arange(30, dtype=float).reshape(5, 6)
first[3,0:2] = np.NaN
inds = np.where(np.isnan(first))
first[inds] = np.take(np.nanmean(first, axis=0), inds[1])
print(first)

# Replace negative values with zero in np array
first = first.ravel()[:15]
first[4:7] = [-1, -2, -10]
first[first < 0] = 0
print(first)

# How to get values of an NumPy array at certain index positions
inds = [1, 3, 6]
print(first[inds])

# Indices of elements with zero as value
inds = np.where(first == 0)
print(inds[0])

# Remove column with non numeric values in np array
first = first.reshape(-1, 3)
first[2,2] = np.nan
first = np.delete(first, np.where(np.isnan(first))[1], axis=1)
print(first)

# Access differente rows of multidimensional np array
rows = [1, 3]
second = first[rows]
print(second)

# Get row numbers of np array having elements larger than x
x = 1
print(np.where(np.any(first > x, axis=1))[0])

# Get filled the diagonals of the numpy array
np.fill_diagonal(first, 111)
print(first)

# Check elements present in the NumPy array
print(1 in first)

##### Numpy Linear algebra #####

# Find the norm of a matrix or vector
print(np.linalg.norm(first))

# Calculate the QR decomposition of a given matrix
q, r= np.linalg.qr(first)
print('q=', q, '\nr=', r)

# Compute the condition number of a given matrix
print(np.linalg.cond(first))

# Compute the eigenvalues and right eigenvectors of a given square array
first = np.resize(first, (3,3))
eig_vals, eig_vec = np.linalg.eig(first)
print(eig_vals)
print(eig_vec)

# Calculating the euclidean distance using np
first = np.resize(first, (1, 3))
second = np.resize(second, (1, 3))
distance = np.linalg.norm(first - second)
print(distance)


##### NumPy Random #####

# Create a Numpy array with random values
first = np.random.rand(12)
print(first)

# How to choose elements from the list with different probability using NumPy
number = np.random.choice(first)
print(number)

# How to get weighted random choice in Python
weights = np.array([1, 1, 1, 1, 1, 2, 2, 4, 1, 4, 1, 5])
number = np.random.choice(first, p=weights/weights.sum())
print(number)

# Generate random numbers from the uniform distribution
print(np.random.choice(10, 12))

# Get Random Elements from geometric distribution
print(np.random.geometric(.2, 20))

# Get Random Elements from laplace distribution
print(np.random.laplace(0.0, 1.0, 10))

# Return a Matrix of random values from a uniform distribution
print(np.matrix(np.random.uniform(0, 1, 12)).reshape(3, 4))

# Return a Matrix of random values from a Gaussian distribution
print(np.matrix(np.random.normal(0, 1, 12)).reshape(3, 4))


##### Numpy sorting and searching #####

# How to get the indices of the sorted array using NumPy in Python
first = np.rint(first * 10)
sort_ind = np.argsort(first)
print('The indices of a sorted array:', sort_ind)

# Finding the k smallest values of a NumPy array
k = first[np.where(sort_ind == 0)]
print(first, 'The smallest is:', k.squeeze())

# How to get the n-largest values of an array using NumPy
n = 3
print(first[np.where(sort_ind == first.size - n)].squeeze())

# Sort the values in a matrix
first = first.reshape(3, -1)
print(np.sort(first))

# Filter out integers from float numpy array
first[1,2] = 1.2
first[0,0] = 2.3
print('The integers are:', first[first == first.astype(int)])
print('The floats are:', first[first != first.astype(int)])

# Find the indices into a sorted array
second = np.sort(first.reshape(1, -1))
print(np.argsort(second))


##### Mathmatics using numpy #####

# How to get element-wise true division of an array using Numpy
first = first.ravel()
print(np.true_divide(first, 10))

# How to calculate the element-wise absolute value of NumPy array
first[3:7] *= -1
print(np.absolute(first))

# Compute the negative of the NumPy array
second = first[:] * -1
print(second)

# Multiply 2d numpy array corresponding to 1d array
first = first.reshape(3, -1)
second = np.array([1.2, 1.1, 2.3, 1])
print(first * second)

# Computes the inner product of two arrays
print(np.inner(first, second))

# Compute the nth percentile of the NumPy array
print(np.percentile(second, 30))

# Calculate the n-th order discrete difference along the given axis
print(np.diff(second, n=2))

# Calculate the sum of all columns in a 2D NumPy array
print(np.sum(first, axis=0))

# Calculate average values of two given NumPy arrays
arr1 = np.array([1,3])
arr2 = np.array([2,1])
print((arr1 + arr2) / 2)

# How to compute numerical negative value for all elements in a given NumPy array
print(np.negative(second))

# How to get the floor, ceiling and truncated values of the elements of a numpy array
print(np.floor(second))
print(np.ceil(second))
print(np.trunc(second))

# Get the round number close to the nearest integer
print(np.rint(second))

# Getting the round of values from a matrix
print(first.round())

# Determine the positive square-root of an array
print(np.sqrt(second))

# Evaluate Einstein’s summation convention of two multidimensional NumPy arrays
print(np.einsum('mk,kn', first, first.T))


##### Statistical part numpy #####

# Compute the median of the flattened NumPy array
print(np.median(first.ravel()))

# Find Mean of a List of Numpy Array
print(np.mean(first.ravel()))

# Calculate the mean of array ignoring the NaN value
first = first.ravel()
print(np.mean(first[first != np.nan]))

# Get the mean value from given matrix
first = first.reshape(3, -1)
print(np.mean(first))

# Compute the variance of the NumPy array
first = first.ravel()
print(np.var(first))

# Compute the standard deviation of the NumPy array
print(np.std(first))

# Compute pearson product-moment correlation coefficients of two given NumPy arrays
print(np.corrcoef(arr1, arr2))

# Calculate the mean across dimension in a 2D NumPy array
# Just calcualte the mean of a matrix and specify the different axis
first = first.reshape(3,-1)
print(np.mean(first, axis=1))

# Calculate the average, variance and standard deviation in Python using NumPy
# The variance and standard deviation is alredy made before, so i'll just put the average
print(np.average(first))

# Describing the array in python would be just to print all the functions return in
# a organizerd manner, so I'll pass this one because it's just to print it pretty


import numpy.polynomial as poly

##### Questions on Polynomial #####

# Define a polynomial function
poly1 = poly.Polynomial([31, 3, 2])
print(poly1)

# How to add one polynomial to another using NumPy in Python
poly2 = poly.Polynomial([1, 1, 3])
print(poly1 + poly2)

# How to subtract one polynomial to another using NumPy in Python
print(poly1 - poly2)

# How to multiply a polynomial to another using NumPy in Python
print(poly1 * poly2)

# How to divide a polynomial to another using NumPy in Python
arr1 = poly.Polynomial([1, 2])
arr2 = poly.Polynomial([2, 2])
print(arr1 // arr2)

# Find the roots of the polynomials using NumPy
print(np.roots([31, 3, 2]))

# Evaluate a 2-D polynomial series on the Cartesian product
print(poly.polynomial.polygrid2d(arr1, arr2, poly2))

# Evaluate a 3-D polynomial series on the Cartesian product
print(poly.polynomial.polygrid3d(arr1, arr2, [3, 2], poly2))


##### Questions on NumPy Strings #####

# Repeat all the elements of a NumPy array of strings
arr = np.array(['Banana', 'Manga', 'Flor', 'Macaco'])
print(np.char.multiply(arr, 2))

# How to split the element of a given NumPy array with spaces
arr = np.array(['Semi Automatico', 'Coisa Alheia', 'Outra Coisa'])
print(np.char.split(arr))

# How to insert a space between characters of all the elements of a given NumPy array
print(np.char.join(' ', arr))

# Find the length of each string element in the Numpy array
print(np.vectorize(len)(arr))

# Swap the case of an array of string
print(np.char.swapcase(arr))

# Change the case to uppercase of elements of an array
print(np.char.upper(arr))

# Change the case to lowercase of elements of an array
print(np.char.lower(arr))

# Join String by a seperator
print(np.char.join('.', arr))

# Check if two same shaped string arrays one by one
print(np.array_equal(arr, arr))

# Count the number of substrings in an array
print(np.char.count(arr, ' '))

# Find the lowest index of the substring in an array
print(np.char.find(arr, ' '))

# Get the boolean array when values end with a particular character
print(np.char.endswith(arr, 'o'))


##### More Questions on Numpy #####

# Different ways to convert a Python dictionary to a NumPy array
simple_dict = {'aaa': 333, 'bbb': 666}
keys = np.fromiter(simple_dict.keys(), dtype=(str, 3))
values = np.fromiter(simple_dict.values(), dtype=int)
print(keys, values)

# How to convert a list and tuple into NumPy arrays
# The list conversion is already done extensively into this files, so I'll only do the tuple
tuple_list = (3, 1, 3, 3, 1, 2, 3)
print(np.array(tuple_list))

# Ways to convert array of strings to array of floats
arr = np.array(['1.3', '3.1321', '1.23131', '93.234']).astype(float)
print(arr)

# Convert a NumPy array into a csv file
np.savetxt('data.csv', first, delimiter=',')
print(first)

# Convert an image to NumPy array and save it to CSV file using Python
from PIL import Image
image = Image.open('images/4 leaf clover.jpg')
arr = np.asarray(image)
arr = arr.reshape(arr.shape[0], arr.shape[1] * arr.shape[2])
np.savetxt('image.csv', arr, delimiter=',')

# Save np array to text file
np.savetxt('file.txt', first)

# Load from text file
another = np.loadtxt('file.txt')
print(np.array_equal(another, first))

# Plot line graph from np array
import matplotlib.pyplot as plt
plt.title('line graph')
plt.plot(np.arange(12).reshape(3, 4), first, color='red')
plt.show()

# Create histogram using np array
first = np.arange(6)
plt.bar(first, height = 100)
plt.show()