import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Preprocessing
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['season'] = day_df['season'].astype('category')
day_df['weathersit'] = day_df['weathersit'].astype('category')

# Set title for the dashboard
st.title("🚴‍♂️ Dashboard Analisis Penyewaan Sepeda")
st.subheader("Analisis Data Penyewaan Sepeda Berdasarkan Faktor Cuaca dan Waktu")

# Sidebar for navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["🌤️ Analisis Cuaca", "📈 Pola Penyewaan", "📚 Kesimpulan"])

# Page: Analisis Cuaca
if page == "🌤️ Analisis Cuaca":
    st.header("Analisis Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda")
    
    # Scatter plot suhu vs jumlah penyewaan
    st.subheader("Hubungan Suhu terhadap Penyewaan Sepeda")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=day_df, x='temp', y='cnt', scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax1)
    ax1.set_title('Hubungan Suhu terhadap Penyewaan Sepeda', fontsize=14)
    ax1.set_xlabel('Suhu (Normalisasi)', fontsize=12)
    ax1.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig1)

    # Scatter plot kelembaban vs jumlah penyewaan
    st.subheader("Hubungan Kelembaban terhadap Penyewaan Sepeda")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=day_df, x='hum', y='cnt', scatter_kws={'alpha':0.5}, line_kws={'color':'blue'}, ax=ax2)
    ax2.set_title('Hubungan Kelembaban terhadap Penyewaan Sepeda', fontsize=14)
    ax2.set_xlabel('Kelembaban (Normalisasi)', fontsize=12)
    ax2.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig2)

    # Scatter plot kecepatan angin vs jumlah penyewaan
    st.subheader("Hubungan Kecepatan Angin terhadap Penyewaan Sepeda")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=day_df, x='windspeed', y='cnt', scatter_kws={'alpha':0.5}, line_kws={'color':'green'}, ax=ax3)
    ax3.set_title('Hubungan Kecepatan Angin terhadap Penyewaan Sepeda', fontsize=14)
    ax3.set_xlabel('Kecepatan Angin (Normalisasi)', fontsize=12)
    ax3.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig3)

    # Box plot kondisi cuaca
    st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='weathersit', y='cnt', ax=ax4)
    ax4.set_title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda', fontsize=14)
    ax4.set_xlabel('Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan)', fontsize=12)
    ax4.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig4)

    # Heatmap korelasi
    st.subheader("Korelasi Faktor Cuaca terhadap Penyewaan")
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.heatmap(day_df[['temp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', ax=ax5)
    ax5.set_title('Korelasi Faktor Cuaca terhadap Penyewaan Sepeda', fontsize=14)
    st.pyplot(fig5)

# Page: Pola Penyewaan
elif page == "📈 Pola Penyewaan":
    st.header("Pola Penyewaan Sepeda Berdasarkan Waktu")
    
    # Line plot pola penyewaan dalam sehari
    st.subheader("Waktu Puncak Penyewaan Sepeda dalam Sehari")
    fig6, ax6 = plt.subplots(figsize=(12, 6))
    hour_df['day_type'] = hour_df['workingday'].map({1: 'Hari Kerja', 0: 'Akhir Pekan/Libur'})
    hourly_rentals = hour_df.groupby(['hr', 'day_type'])['cnt'].mean().reset_index()
    sns.lineplot(data=hourly_rentals, x='hr', y='cnt', hue='day_type', marker='o', ax=ax6)
    ax6.set_title('Pola Penyewaan Sepeda dalam Sehari', fontsize=14)
    ax6.set_xlabel('Jam', fontsize=12)
    ax6.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
    ax6.set_xticks(range(0, 24))
    ax6.legend(title='Tipe Hari')
    ax6.grid(True)
    st.pyplot(fig6)

    # Box plot perbandingan hari kerja vs akhir pekan
    st.subheader("Perbandingan Penyewaan: Hari Kerja vs Akhir Pekan")
    fig7, ax7 = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=day_df, x='workingday', y='cnt', ax=ax7)
    ax7.set_title('Perbandingan Penyewaan: Hari Kerja vs Akhir Pekan', fontsize=14)
    ax7.set_xlabel('Hari Kerja (1=Ya, 0=Tidak)', fontsize=12)
    ax7.set_ylabel('Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig7)

# Page: Kesimpulan
elif page == "📚 Kesimpulan":
    st.header("Kesimpulan Analisis")
    st.write("Berdasarkan analisis data penyewaan sepeda, berikut adalah temuan utama:")
    st.write("1. **Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda**:")
    st.write("   - **Suhu**: Terdapat korelasi positif yang kuat. Semakin tinggi suhu (dalam batas nyaman), semakin banyak penyewaan sepeda.")
    st.write("   - **Kelembaban**: Korelasi negatif. Kelembaban tinggi cenderung mengurangi minat penyewaan sepeda.")
    st.write("   - **Kecepatan Angin**: Pengaruhnya relatif kecil, tetapi kecepatan angin tinggi sedikit menurunkan jumlah penyewaan.")
    st.write("   - **Kondisi Cuaca**: Hari cerah (weathersit=1) memiliki penyewaan tertinggi, diikuti berkabut (2), dan hujan (3) dengan jumlah terendah.")
    st.write("2. **Pola Penyewaan Sepeda dalam Sehari dan Perbandingan Hari Kerja vs Akhir Pekan**:")
    st.write("   - **Hari Kerja**: Pola penyewaan menunjukkan dua puncak utama pada jam 08:00 (pagi) dan 17:00-18:00 (sore), mencerminkan penggunaan untuk commuting.")
    st.write("   - **Akhir Pekan/Libur**: Pola lebih merata dengan puncak di siang hingga sore (12:00-16:00), menunjukkan penggunaan untuk rekreasi.")
    st.write("   - Secara keseluruhan, hari kerja memiliki variasi penyewaan yang lebih besar dibandingkan akhir pekan.")

# Footer
st.write("---")
st.sidebar.write("**Informasi Kontak:**")
st.sidebar.write("Nama: Damianus Christopher Samosir")
st.sidebar.write("Email: christophersamosir@gmail.com")
st.sidebar.write("ID Dicoding: mc189d5y0821")