import numpy as np
import pandas as pd

# Create NumPy array of room rents
rents = np.array([2500, 3500, 4200, 5000, 3000, 4500])

# Calculate statistics
print("Mean Rent:", np.mean(rents))
print("Median Rent:", np.median(rents))
print("Maximum Rent:", np.max(rents))
print("Minimum Rent:", np.min(rents))

# Create Pandas DataFrame
df = pd.DataFrame({
    "Room": ["R1", "R2", "R3", "R4", "R5", "R6"],
    "Rent": rents
})

# Display DataFrame
print("\nHotel Room Rent Data:")
print(df)

# Display rooms having rent greater than ₹4000
print("\nRooms having rent greater than ₹4000:")
print(df[df["Rent"] > 4000])


##OUTPUT:-
# Mean Rent: 3783.3333333333335
# Median Rent: 3850.0
# Maximum Rent: 5000
# Minimum Rent: 2500

# Hotel Room Rent Data:
#   Room  Rent
# 0   R1  2500
# 1   R2  3500
# 2   R3  4200
# 3   R4  5000
# 4   R5  3000
# 5   R6  4500

# Rooms having rent greater than ₹4000:
#   Room  Rent
# 2   R3  4200
# 3   R4  5000
# 5   R6  4500
