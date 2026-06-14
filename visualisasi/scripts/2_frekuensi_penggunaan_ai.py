import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv("../data/chatbot_ai.csv")

kolom = "Seberapa sering Anda menggunakan chatbot AI untuk kegiatan belajar dalam satu minggu?"

data = df[kolom].value_counts().sort_values(ascending=False)

os.makedirs("../output", exist_ok=True)

x = np.arange(len(data))
y = np.zeros(len(data))
z = np.zeros(len(data))

dx = np.ones(len(data)) * 0.6
dy = np.ones(len(data)) * 0.6
dz = data.values

colors = [
    "#FFD700", 
    "#FFE066",
    "#FFEB99",
    "#FFF2B2",
    "#FFF7CC",
    "#FFFBE6"
]

colors = colors[:len(data)]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

ax.bar3d(
    x, y, z,
    dx, dy, dz,
    color=colors,
    edgecolor="#C9A227",
    alpha=0.95
)

ax.set_title("Distribusi Frekuensi Penggunaan AI", fontsize=14, fontweight="bold")
ax.set_xlabel("Frekuensi")
ax.set_ylabel("")
ax.set_zlabel("Jumlah Mahasiswa")

ax.set_xticks(x + dx / 2)
ax.set_xticklabels(data.index, rotation=20, ha="right")
ax.set_yticks([])

plt.tight_layout()
plt.savefig("../output/2_frekuensi_penggunaan_ai.png", dpi=300, bbox_inches="tight")
plt.show()