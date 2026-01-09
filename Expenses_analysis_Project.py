import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("raw_expense.csv")

df["category"]=df["category"].str.lower().str.strip()
df["amount"]=pd.to_numeric(df["amount"],errors="coerce")
clean_df=df.dropna(subset=["category","amount"]).reset_index(drop=True)
print(clean_df)

category_totals=clean_df.groupby("category")["amount"].sum()
print(category_totals)

grand_total=category_totals.sum()
print(f"\nTotal Spending: {grand_total}")

highest=category_totals.idxmax()
print(f"Highest spending category:{highest} = {category_totals[highest]:.2f}")

percentage=(category_totals/grand_total)*100
print("Percentage Spending:")
print(percentage.round(2))

category_totals.plot(kind="bar")
plt.title("Total Spending per Category")
plt.ylabel("Amount(€)")
plt.xlabel("category")
plt.tight_layout()
plt.show()

category_totals.plot(kind="pie",autopct="%1.1f%%",startangle=90)
plt.title("Spending Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

high_expenses=clean_df[clean_df["amount"] > 100]

plt.scatter(high_expenses["category"],high_expenses["amount"])
plt.title("High Expenses (>100)")
plt.ylabel("Amount(€)")
plt.xlabel("Category")
plt.show()

clean_df.to_csv("clean_expenses_final.csv",index=False)
print("Cleaned data saved.")

summary=clean_df.groupby("category")["amount"].sum().reset_index()
summary.to_csv("expense_summary.csv",index=False)
