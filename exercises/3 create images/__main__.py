import numpy as np
import matplotlib.pyplot as plt

# Criando paraboloid

theta = np.linspace(0, 2 * np.pi, 10)
z = np.linspace(0, 1, 10)

r = np.sqrt(4 * z).reshape(-1, 1)

theta, z = np.meshgrid(theta, z)

x = r * np.cos(theta) * 4
y = r * np.sin(theta)
z = z

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z)
ax.plot_wireframe(x, y, z)
plt.xlim([-8, 8])
plt.ylim([-8, 8])
plt.show()

# # Criando função seno

x = np.linspace(0, 20, 10)
y = x.copy().T
x, y = np.meshgrid(x, y)
z = np.sin(x)

def rotate(x, y, angle):
    angle = np.radians(angle)
    val_x = x * np.cos(angle) - y * np.sin(angle)
    val_y = x * np.sin(angle) + y * np.cos(angle)
    return val_x, val_y

x, z = rotate(x, z, 10)

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)
plt.xlim([0, 20])
plt.ylim([0, 20])
plt.show()

# Criando função gaussiana

def gaussian_3d(x, y, mx, my, sx, sy):
    exp = - (((x - mx) ** 2) / (2 * sx ** 2) + ((y - my) ** 2) / (2 * sy ** 2))
    return (1 / (2 * np.pi * sx * sy)) * (np.e ** exp)

def gaussian_3d_with_rotate(axis, mx, my, sx, sy, theta = 0):
    x = axis
    y = axis.copy().T
    x, y = np.meshgrid(x, y)
    z = gaussian_3d(x, y, mx, my, sx, sy)
    
    x, z = rotate(x, z, np.radians(theta))
    
    return x, y, z

axis = np.linspace(0, 20, 10)
x, y, z = gaussian_3d_with_rotate(axis, 10, 10, 2, 2, 1)

print(x)
print(y)
print(z)

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)
ax.plot_wireframe(x, y, z)
plt.show()