import pandas as pd
df=pd.read_csv("customer_shopping.csv")
print(df)
print(df.info())
print(df.columns.str.lower())

df.columns=df.columns.str.replace(" ","")
print(df.columns)
'''print(df['Purchase_Amount'].sum())

# 1.What are the top 10 most purchased products?#

print(df.groupby('Item_Purchased')['Customer_ID'].count().sort_values(ascending=False).head(10))'''

# 2.Which product categories generate the highest total purchase revenue? #

print(df.groupby('Category')['Purchase_Amount'].sum().sort_values(ascending=False))

# 3.Which locations have the highest total sales revenue?#

print(df.groupby('Location')['Purchase_Amount'].sum().sort_values(ascending=False))

# 4.What is the average purchase amount for each product category?#

print(df.groupby('Category')['Purchase_Amount'].mean().sort_values(ascending=False))

# 5.Which customer age group contributes the highest revenue?#

bins = [0, 20, 30, 40, 50, 60, 100]

labels = [
    "Under 20",
    "21-30",
    "31-40",
    "41-50",
    "51-60",
    "61+"
]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)
age_revenue = df.groupby(
    "Age_Group",
    observed=True
)["Purchase_Amount"].sum().sort_values(ascending=False)

print(age_revenue)

# 6.Which season generates the highest sales revenue?#

print(df.groupby('Season')['Purchase_Amount'].sum().sort_values(ascending=False))

# 7.Does subscription status affect customer spending?#

subscription_analysis = df.groupby("Subscription_Status").agg(
    Number_of_Purchases=("Purchase_Amount", "count"),
    Total_Revenue=("Purchase_Amount", "sum"),
    Average_Purchase=("Purchase_Amount", "mean"),
    Average_Rating=("Review_Rating", "mean")
)

print(subscription_analysis)

# 8.How does purchasing behavior differ between male and female customers?#

Gender_wise_analysis=df.groupby("Gender").agg(number_of_purchases=("Purchase_Amount","count"),total_revenue=("Purchase_Amount","sum"),
                         average_purchase=("Purchase_Amount","mean"))
print(Gender_wise_analysis) 
                        
# 9.Which payment method is most commonly used by customers?#

print(df["Payment_Method"].value_counts())

# 10.Which products receive the highest average customer ratings?#

print(df.groupby('Product')['Review_Rating'].mean().sort_values(ascending=False))







