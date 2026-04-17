import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# STYLE (DARK THEME)
# ---------------------------
plt.style.use('dark_background')

# ---------------------------
# CREATE DATA
# ---------------------------
np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=200)

categories = ['Food', 'Travel', 'Rent', 'Shopping', 'Bills']

data = {
    'Date': dates,
    'Food': np.random.randint(200, 2000, 200),
    'Travel': np.random.randint(100, 1500, 200),
    'Shopping': np.random.randint(300, 2500, 200)
}

df = pd.DataFrame(data)

# ---------------------------
# CREATE FIGURE (LIKE YOUR FRIEND)
# ---------------------------
fig, axes = plt.subplots(3, 1, figsize=(12, 8))

fig.suptitle("Expense Tracker Dashboard", fontsize=16, fontweight='bold')

# ---------------------------
# GRAPH 1: FOOD TREND
# ---------------------------
axes[0].plot(df['Date'], df['Food'], color='skyblue', linewidth=2)
axes[0].set_title("Food Expenses Trend")

# Trend line
z = np.polyfit(range(len(df)), df['Food'], 1)
p = np.poly1d(z)
axes[0].plot(df['Date'], p(range(len(df))), "r--")

# ---------------------------
# GRAPH 2: TRAVEL TREND
# ---------------------------
axes[1].plot(df['Date'], df['Travel'], color='lime', linewidth=2)
axes[1].set_title("Travel Expenses Trend")

z = np.polyfit(range(len(df)), df['Travel'], 1)
p = np.poly1d(z)
axes[1].plot(df['Date'], p(range(len(df))), "r--")

# ---------------------------
# GRAPH 3: SHOPPING TREND
# ---------------------------
axes[2].plot(df['Date'], df['Shopping'], color='orange', linewidth=2)
axes[2].set_title("Shopping Expenses Trend")

z = np.polyfit(range(len(df)), df['Shopping'], 1)
p = np.poly1d(z)
axes[2].plot(df['Date'], p(range(len(df))), "r--")

# ---------------------------
# FINAL TOUCH
# ---------------------------
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()