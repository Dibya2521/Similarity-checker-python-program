import csv
from geopy.distance import geodesic
from Levenshtein import distance as lev_distance
from scipy.spatial import cKDTree

# Function to check if two names are similar
def is_similar(name1, name2):
    return lev_distance(name1, name2) <= 5

# Function to check if two coordinates are close to each other
def is_close(coord1, coord2):
    return geodesic(coord1, coord2).meters <= 200

def main():
    # List to store the entries read from the input CSV file
    entries = []
    
    # Read the entries from the input CSV file
    with open("input.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            entries.append(row)

    # print("Entries read from file:", len(entries))
    
    # Create a KD-Tree from the latitudes and longitudes of the entries
    coords = [(float(entry["latitude"]), float(entry["longitude"])) for entry in entries]
    kdtree = cKDTree(coords)
    
    # Iterate over each entry, and check if it's close and similar to any other entry
    for i, entry in enumerate(entries):
        lat, lng = float(entry["latitude"]), float(entry["longitude"])
        distances, indices = kdtree.query((lat, lng), 2)
        for j, index in enumerate(indices):
            if index != i and is_close((lat, lng), coords[index]) and is_similar(entry["name"], entries[index]["name"]):
                # Mark the two entries as similar
                entry["is_similar"] = 1
                entries[index]["is_similar"] = 1
                # print(f"{i} and {index} are similar")
                
    # Write the entries to the output CSV file, with the 'is_similar' column added
    with open("output.csv", "w", newline = '') as file:
        fieldnames = [ "name", "latitude", "longitude", "is_similar"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in entries:
            if "is_similar" in row:
                row["is_similar"] = 1
            else:
                row["is_similar"] = 0
            writer.writerow(row)

    # print("Output written to file")

if __name__ == "__main__":
    main()

