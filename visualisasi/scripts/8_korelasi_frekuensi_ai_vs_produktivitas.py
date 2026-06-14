import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/chatbot_ai.csv")

kolom_frekuensi = "Seberapa sering Anda menggunakan chatbot AI untuk kegiatan belajar dalam satu minggu?"
kolom_produktivitas = "Chatbot AI membuat saya lebih produktif dalam belajar"

mapping_frekuensi = {
    "1-2 kali": 1,
    "3-5 kali": 2,
    "6-10 kali": 3,
    ">10 kali": 4
}

df["frekuensi_angka"] = df[kolom_frekuensi].map(mapping_frekuensi)
df["produktivitas_angka"] = pd.to_numeric(df[kolom_produktivitas], errors="coerce")

df = df.dropna(subset=["frekuensi_angka", "produktivitas_angka"])

os.makedirs("output", exist_ok=True)

plt.figure(figsize=(8, 5))
plt.scatter(
    df["frekuensi_angka"],
    df["produktivitas_angka"],
    color="#FFD966",
    edgecolor="#B7950B",
    s=90,
    alpha=0.8
)

plt.title("Korelasi Frekuensi AI vs Produktivitas", fontsize=14, fontweight="bold")
plt.xlabel("Frekuensi Penggunaan AI")
plt.ylabel("Produktivitas Belajar")

plt.xticks([1, 2, 3, 4], ["1-2 kali", "3-5 kali", "6-10 kali", ">10 kali"])
plt.grid(linestyle="--", alpha=0.3)

plt.tight_layout()
plt.savefig("output/8_korelasi_frekuensi_ai_vs_produktivitas.png", dpi=300)
plt.show()