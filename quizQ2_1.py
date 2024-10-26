import random
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, LineString, MultiPolygon
from shapely.ops import polygonize, unary_union

# Function to calculate the slope of an edge
def calculate_slope(p1, p2):
    if p2[0] - p1[0] == 0:  # Avoid division by zero (vertical line)
        return float('inf')  # Use infinity for vertical lines
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

# Function to extend a line segment
def extend_line(line, factor):
    """Extend the line in both directions by a specified factor."""
    x_coords, y_coords = line.xy
    start = (x_coords[0], y_coords[0])
    end = (x_coords[1], y_coords[1])

    # Calculate direction vector
    direction = np.array(end) - np.array(start)
    direction = direction / np.linalg.norm(direction)  # Normalize

    # Extend in both directions
    new_start = (start[0] - direction[0] * factor, start[1] - direction[1] * factor)
    new_end = (end[0] + direction[0] * factor, end[1] + direction[1] * factor)

    return LineString([new_start, new_end])

# Generate random colors for each polygon
def random_color():
    return random.random(), random.random(), random.random()

def calculate_area(polygon_objs, wall_width=2, extend_factor=2):
    # Group edges by slope
    slope_groups = defaultdict(list)
    extended_edges = []

    for poly in polygon_objs:
        coords = list(poly.exterior.coords)
        for i in range(len(coords) - 1):
            slope = calculate_slope(coords[i], coords[i + 1])
            edge = LineString([coords[i], coords[i + 1]])
            if edge.length < wall_width:
                continue
            extended_edge = extend_line(edge, factor=extend_factor)  # Extend the edge
            group = "A" if slope > 0 else "B"
            slope_groups[group].append(extended_edge)
            extended_edges.append(extended_edge)

    # Create polygons from the extended edges and intersection points
    u = unary_union(extended_edges)
    new_polygons = list(polygonize(u))

    polygon_colors = [random_color() for _ in new_polygons]

    # Plotting
    fig, ax = plt.subplots()

    # Plot original polygons with dotted green lines
    for poly in polygon_objs:
        x, y = poly.exterior.xy
        ax.plot(x, y, linestyle=':', color='blue', linewidth=2)

    # Plot extended edges
    for edge in extended_edges:
        x_values, y_values = edge.xy
        ax.plot(x_values, y_values, color='gray', linewidth=1)

    # Plot new polygons formed from extended lines with random colors and display their areas
    for new_poly, color in zip(new_polygons, polygon_colors):
        # Calculate and plot only for new polygons that do not overlap with the original
        if new_poly.centroid.intersects(MultiPolygon(polygon_objs)):
            continue
        x, y = new_poly.exterior.xy
        ax.fill(x, y, alpha=0.5, fc=color, edgecolor='black')

        # Display the area at the polygon's centroid
        area = new_poly.area
        centroid = new_poly.centroid
        ax.text(centroid.x, centroid.y, f"{area:.2f}", fontsize=8, ha='center', color='black')

    # Set aspect ratio and add title
    ax.set_aspect('equal', 'box')
    plt.title('Polygons with Extended Edges, Randomly Colored New Polygons, and Area Labels')
    plt.show()

# Define the original polygons
polygons_1 = {
    'Lower-left vertical polygon': [(2, 2), (1, 2), (1, 6), (2, 6)],
    'Lower-left L polygon': [(1, 1), (1, 2), (7.5, 2), (7.5, 5.5), (8.5, 5.5), (8.5, 1)],
    'Top-left polygon': [(1, 6), (1, 7), (6, 7), (6, 6)],
    'Middle-top left polygon': [(6.5, 6), (6.5, 7), (8.5, 7), (8.5, 6)],
}

# Create Shapely Polygon objects
polygons_objs = [Polygon(coords) for coords in polygons_1.values()]
calculate_area(polygons_objs)

# Define the original polygons
polygons_2 = {
    'A': [(9, 3), (9.5, 3), (9.5, 8), (9, 8)],
    'B': [(9, 8.5), (9, 9), (11.5, 9), (11.5, 8.5)],
    'C': [(12, 9), (12.5, 9), (12.5, 5.5), (12, 5.5)],
    'D': [(10, 4.5), (10, 4), (12.5, 4), (12.5, 4.5)]
}

# Create Shapely Polygon objects
polygons_objs2 = [Polygon(coords) for coords in polygons_2.values()]
calculate_area(polygons_objs2)
