import matplotlib.pyplot as plt
import pandas as pd


def main():
	data = pd.read_csv("sales.csv")
	print("Total sales:", data["Sales"].sum())
	print("Average sales:", data["Sales"].mean())

	monthly_sales = data.groupby("Month")["Sales"].sum()
	print("Highest-sales month:", monthly_sales.idxmax(), monthly_sales.max())
	category_sales = data.groupby("Category").Sales.sum()
	print("Sales by category:\n", category_sales)

	plt.figure()
	category_sales.plot(kind="bar", title="Sales by Product Category")
	plt.figure()
	monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
	plt.figure()
	category_sales.plot(kind="pie", autopct="%1.1f%%", title="Category Contribution")
	plt.tight_layout()

	plt.show()


if __name__ == "__main__":
	main()

#Output:
# Total sales: 1495000
# Average sales: 124583.33333333333
# Highest-sales month: Jun 285000
# Sales by category:
#  Category
# Electronics    1495000

