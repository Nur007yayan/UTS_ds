import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


print("Folder saat ini:", os.getcwd())
print("Isi folder sekarang:", os.listdir("."))
print("Isi folder di atas:", os.listdir(".."))

# Baca CSV dari folder data
df = pd.read_csv("data/chatbot_ai.csv")

# Cari kolom produktivitas otomatis
kolom = None
for c in df.columns:
    if "produktif" in c.lower():
        kolom = c
        break

if kolom is None:
    print("Kolom produktivitas tidak ditemukan")
    print(df.columns.tolist())
    exit()

data = df[kolom].value_counts().sort_index()

# Buat folder output
os.makedirs("output", exist_ok=True)

x = np.arange(len(data))

plt.figure(figsize=(10, 6), facecolor="#FFFDF5")

# Grafik batang 2D
bars = plt.bar(
    x,
    data.values,
    width=0.6,
    color="#FFE082",
    edgecolor="#C9A227",
    linewidth=2
)

# Angka di atas batang
for bar in bars:
    tinggi = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        tinggi + 0.2,
        int(tinggi),
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold"
    )

plt.title("Tingkat Produktivitas Belajar dengan Chatbot AI", fontsize=16, fontweight="bold")
plt.xlabel("Skala Produktivitas")
plt.ylabel("Jumlah Mahasiswa")

plt.xticks(x, data.index)
plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.savefig("output/6_tingkat_produktivitas_belajar.png", dpi=300)
plt.show()
