import matplotlib.pyplot as plt
import numpy as np

# Coordinates for the polygons
polygons = [
    # Left Vertical Polygon
    [(9, 3), (9.5, 3), (9.5, 8), (9, 8)],

    # Top Horizontal Polygon
    [(9, 8.5), (9, 9), (11.5, 9), (11.5, 8.5)],

    # Right Vertical Polygon
    [(12, 9), (12.5, 9), (12.5, 5.5), (12, 5.5)],

    # Bottom Horizontal Polygon
    [(10, 4.5), (10, 4), (12.5, 4), (12.5, 4.5)]
]

# Set up plot
plt.figure(figsize=(6, 6))

# Function to plot polygons
for polygon in polygons:
    polygon_np = np.array(polygon + [polygon[0]])  # Close the polygon by repeating the first point
    plt.plot(polygon_np[:, 0], polygon_np[:, 1], 'b-', lw=2)  # Polygon outline
    plt.fill(polygon_np[:, 0], polygon_np[:, 1], 'lightblue', edgecolor='black')  # Fill polygon

# Setting axes and grid
plt.xlim(8, 14)
plt.ylim(0, 10)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Labels
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Polygon Plot")

# Show the plot
plt.show()
