import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Orange', 'Mango']
sizes = [30, 25, 20, 25]
colors = ['red', 'yellow', 'orange', 'green']

plt.pie(sizes, labels=labels, colors=colors, autopct="%.1f")

plt.title('Fruit Distribution')

plt.show()
