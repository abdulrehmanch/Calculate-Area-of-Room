from shapely.geometry import Polygon
import pandas as pd


def create_polygons(coordinates):
    """Create polygons from given coordinates."""
    polygons = {}
    for name, coords in coordinates.items():
        polygons[name] = Polygon(coords)
    return polygons


def calculate_distances(polygons):
    """Calculate distances between polygons."""
    distances = {}
    names = list(polygons.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            poly1 = polygons[names[i]]
            poly2 = polygons[names[j]]
            distance = poly1.distance(poly2)
            distances[(names[i], names[j])] = distance

    return distances


def summarize_polygons(polygons):
    """Summarize polygon details."""
    summary = []
    for name, poly in polygons.items():
        # Coordinates
        coords = list(poly.exterior.coords)
        # Length and width are calculated based on the bounding box
        length = poly.bounds[2] - poly.bounds[0]  # Xmax - Xmin
        width = poly.bounds[3] - poly.bounds[1]  # Ymax - Ymin
        summary.append({
            "Polygon": name,
            "Coordinates": coords,
            "Length (units)": length,
            "Width (units)": width
        })
    return summary


# Define the coordinates for each polygon
coordinates = {
    "Polygon 1": [(0, 1), (7, 1), (7, 0), (0, 0)],
    "Polygon 2": [(1, 0), (6, 0), (6, 1), (1, 1)],
    "Polygon 3": [(1, -3), (6, -3), (6, -2), (1, -2)],
    "Polygon 4": [(0, -4), (1, -4), (1, -3), (0, -3)],
    "Polygon 5": [(3, -6), (5, -6), (5, -5), (3, -5)],
    "Polygon 6": [(3, -7), (5, -7), (5, -6), (3, -6)],
    "Polygon 7": [(8, 6), (11, 6), (11, 5), (8, 5)],
    "Polygon 8": [(9, 5), (12, 5), (12, 4), (9, 4)],
}

# Create polygons
polygons = create_polygons(coordinates)

# Calculate distances
distances = calculate_distances(polygons)

# Create a summary table for distances
distance_table = []
for (poly1, poly2), dist in distances.items():
    distance_table.append({
        "Polygon Pair": f"{poly1} - {poly2}",
        "Distance (units)": dist
    })

# Convert to DataFrame for better visualization
distance_df = pd.DataFrame(distance_table)
print("Distance Summary:")
print(distance_df)

# Summarize polygons
polygon_summary = summarize_polygons(polygons)

# Convert to DataFrame for better visualization
polygon_df = pd.DataFrame(polygon_summary)
print("\nPolygon Summary:")
print(polygon_df)
