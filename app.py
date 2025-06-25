# Import library yang dibutuhkan
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =============================================================================
## Perubahan 1: Konfigurasi Halaman (Page Config)
# Ini harus menjadi perintah pertama yang dijalankan Streamlit
# Kita atur judul tab di browser, ikon, dan layout halaman menjadi 'wide'
# =============================================================================
st.set_page_config(
    page_title="Prediksi Penguin",
    page_icon="🐧",
    layout="wide"
)

# Fungsi untuk memuat data dari path lokal
@st.cache_data
def load_data(local_path):
    df = pd.read_csv(local_path)
    return df

# Judul dan Tampilan Teks 
st.title("🐧 Aplikasi Klasifikasi Spesies Penguin")
st.write("""
Aplikasi ini adalah contoh pengerjaan **Studi Kasus** dari modul praktikum Data Mining. Tujuannya adalah untuk memprediksi spesies Penguin Palmer (Adelie, Chinstrap, atau Gentoo) menggunakan model **Random Forest Classifier**.
""")

# Memuat data
file_path = r"D:\Datmi\streamlit\penguins.csv"
df_penguins = load_data(file_path)

# Preprocessing data
df_cleaned = df_penguins.dropna()
X = df_cleaned[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df_cleaned['species']

# Membangun Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# =============================================================================
## Perubahan 2: Menggunakan Navigasi Tab
# Kita pisahkan konten menjadi dua tab utama agar lebih rapi
# =============================================================================
tab1, tab2 = st.tabs(["📊 Informasi & Visualisasi Dataset", "🤖 Prediksi Interaktif"])

with tab1:
    st.header("Informasi Dataset Penguin")
    
    # Persyaratan Studi Kasus: Menampilkan data awal
    # Perubahan 3: Menggunakan Expander agar tidak memakan tempat
    with st.expander("Klik untuk melihat Tabel Data Mentah"):
        st.write(f"Dataset ini memiliki {df_penguins.shape[0]} baris dan {df_penguins.shape[1]} kolom.")
        st.dataframe(df_penguins)

    st.markdown("---")
    st.header("Visualisasi Data")
    
    # Persyaratan Studi Kasus: Menampilkan visualisasi
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.subheader("Scatter Plot: Panjang vs Kedalaman Paruh")
        fig1, ax1 = plt.subplots()
        sns.scatterplot(data=df_cleaned, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax1)
        st.pyplot(fig1)

    with fig_col2:
        st.subheader("Histogram: Distribusi Panjang Sirip")
        fig2, ax2 = plt.subplots()
        sns.histplot(data=df_cleaned, x='flipper_length_mm', hue='species', kde=True, ax=ax2)
        st.pyplot(fig2)

with tab2:
    st.header("Prediksi Spesies Penguin Secara Real-time")
    
    # Membuat Sidebar untuk Input 
    st.sidebar.header("Input Fitur Penguin:")

    def user_input_features():
        # Komponen Input Slider 
        bill_length = st.sidebar.slider("Panjang Paruh (mm)", float(X['bill_length_mm'].min()), float(X['bill_length_mm'].max()), float(X['bill_length_mm'].mean()))
        bill_depth = st.sidebar.slider("Kedalaman Paruh (mm)", float(X['bill_depth_mm'].min()), float(X['bill_depth_mm'].max()), float(X['bill_depth_mm'].mean()))
        flipper_length = st.sidebar.slider("Panjang Sirip (mm)", float(X['flipper_length_mm'].min()), float(X['flipper_length_mm'].max()), float(X['flipper_length_mm'].mean()))
        body_mass = st.sidebar.slider("Massa Tubuh (g)", float(X['body_mass_g'].min()), float(X['body_mass_g'].max()), float(X['body_mass_g'].mean()))
        data = {'bill_length_mm': bill_length, 'bill_depth_mm': bill_depth, 'flipper_length_mm': flipper_length, 'body_mass_g': body_mass}
        features = pd.DataFrame(data, index=[0])
        return features

    user_df = user_input_features()
    
    st.subheader("Parameter Input dari Pengguna:")
    st.table(user_df) # Menggunakan st.table untuk tampilan yang lebih simpel 

    st.markdown("---")
    
    # Tombol Aksi 
    if st.sidebar.button("Prediksi Spesies"):
        prediction = model.predict(user_df)
        prediction_proba = model.predict_proba(user_df)
        res_col1, res_col2 = st.columns([1, 1.2]) # Kolom kedua sedikit lebih lebar
        with res_col1:
            st.subheader("Hasil Prediksi:")
            st.success(f"Spesies yang diprediksi adalah **{prediction[0]}**.")
            st.subheader("Tingkat Kepercayaan Model:")
            st.write(pd.DataFrame(prediction_proba, columns=model.classes_, index=["Probabilitas"]))
        with res_col2:
            st.subheader("Contoh Gambar Spesies:")
            if prediction[0] == "Adelie":
                st.image("images/adelie.jpg", caption="Contoh Penguin Adelie")
            elif prediction[0] == "Chinstrap":
                st.image("images/chinstrap.jpg", caption="Contoh Penguin Chinstrap")
            else:
                st.image("images/gentoo.jpg", caption="Contoh Penguin Gentoo")

# Footer sederhana di sidebar
st.sidebar.markdown("---")
st.sidebar.info(f"Akurasi model pada data uji: **{accuracy_score(y_test, model.predict(X_test)):.2%}**")