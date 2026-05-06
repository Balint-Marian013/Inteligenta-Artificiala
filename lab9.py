import pandas as pd
import matplotlib.pyplot as plt

#pd.set_option('display.max_columns',None,'display.max_rows',None)
data=pd.read_csv("data.csv")

#print(data)

past40=data[data["Age"]>40]
#print(past40.head(10))

rez=data[(data["Overall"]>=85)&(data["Age"]<25)]
#print(rez)

sorted_data= data.sort_values(by="Skill Moves",ascending=False)
#print(sorted_data)

#print(data.columns)


data["Contract Valid Until"] = pd.to_numeric(
    data["Contract Valid Until"],
    errors="coerce"
)

contract = data[data["Contract Valid Until"] <= 2021]

#print(contract)

#print(data.columns)

#print("Dimensiune dataset:", data.shape)

#print("Randuri:", data.shape[0])

#print("Coloane:", data.shape[1])

#print("Jucatori unici:", data["Name"].nunique())


#print(data)

#print(data.columns)

top5=data["Nationality"].value_counts().head(5)
#print(top5)


plt.figure(figsize=(7,7))

plt.pie(
    top5,
    labels=top5.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Top 5 Nationalities - Players Distribution")
#plt.show()

result = data.groupby("Nationality")[["SprintSpeed", "Acceleration"]].mean()

#print(result)

data=['Position']=data['Position'].fillna("Unknown")
print(data=['Position'])