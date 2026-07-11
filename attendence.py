import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["piyuu"],
    "january": [90],
    "february": [85],
    "march": [88],
    "april": [89],
    "may": [87],
    "june": [90],
    "july": [92],
    "august": [83],
    "september": [None],
    "october": [86],
    "november": [None],
    "december": [93]
}

df = pd.DataFrame(data)

# Fill September (average of Jan–Aug)
df.loc[0, "september"] = df.loc[0, [
    "january", "february", "march", "april",
    "may", "june", "july", "august"
]].mean()

# Fill November (average of Jan–Oct)
df.loc[0, "november"] = df.loc[0, [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october"
]].mean()

months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]

attendance = df.loc[0, months]

print(attendance)
plt.figure()
plt.plot(months, attendance, marker='o')
plt.xlabel("Months")
plt.ylabel("Attendance")
plt.title("Piyuu's Monthly Attendance")
plt.show()
