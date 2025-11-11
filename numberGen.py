import hashlib

print("Hello, World!")

# Prefix list
prefixes = ["2547", "2541"]

# Step and range limits
step = 1_000_000
max_value = 100_000_000
min_value = 0

# Function to compute SHA-256 hash
def get_hash_sha256(value: str) -> str:
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# List to hold results
results = []

# Loop through prefixes and number ranges
for prefix in prefixes:
    for start in range(step, max_value + 1, step):
        previous = start - step + 1  # Start of the range

        for i in range(previous, start + 1):
            no = f"{prefix}{i:08d}"  # Format number with 8 digits
            ency = get_hash_sha256(no)
            print(f"No: {no}, Hash: {ency}")

            # Add to results list
            results.append(f"{no},{ency}\n")

# Dump to file
with open("output.csv", "w", encoding="utf-8") as f:
    f.writelines(results)

print("✅ Hash generation completed and saved to output.csv")
