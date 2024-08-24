import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

day_df = pd.read_csv('day.csv')

st.title('Pengaruh Cuaca terhadap Penggunaan Sepeda')

weather_workingday_avg = day_df.groupby(['weathersit', 'workingday'])['cnt'].mean().reset_index()


weather_labels = {
    1: 'Cerah/Cerah Berawan',
    2: 'Berawan Penuh',
    3: 'Hujan/Lainnya'
}
weather_workingday_avg['weathersit'] = weather_workingday_avg['weathersit'].map(weather_labels)


st.subheader('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Cuaca dan Hari Kerja/Hari Libur')
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', hue='workingday', data=weather_workingday_avg)
plt.title('Pengaruh Cuaca terhadap Rata-rata Jumlah Pengguna Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
plt.legend(title='Hari Kerja (1: Ya, 0: Tidak)')
st.pyplot(plt)  


st.markdown("""
## Penjelasan Visualisasi

1. **Cuaca Cerah/Cerah Berawan**:
   - **Hari Kerja**: Penggunaan sepeda paling tinggi terjadi saat cuaca cerah atau cerah berawan pada hari kerja. Ini menunjukkan bahwa kondisi cuaca yang nyaman sangat mendorong penggunaan sepeda, terutama untuk kegiatan rutin seperti perjalanan ke tempat kerja atau sekolah.
   - **Hari Libur**: Penggunaan sepeda juga tinggi pada hari libur ketika cuaca cerah, meskipun sedikit lebih rendah dibandingkan hari kerja. Ini bisa terkait dengan kegiatan rekreasi atau berolahraga.

2. **Cuaca Berawan Penuh**:
   - **Hari Kerja**: Meskipun sedikit menurun, penggunaan sepeda masih cukup tinggi saat cuaca berawan penuh pada hari kerja. Ini menunjukkan bahwa meskipun cuaca tidak seideal cerah, orang masih bersedia menggunakan sepeda untuk keperluan sehari-hari.
   - **Hari Libur**: Pada hari libur, penggunaan sepeda menurun lebih lanjut saat cuaca berawan penuh, tetapi tetap ada penggunaan yang signifikan.

3. **Cuaca Hujan/Snow/Lainnya**:
   - **Hari Kerja**: Penggunaan sepeda turun drastis ketika cuaca buruk seperti hujan atau salju. Ini menunjukkan bahwa kondisi cuaca yang tidak nyaman sangat mengurangi minat orang untuk bersepeda, bahkan untuk perjalanan harian.
   - **Hari Libur**: Pada hari libur, penggunaan sepeda adalah yang terendah ketika cuaca buruk, yang menunjukkan bahwa orang cenderung menghindari aktivitas luar ruangan saat cuaca ekstrem.
""")




hour_df = pd.read_csv('hour.csv')

hour_df['hour'] = hour_df['hr'].apply(lambda x: f'{x}:00')

st.title('Pola Penggunaan Sepeda Berdasarkan Jam dalam Hari')


numeric_cols = ['cnt', 'workingday', 'hr']


hourly_mean = hour_df[numeric_cols].groupby(['hr', 'workingday']).mean().reset_index()


hourly_mean['hour'] = hourly_mean['hr'].apply(lambda x: f'{x}:00')


st.subheader('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Jam dan Hari Kerja/Hari Libur')
plt.figure(figsize=(14, 7))
sns.lineplot(x='hour', y='cnt', hue='workingday', data=hourly_mean)
plt.title('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Jam dan Hari Kerja/Hari Libur')
plt.xlabel('Jam dalam Hari')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
plt.xticks(rotation=45)
plt.legend(title='Hari Kerja (1: Ya, 0: Tidak)')
st.pyplot(plt)


st.markdown("""
## Penjelasan Visualisasi
Pada hari kerja, terdapat puncak penggunaan sepeda pada jam 7-9 pagi, yang mungkin terkait dengan perjalanan pagi ke tempat kerja atau sekolah.
Puncak lain terjadi pada jam 5-7 sore, menunjukkan bahwa banyak pengguna kembali ke rumah setelah bekerja.
Kemudian, penggunaan sepeda pada hari kerja lebih terfokus pada jam sibuk pagi dan sore, mencerminkan penggunaan sepeda sebagai alat transportasi.
Pada hari libur, pola penggunaan sepeda lebih merata sepanjang hari, tanpa puncak yang signifikan pada jam-jam tertentu.       
"""
)
