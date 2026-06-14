import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv("../data/chatbot_ai.csv")

kolom = "Untuk kegiatan apa chatbot AI paling sering digunakan?"
data = df[kolom].value_counts().sort_values(ascending=True)

os.makedirs("../output", exist_ok=True)

x = np.zeros(len(data))
y = np.arange(len(data))
z = np.zeros(len(data))

dx = data.values
dy = np.ones(len(data)) * 0.55
dz = np.ones(len(data)) * 0.45

colors = [
    "#FFFBE6",
    "#FFF7CC",
    "#FFF2B2",
    "#FFEB99",
    "#FFE066",
    "#FFD700"
]

while len(colors) < len(data):
    colors.append("#FFD700")

colors = colors[-len(data):]

fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(111, projection="3d")

ax.bar3d(
    x, y, z,
    dx, dy, dz,
    color=colors,
    edgecolor="#B8860B",
    linewidth=1,
    alpha=0.95,
    shade=True
)

ax.set_title(
    "Tujuan Penggunaan Chatbot AI",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Jumlah Mahasiswa", fontsize=11, fontweight="bold")
ax.set_ylabel("Tujuan Penggunaan", fontsize=11, fontweight="bold")
ax.set_zlabel("")

ax.set_yticks(y + dy / 2)
ax.set_yticklabels(data.index, fontsize=9)

ax.set_zticks([])

for i, value in enumerate(data.values):
    ax.text(
        value + 0.15,
        y[i] + 0.25,
        0.45,
        str(value),
        fontsize=10,
        fontweight="bold"
    )

ax.view_init(elev=25, azim=-55)

plt.tight_layout()

plt.savefig(
    "../output/4_tujuan_penggunaan_ai_3d.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()