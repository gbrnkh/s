import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat dataset
day_df = pd.read_csv("./data/day.csv")

hour_df = pd.read_csv("./data/hour.csv")

# Mapping musim
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_map)

# Judul Dashboard
st.title("Dashboard Analisis Data Bike Sharing")

# Visualisasi Peminjaman Sepeda Berdasarkan Musim
st.subheader("Rata-rata Peminjaman Sepeda per Musim")
seasonal_counts = day_df.groupby("season_label")["cnt"].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="season_label", y="cnt", data=seasonal_counts, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Visualisasi Peminjaman Sepeda Berdasarkan Jam
st.subheader("Rata-rata Peminjaman Sepeda per Jam dalam Sehari")
hourly_counts = hour_df.groupby("hr")["cnt"].mean().reset_index()
fig, ax = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=hourly_counts, marker="o", color="b", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_xticks(range(0, 24))
st.pyplot(fig)
