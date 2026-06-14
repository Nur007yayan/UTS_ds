import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv("data/chatbot_ai.csv")

kolom = "Saya merasa bergantung pada chatbot AI dalam menyelesaikan tugas kuliah"
data = df[kolom].value_counts().sort_index()

os.makedirs("output", exist_ok=True)

labels = [str(i) for i in data.index]
values = data.values.tolist()

values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

ax.plot(angles, values, color="#E6B800", linewidth=3)
ax.fill(angles, values, color="#FFF2CC", alpha=0.8)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_title("Tingkat Ketergantungan terhadap AI", fontsize=14, fontweight="bold", pad=20)
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("output/7_tingkat_ketergantungan_ai.png", dpi=300)
plt.show()