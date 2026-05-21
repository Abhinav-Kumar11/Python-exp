import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 120, 140, 130, 160],
    'Profit': [20, 25, 30, 28, 35]
})
print(df)

#Line Plot
df.plot(x='Month', y='Sales', kind='line')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#Vertical Bar
df.plot(x='Month', y='Sales', kind='bar')
plt.show()

#Horizontal Bar
df.plot(x='Month', y='Sales', kind='barh')
plt.show()

#Histogram
df['Sales'].plot(kind='hist')
plt.show()

#With different bins
df['Sales'].plot(kind='hist', bins=5)
plt.show()

#Density Plots
df['Sales'].plot(kind='density')
plt.show()

#Scatter or point plots
df.plot(x='Sales', y='Profit', kind='scatter')
plt.show()

#With Colour
df.plot(x='Sales', y='Profit', kind='scatter', color='red')
plt.show()

# Trendline calculation
m, b = np.polyfit(
    df['Sales'],
    df['Profit'],
    1
)

# Plot trendline
plt.plot(
    df['Sales'],
    m * df['Profit'] + b
)
plt.show()