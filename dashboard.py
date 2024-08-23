import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

day_df = pd.read_csv('/users/rich/submission/data/day.csv')

st.title('Analisis Penggunaan Sepeda Berdasarkan Cuaca dan Hari Kerja')


st.subheader('Distribusi Jumlah Pengguna Berdasarkan Situasi Cuaca dan Hari Kerja/Hari Libur')
plt.figure(figsize=(14, 7))
sns.boxplot(x='weathersit', y='cnt', hue='workingday', data=day_df)
plt.title('Distribusi Jumlah Pengguna Berdasarkan Situasi Cuaca dan Hari Kerja/Hari Libur')
plt.xlabel('Situasi Cuaca (1: Cerah, 2: Berawan, 3: Hujan)')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.legend(title='Hari Kerja (1: Ya, 0: Tidak)')
st.pyplot(plt) 

with st.expander("See Explanation:"):
    st.write("""Penggunaan sepeda cenderung lebih tinggi pada hari-hari dengan cuaca yang lebih baik (misalnya, cerah atau berawan). Sebaliknya, ketika cuaca lebih buruk (misalnya, hujan), jumlah pengguna sepeda cenderung lebih rendah.""")




hour_df = pd.read_csv('/users/rich/submission/data/hour.csv')

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

with st.expander("See Explanation:"):
    st.write("""Pada hari kerja, terdapat puncak penggunaan sepeda pada jam 7-9 pagi, yang mungkin terkait dengan perjalanan pagi ke tempat kerja atau sekolah.
             Puncak lain terjadi pada jam 5-7 sore, menunjukkan bahwa banyak pengguna kembali ke rumah setelah bekerja.
             Kemudian, penggunaan sepeda pada hari kerja lebih terfokus pada jam sibuk pagi dan sore, mencerminkan penggunaan sepeda sebagai alat transportasi.
             Pada hari libur, pola penggunaan sepeda lebih merata sepanjang hari, tanpa puncak yang signifikan pada jam-jam tertentu.""")

