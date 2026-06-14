import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../data/chatbot_ai.csv")

kolom = "Rata-rata durasi penggunaan chatbot AI dalam satu hari"
data = df[kolom].value_counts().sort_values(ascending=True)

os.makedirs("../output", exist_ok=True)

colors = ["#FFF4B8", "#FFEB99", "#FFE066", "#FFD700"]
colors = colors[-len(data):]

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#FFFDF2")
ax.set_facecolor("#FFF9E6")

for i, (label, value) in enumerate(data.items()):
    ax.hlines(
        y=i,
        xmin=0,
        xmax=value,
        color=colors[i],
        linewidth=8,
        alpha=0.9
    )

    ax.scatter(
        value,
        i,
        s=650,
        color=colors[i],
        edgecolor="#B8860B",
        linewidth=2.5,
        zorder=3
    )

    ax.text(
        value,
        i,
        str(value),
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        color="#4A3500",
        zorder=4
    )

ax.set_yticks(range(len(data)))
ax.set_yticklabels(data.index, fontsize=12, fontweight="bold")

ax.set_title(
    "Distribusi Durasi Penggunaan Chatbot AI",
    fontsize=20,
    fontweight="bold",
    color="#4A3500",
    pad=20
)

ax.set_xlabel("Jumlah Mahasiswa", fontsize=13, fontweight="bold")
ax.grid(axis="x", linestyle="--", alpha=0.3)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.tight_layout()

plt.savefig(
    "../output/3_durasi_penggunaan_ai_lollipop.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()