import csv
import matplotlib.pyplot as plt

def normalize_flavor(flavor):
    # Normalize flavor names
    flavor = flavor.lower().strip()
    if 'chocolate' in flavor:
        return 'chocolate'
    elif 'vanilla' in flavor:
        return 'vanilla'
    elif 'strawberry' in flavor:
        return 'strawberry'
    # Add more normalization rules as needed
    return flavor

# Initialize dictionaries to store flavor counts
flavor_counts = {}
flavor1_counts = {}
flavor2_counts = {}
flavor3_counts = {}

# Open the CSV file and read the data
with open("icecream.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        flavor1 = normalize_flavor(row['#1'])
        flavor2 = normalize_flavor(row['#2'])
        flavor3 = normalize_flavor(row['#3'])

        # Count all flavors
        for flavor in [flavor1, flavor2, flavor3]:
            if flavor in flavor_counts:
                flavor_counts[flavor] += 1
            else:
                flavor_counts[flavor] = 1

        # Count Flavor 1
        if flavor1 in flavor1_counts:
            flavor1_counts[flavor1] += 1
        else:
            flavor1_counts[flavor1] = 1

        # Count Flavor 2
        if flavor2 in flavor2_counts:
            flavor2_counts[flavor2] += 1
        else:
            flavor2_counts[flavor2] = 1

        # Count Flavor 3
        if flavor3 in flavor3_counts:
            flavor3_counts[flavor3] += 1
        else:
            flavor3_counts[flavor3] = 1

# Step 1: Create a bar graph for all flavors
plt.figure(figsize=(14, 6))
plt.bar(flavor_counts.keys(), flavor_counts.values(), color='skyblue')
plt.xlabel('Flavors')
plt.ylabel('Count')
plt.title('All Favorite Ice Cream Flavors')
plt.xticks(rotation=45, ha='right', fontsize=8)  # Adjust rotation and font size
plt.tight_layout()

# Show the bar graph for all flavors
plt.show()

# Step 2: Create bar graphs for Flavor #1, Flavor #2, and Flavor #3 sequentially
plt.figure(figsize=(10, 6))

# Plot Flavor 1
plt.bar(flavor1_counts.keys(), flavor1_counts.values(), color='lightgreen')
plt.xlabel('Flavors')
plt.ylabel('Count')
plt.title('Favorite Flavor #1')
plt.xticks(rotation=45, ha='right', fontsize=8)  # Adjust rotation and font size
plt.tight_layout()

# Show the bar graph for Flavor 1
plt.show()

# Plot Flavor 2
plt.figure(figsize=(10, 6))
plt.bar(flavor2_counts.keys(), flavor2_counts.values(), color='salmon')
plt.xlabel('Flavors')
plt.ylabel('Count')
plt.title('Favorite Flavor #2')
plt.xticks(rotation=45, ha='right', fontsize=8)  # Adjust rotation and font size
plt.tight_layout()

# Show the bar graph for Flavor 2
plt.show()

# Plot Flavor 3
plt.figure(figsize=(10, 6))
plt.bar(flavor3_counts.keys(), flavor3_counts.values(), color='lightcoral')
plt.xlabel('Flavors')
plt.ylabel('Count')
plt.title('Favorite Flavor #3')
plt.xticks(rotation=45, ha='right', fontsize=8)  # Adjust rotation and font size
plt.tight_layout()

# Show the bar graph for Flavor 3
plt.show()
