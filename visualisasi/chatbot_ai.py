import pandas as pd
import matplotlib.pyplot as plt

# Membaca data
df = pd.read_csv("data/chatbot_ai.csv")

# Menghitung jumlah penggunaan AI
ai_counts = df["Chatbot AI yang paling sering Anda gunakan"].value_counts()

# warna yang digunakan Soft Yellow 
colors = [
    "#F7D774",  # soft yellow
    "#FFE8A3",  # pastel yellow
    "#FFF4C7",  # cream
    "#F9E4B7"   # beige pastel
]

# Style
plt.figure(figsize=(9, 6))
plt.gca().set_facecolor("#FFFDF8")

bars = plt.bar(
    ai_counts.index,
    ai_counts.values,
    color=colors,
    edgecolor="#D9B65D",
    linewidth=1.5
)

# Judul
plt.title(
    "🌼 Distribusi Chatbot AI yang Digunakan Mahasiswa",
    fontsize=16,
    fontweight="bold",
    color="#8C6A00",
    pad=20
)

plt.xlabel(
    "Chatbot AI",
    fontsize=12,
    color="#8C6A00"
)

plt.ylabel(
    "Jumlah Mahasiswa",
    fontsize=12,
    color="#8C6A00"
)

# Grid lembut
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Angka di atas batang
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.05,
        str(int(height)),
        ha="center",
        fontsize=11,
        fontweight="bold",
        color="#8C6A00"
    )

plt.tight_layout()

# Simpan
plt.savefig(
    "output/distribusi_chatbot_ai.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()