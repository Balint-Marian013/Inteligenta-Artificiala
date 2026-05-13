import pandas as pd

#EX1

df = pd.read_csv(r"C:\Users\Marian\Documents\GitHub\Inteligenta-Artificiala\StudentsPerformance.csv")

# print("Primele 5 înregistrări")
# print(df.head())

# print("Structura dataset-ului")
# print(df.info())

# print( "Statistici descriptive")
# print(df.describe())

# print("Valori lipsă")
# print(df.isnull().sum())

# EX2
# print("Variabile categorice")
# print(df.select_dtypes(include=['object', 'str']).columns.tolist())

# print("Variabile numerice")
# print(df.select_dtypes(include=['int64', 'float64']).columns.tolist())

# print("Categoriile din fiecare variabilă categorică")
# for col in df.select_dtypes(include=['object', 'str']).columns:
#     print(f"{col}: {df[col].unique().tolist()}")



