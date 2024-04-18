import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

url = "https://raw.githubusercontent.com/Sobariyah1001/dataset/main/dataset_jamu_359.csv"
data = pd.read_csv(url)
st.markdown(
        """
        <h1 style="text-align: justify; color:#4186a2;">Prediksi Produksi Jamu Madura Menggunakan <i>Autoregressive Integrated Moving Average </i> (ARIMA) Dengan <i>Statistical Significance</i> dan <i>K-Means Clustering</i></h1>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #ff0099, #493240);
        margin: 0;
        padding: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Beranda", 'Data', 'Method', 'Forecast', 'About us'], 
        icons=['house', 'files','calculator','code', 'info'], menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "rgb(217, 230, 255)", "padding":"10px"},
            "icon": {"color": "black", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"2px", "--hover-color": "#eee", "color": "black", "background-color": "rgba(65, 134, 162, 0.37)"},
            "nav-link-selected": {"background-color": "#4186a2"},
        })
    selected

# Content based on selected option
if selected == "Beranda":
    st.image('img/jamu.jpg', caption='Jamu')
    st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Jamu Madura merupakan salah satu obat tradisional Indonesia yang berasal dari bahan herbal alami seperti tumbuhan, mineral, hewan, sediaan sarian, atau campuran bahan lainnya yang berasal dari pulau Madura di Jawa Timur dan telah digunakan dari generasi ke generasi untuk mengatasi permasalahan kesehatan tubuh, baik untuk mencegah penyakit ataupun untuk mengobati penyakit. Jamu Madura mempunyai beragam campuran bahan alam yang khas seperti rasa yang pahit dan mempunyai aroma rempah-rempah yang kuat dan khasiatnya sudah tidak diragukan lagi yang membuat pemasaran jamu Madura meluas bukan hanya didalam negeri, namun hingga ke mancanegara, seperti Arab Saudi, Brunei Darussalam, Jepang, Hongkong, Malaysia, Korea, dan Singapura.</p>
            <p>Jumlah industri jamu yang masih beroperasi di masing-masing kabupaten di pulau Madura banyak. Di kabupaten Sumenep terdapat 11 industri, di kabupaten Pamekasan terdapat 25 industri, di kabupaten Sampang terdapat 3 industri, dan kabupaten Bangakalan terdapat 8 industri jamu.</p>
            <p>Salah satu industri Jamu Madura didaerah Bangkalan adalah PT. Jamu Firdaus Kurnia Indah Utama (Jafir Utama) yang berada di Jl. Kh Lemah Duwur Gg. IX No.60, Barattambak, Pejagan, Kec. Bangkalan, Kabupaten Bangkalan, Jawa Timur 69112. Terdapat beberapa produk jamu yang telah diperjual belikan secara online maupun offline, seperti manjakani, empot super, ratu pil rapet wangi, galian montok, galiaan singset ++, Feminia, Helbeh double black, empot love, butiran delima, herbal bubuk ajaib, dll. Produk andalan yang meruapakn top 1 best seller perusahaan tersebut adalah ratu pil rapet wangi.</p>
            <p>Keberhasilan perusahaan tersebut dalam memperkenalkan jamu Madura tidak luput dari kepercayaan konsumen dalam mengonsumsinya.Namun, permintaan konsumen yang tidak menentu dan pemasaran yang meluas menjadi tantangan tersendiri dalam melakukan produksi supaya jumlahnya tidak terlalu banyak ataupun terlalu sedikit. Oleh sebab itu, dibutuhkan metode untuk melakukan prediksi produksi jamu Madura dimasa mendatang, salah satu metode yang bisa digunakan adalah ARIMA. Tetapi, data dengan fitur tidak relevan dan data outlier dapat membuat metode tersebut menjadi kurang akurat dalam memprediksi. Oleh karena tersebut, metode seleksi fitur menggunakan Statistical Significance dan K-Means Clustering dalam mendeteksi data outlier digunakan dalam penelitian ini.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif selected == "Data":

    st.markdown(
        """
        <h2 style="text-align: center;">Data Pada Time Series</h2>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Data yang digunakan haruslah stasioner, karena pada model ARIMA hanya menggunakan data yang stasioner. Pola data pada time series ada 4, yaitu pola data stasioner atau horizontal, tren, musiman, dan siklis.</p>
            <p>Pola data stasioner atau horizontal pada time series merupakan data yang stasioner terhadap rata-rata atau fluktuasinya bersifat konstan pada sekitar rata-rata, contohnya dapat dilihat pada gambar berikut:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/stasioner.png', caption='Data Stasioner (konstan)', use_column_width=True)

    st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data time series yang kedua adalah tren, yaitu data memiliki pola tren atau musiman adalah data dengan pola naik atau turun dalam jangka yang panjang dalam data. Contoh pola data yang memiliki tren dapat dilihat bersama pada gambar berikut:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/trend.png', caption='Data Trend', use_column_width=True)

    st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data selanjutnya yaitu pola data musiman, pola data musiman adalah data dengan pola yang terpengaruh musiman, seperti hari tertentu dalam 1 pekan, mingguan, bulanan, dan kuartil tahunan. Pola musiman dapat dilihat pada gambar berikut:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/musiman.png', caption='Data Musiman', use_column_width=True)

    st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data pada time series yang terakhir adalah pola siklis. Pola siklis adalah data yang terpengaruh oleh fluktuasi ekonomi atau semacamnya dalam jangka yang panjang di dalam data. Contoh pola siklis dapat dilihat bersama pada gambar berikut ini:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/siklis.png', caption='Data Siklis', use_column_width=True)



    st.markdown(
        """
        <h2 style="text-align: center;">Data Pada Penelitian</h2>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Data yang digunakan pada penelitian ini adalah data jamu Madura yang berasal dari PT. Jamu Firdaus Kurnia Indah Utama (Jafir Utama) dengan produk jamu yaitu Ratu Pil Rapet Wangi. Untuk detail dari data tersebut sebagai berikut:</p>
            <ol>
                <li>Dataset yang digunakan adalah dataset harian Jamu Ratu Pil Rapet Wangi</li>
                <li>Data diambil dari periode 7/9/2022 s/d 29/12/2023</li>
                <li>Jumlah dataset sebelum preprocessing: 359 data</li>
                <li>Jumlah dataset setelah preprocessing: 359 data (71%) dari dataset sebelumnya</li>
                <li>Variabel yang digunakan adalah penjualan, persediaan, dan produksi.</li>
            </ol>
        </div>
        <p>Berikut adalah data (359 data) yang digunakan dalam penelitian ini.</p>
        """,
        unsafe_allow_html=True
    )
    
    st.dataframe(data)

    # Visualize the data with a bar chart
    st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Dari data penelitian ini, untuk mengetahui pola pada data yang digunakan, berikut ini adalah visualisasi dari semua variabel (penjualan, persediaan, dan produksi).</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    fig = px.line(data, x='tanggal', y=['penjualan', 'persediaan', 'produksi'], title='Penjualan, Persediaan, dan Produksi')
    st.plotly_chart(fig)
elif selected == "Method":
    st.write("This is the Method content.")
elif selected == "Forecast":
    st.write("This is the Forecast content.")

# Manual item selection
# if st.session_state.get('switch_button', False):
#     st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
#     manual_select = st.session_state['menu_option']
# else:
#     manual_select = None

# Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
#     st.write(f"Selection changed to {selection}")
