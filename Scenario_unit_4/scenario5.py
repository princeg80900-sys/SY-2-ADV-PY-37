import numpy as np
import pandas as pd

# Create NumPy array of electricity bills
bills = np.array([1500, 2800, 3500, 4200, 2200, 5000])

# Calculate bill statistics
print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

# Create Pandas DataFrame
df = pd.DataFrame({
    "Consumer": ["C1", "C2", "C3", "C4", "C5", "C6"],
    "Bill": bills
})

# Display complete DataFrame
print("\nElectricity Bill Data:")
print(df)

# Display consumers whose bill exceeds ₹3000
print("\nConsumers whose bill exceeds ₹3000:")
print(df[df["Bill"] > 3000])

##OUTPUT:-
# Mean Bill: 3200.0
# Median Bill: 3150.0
# Maximum Bill: 5000
# Minimum Bill: 1500

# Electricity Bill Data:
#   Consumer  Bill
# 0       C1  1500
# 1       C2  2800
# 2       C3  3500
# 3       C4  4200
# 4       C5  2200
# 5       C6  5000

# Consumers whose bill exceeds ₹3000:
#   Consumer  Bill
# 2       C3  3500
# 3       C4  4200
# 5       C6  5000

