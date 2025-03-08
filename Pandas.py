import pandas as pd

# Dictionary se DataFrame Banana
data = {
    "Name": ["Ali", "Sara", "Tahir"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}

df = pd.DataFrame(data)

print(df)
