import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("data/chatbot_ai.csv")

kolom_frekuensi = "Seberapa sering Anda menggunakan chatbot AI untuk kegiatan belajar dalam satu minggu?"
kolom_produktivitas = "Chatbot AI membuat saya lebih produktif dalam belajar"
kolom_pemahaman = "Chatbot AI membantu saya memahami materi kuliah yang sulit"

mapping_frekuensi = {
    "1-2 kali": 1,
    "3-5 kali": 2,
    "6-10 kali": 3,
    ">10 kali": 4
}

df["frekuensi_angka"] = df[kolom_frekuensi].map(mapping_frekuensi)
df["produktivitas_angka"] = pd.to_numeric(df[kolom_produktivitas], errors="coerce")
df["pemahaman_angka"] = pd.to_numeric(df[kolom_pemahaman], errors="coerce")

df = df.dropna(subset=["frekuensi_angka", "produktivitas_angka", "pemahaman_angka"])

os.makedirs("output", exist_ok=True)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    df["frekuensi_angka"],
    df["produktivitas_angka"],
    df["pemahaman_angka"],
    c="#FFD966",
    edgecolor="#B7950B",
    s=90,
    alpha=0.85
)

ax.set_title("Visualisasi 3D Frekuensi, Produktivitas, dan Pemahaman", fontsize=13, fontweight="bold")
ax.set_xlabel("Frekuensi AI")
ax.set_ylabel("Produktivitas")
ax.set_zlabel("Pemahaman Materi")

ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(["1-2", "3-5", "6-10", ">10"])

plt.tight_layout()
plt.savefig("output/9_ringkasan_visualisasi_3d.png", dpi=300)
plt.show()