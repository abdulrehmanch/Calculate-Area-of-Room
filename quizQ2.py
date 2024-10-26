from shapely.geometry import Polygon, MultiPolygon

polygons = {
    'Lower-left vertical polygon': [(2, 2), (1, 2), (1, 6), (2, 6)],
    'Lower-left L polygon': [(1, 1), (1, 2), (7.5, 2), (7.5, 5.5), (8.5, 5.5), (8.5, 1)],
    'Top-left polygon': [(1, 6), (1, 7), (6, 7), (6, 6)],
    'Middle-top left polygon': [(6.5, 6), (6.5, 7), (8.5, 7), (8.5, 6)],
    'Middle-top right polygon': [(10, 7), (10, 8), (11.5, 8), (11.5, 7)],
    'Far-right vertical polygon': [(12, 7), (12, 9), (13, 9), (13, 7)],
    'Middle-small rectangle': [(9, 5), (9, 6), (10, 6), (10, 5)]
}

# Create Shapely polygons
shapely_polygons = [Polygon(coords) for coords in polygons.values()]

# Create a MultiPolygon from all individual polygons
multi_polygon = MultiPolygon(shapely_polygons)

# Calculate the total area of the MultiPolygon
total_area = multi_polygon.area

# Output the result
print(f"Total area of the MultiPolygon: {total_area} square units")

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Function to plot polygons
def plot_polygon(ax, coordinates, color='lightblue'):
    polygon = Polygon(coordinates, closed=True, edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(polygon)


# Create a plot
fig, ax = plt.subplots()

# Set the plot limits
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)

# Define polygons with their coordinates
polygons = {
    'Lower-left vertical polygon': [(2, 2), (1, 2), (1, 6), (2, 6)],
    'Lower-left L polygon': [(1, 1), (1, 2), (7.5, 2), (7.5, 5.5), (8.5, 5.5), (8.5, 1)],
    'Top-left polygon': [(1, 6), (1, 7), (6, 7), (6, 6)],
    'Middle-top left polygon': [(6.5, 6), (6.5, 7), (8.5, 7), (8.5, 6)],
    # 'Middle-top right polygon': [(10, 7), (10, 8), (11.5, 8), (11.5, 7)],
    # 'Far-right vertical polygon': [(12, 7), (12, 9), (13, 9), (13, 7)],
    # 'Middle-small rectangle': [(9, 5), (9, 6), (10, 6), (10, 5)]
}

# Plot each polygon
for name, coords in polygons.items():
    plot_polygon(ax, coords)

# Add labels and grid
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

# Show the plot
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
