import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os


df = pd.read_csv("../data/chatbot_ai.csv")


kolom = None

for c in df.columns:
    if "memahami materi" in c.lower():
        kolom = c
        break

if kolom is None:
    print("Kolom tidak ditemukan!")
    print(df.columns.tolist())
    exit()


data = df[kolom].value_counts()

labels = data.index.tolist()
values = data.values

# Persentase
persen = values / values.sum() * 100


os.makedirs("../output", exist_ok=True)


fig = plt.figure(figsize=(12,9), facecolor="#FFFDF5")
ax = fig.add_subplot(111, projection="3d")

x = np.arange(len(labels))
y = np.zeros(len(labels))
z = np.zeros(len(labels))

dx = np.full(len(labels), 0.7)
dy = np.full(len(labels), 0.7)
dz = persen

# Warna pastel
warna = [
    "#FFD54F",
    "#FFE082",
    "#FFF3C4",
    "#FFECB3",
    "#FFD180"
]

# Jika kategori lebih banyak
while len(warna) < len(labels):
    warna.extend(warna)


ax.bar3d(
    x,
    y,
    z,
    dx,
    dy,
    dz,
    color=warna[:len(labels)],
    edgecolor="white",
    shade=True
)


for i in range(len(labels)):
    ax.text(
        x[i] + 0.2,
        y[i] + 0.2,
        dz[i] + 2,
        f"{persen[i]:.0f}%",
        fontsize=18,
        fontweight="bold",
        color="#8B5A00"
    )


# Pengaturan tampilan

ax.set_xticks(x + 0.35)
ax.set_xticklabels(labels, rotation=15, ha="right", fontsize=10)

ax.set_yticks([])

ax.set_zlabel("Persentase (%)", fontsize=12)

ax.set_title(
    "Tingkat Pemahaman Materi dengan Bantuan Chatbot AI",
    fontsize=18,
    fontweight="bold",
    pad=20
)

# Sudut pandang seperti infografik
ax.view_init(elev=25, azim=35)

# Background putih
ax.xaxis.pane.set_facecolor((1,1,1,1))
ax.yaxis.pane.set_facecolor((1,1,1,1))
ax.zaxis.pane.set_facecolor((1,1,1,1))

ax.grid(False)

plt.tight_layout()


plt.savefig(
    "../output/5_tingkat_pemahaman_materi_3D.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()