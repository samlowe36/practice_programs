import matplotlib.pyplot as plt

x1 = [3, 4, 5, 6]
y1 = [3, 3, 6, 7]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 2, 3, 4, 5]

plt.plot(x1, y1, color="green", linestyle="dashed", linewidth=3, marker="o", markerfacecolor="blue", markersize=12,
         label="Line 1")
plt.plot(x2, y2, label="Line 2")

plt.ylim(1, 8)
plt.xlim(1, 8)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("Practice Graph")

plt.legend()
plt.show()