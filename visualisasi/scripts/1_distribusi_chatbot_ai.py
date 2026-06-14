import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv("data/chatbot_ai.csv")

kolom = "Chatbot AI yang paling sering Anda gunakan"
data = df[kolom].value_counts()


os.makedirs("output", exist_ok=True)


colors = [
    "#FFD966",  # Lemon Chiffon (paling cerah)
    "#FFF2B2",
    "#FFE699",
    "#F9F09A",
    "#E6C65C",
    "#D4B248"
]

# Sedikit mengeluarkan setiap irisan
explode = [0.04] * len(data)

plt.figure(figsize=(9, 7))

plt.pie(
    data.values,
    labels=data.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    shadow=True,              
    explode=explode,
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 2
    },
    textprops={
        "fontsize": 11,
        "fontweight": "bold"
    }
)

plt.title(
    "Distribusi Chatbot AI yang Digunakan",
    fontsize=18,
    fontweight="bold",
    pad=20
)

plt.axis("equal")  

plt.savefig(
    "output/1_distribusi_chatbot_ai.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()