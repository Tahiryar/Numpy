import pandas as pd

# Dictionary se DataFrame Banana
data = {
    "Name": ["Ali", "Sara", "Tahir"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}

df = pd.DataFrame(data)

print(df)

df = pd.read_csv("data.csv")  # CSV file read karna
df = pd.read_excel("data.xlsx")  # Excel file read karna
df = pd.read_sql("SELECT * FROM users", connection)  # SQL Database se data lena
