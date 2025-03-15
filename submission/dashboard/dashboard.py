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

# Menambahkan filter interaktif untuk memilih musim
selected_season = st.selectbox("Pilih Musim:", ["Semua"] + list(season_map.values()))

# Filter data berdasarkan musim yang dipilih
if selected_season != "Semua":
    filtered_day_df = day_df[day_df["season_label"] == selected_season]
else:
    filtered_day_df = day_df

# Visualisasi Peminjaman Sepeda Berdasarkan Musim
st.subheader("Rata-rata Peminjaman Sepeda per Musim")
seasonal_counts = filtered_day_df.groupby("season_label")["cnt"].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="season_label", y="cnt", data=seasonal_counts, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Menambahkan filter interaktif untuk memilih rentang jam
st.subheader("Rata-rata Peminjaman Sepeda per Jam dalam Sehari")
hour_range = st.slider("Pilih Rentang Jam:", 0, 23, (0, 23))

# Filter data berdasarkan rentang jam yang dipilih
filtered_hour_df = hour_df[(hour_df["hr"] >= hour_range[0]) & (hour_df["hr"] <= hour_range[1])]

hourly_counts = filtered_hour_df.groupby("hr")["cnt"].mean().reset_index()
fig, ax = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=hourly_counts, marker="o", color="b", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_xticks(range(hour_range[0], hour_range[1] + 1))
st.pyplot(fig)

# Insight
st.markdown("### Insight")
st.write("""
- Jumlah peminjaman sepeda cenderung lebih tinggi pada musim Summer dan Fall dibandingkan musim lainnya.
- Peminjaman sepeda mencapai puncaknya pada jam 8 pagi dan jam 5 sore, yang kemungkinan besar berhubungan dengan jam sibuk kerja dan pulang kerja.
- Musim mempengaruhi jumlah peminjaman, dengan peminjaman lebih rendah di musim dingin.
""")
