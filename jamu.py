import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("https://raw.githubusercontent.com/Sobariyah1001/dataset/main/dataset_jamu_359.csv")
data_clear = pd.read_csv("https://raw.githubusercontent.com/Sobariyah1001/maduraherbs/main/dataset/data_clear.csv")
pearson = pd.read_csv("https://raw.githubusercontent.com/Sobariyah1001/maduraherbs/main/dataset/pearson.csv")
vif = pd.read_csv("https://raw.githubusercontent.com/Sobariyah1001/maduraherbs/main/dataset/vif.csv")
distance = pd.read_csv("https://raw.githubusercontent.com/Sobariyah1001/maduraherbs/main/dataset/distance.csv")
outlier = pd.read_csv("https://raw.githubusercontent.com/Sobariyah1001/maduraherbs/main/dataset/dfkmeans.csv")
# data = [1,2,3,4]
st.markdown(
        """
        <h2 style="text-align: justify; color:#4186a2;">Prediksi Produksi Jamu Madura Menggunakan <i>Autoregressive Integrated Moving Average </i> (ARIMA) Dengan <i>Statistical Significance</i> dan <i>K-Means Clustering</i></h2>
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

# Content
#-------------------------------------------------------------------------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------------------------------------------------------------------------
elif selected == "Data":

    st.markdown(
        """
        <h3 style="text-align: center;">Data Pada Time Series</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Data yang digunakan haruslah stasioner, karena pada model ARIMA hanya menggunakan data yang stasioner. Pola data pada time series ada 4, yaitu pola data stasioner atau horizontal, tren, musiman, dan siklis.</p>
       </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3>Stasioner</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data stasioner atau horizontal pada time series merupakan data yang stasioner terhadap rata-rata atau fluktuasinya bersifat konstan pada sekitar rata-rata, contohnya dapat dilihat pada gambar berikut:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/stasioner.png', caption='Data Stasioner (konstan)', use_column_width=True) #stasioner


    st.markdown(
        """
        <h3>Tren</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data time series yang kedua adalah tren, yaitu data memiliki pola tren atau musiman adalah data dengan pola naik atau turun dalam jangka yang panjang dalam data. Contoh pola data yang memiliki tren dapat dilihat bersama pada gambar berikut:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/trend.png', caption='Data Trend', use_column_width=True) #tren

    st.markdown(
        """
        <h3>Musiman</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data selanjutnya yaitu pola data musiman, pola data musiman adalah data dengan pola yang terpengaruh musiman, seperti hari tertentu dalam 1 pekan, mingguan, bulanan, dan kuartil tahunan. Pola musiman dapat dilihat pada gambar berikut:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/musiman.png', caption='Data Musiman', use_column_width=True) #musiman

    st.markdown(
        """
        <h3>siklis</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data pada time series yang terakhir adalah pola siklis. Pola siklis adalah data yang terpengaruh oleh fluktuasi ekonomi atau semacamnya dalam jangka yang panjang di dalam data. Contoh pola siklis dapat dilihat bersama pada gambar berikut ini:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image('img/siklis.png', caption='Data Siklis', use_column_width=True) #siklis

    #Dataframe
    st.markdown(
        """
        <h3 style="text-align: center;">Data Pada Penelitian</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Data yang digunakan pada penelitian ini adalah data jamu Madura yang berasal dari PT. Jamu Firdaus Kurnia Indah Utama (Jafir Utama) dengan produk jamu yaitu Ratu Pil Rapet Wangi. Untuk detail dari data tersebut sebagai berikut:</p>
            <ol>
                <li>Dataset yang digunakan adalah dataset harian Jamu Ratu Pil Rapet Wangi</li>
                <li>Data diambil dari periode 7/9/2022 s/d 29/12/2023</li>
                <li>Jumlah data adalah 359 data</li>
                <li>Variabel yang digunakan adalah penjualan, persediaan, dan produksi.</li>
            </ol>
        </div>
        <p>Berikut adalah data (359 data) yang digunakan dalam penelitian ini.</p>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(data)

    # Visulaisasi dataset
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
    st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pola data dari ketiga variabel tersebut menunjukkan mempunyai pola stasioner. Namun, perlu dilakukan uji stasioneritas terlebih dahulu untuk benar-benar memastikan data memang stasioner. Jika data menunjukkan tidak stasioner, daat dilakukan differencing terhadap data</p>
        </div>
        """,
        unsafe_allow_html=True
    )

#-------------------------------------------------------------------------------------------------------------------------------------------------
elif selected == "Method":
    with st.sidebar:
        method_selected = st.radio(
                        "Choose the method",
                        ["Preprocessing :gear:", "Statistical Significance :bar_chart:", "K-Means  🔍", "ARIMA :chart_with_downwards_trend:"],
                        captions = ["Missing value handling", "Feature selection", "Outlier detection", "forecast"])
    if method_selected == "Preprocessing :gear:":
        st.markdown(
        """
        <h3 style="text-align:center;">Preprocessing</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Preprocessing digunakan untuk mempersiapkan data supaya dapat digunakan untuk proses selanjutnya, seperti menormalkan data, mengecilkan ukuran data, transformasi data, reduksi data, menghapus data, dan lain sebagainya. Teknik yang bisa digunakan dalam tahapan ini pada umumnya ada 2, yaitu menghapus data yang hilang dengan ketentuan data yang hilang tidak banyak dan yang kedua menggantinya dengan nilai rata-rata atau biasa disebut mean substitution. Mean substitution digunakan karena data yang digunakan haruslah stasioner (konstan dalam rata-rata). Untuk persamaan dalam mencari rata-rata dari data dapat dilihat pada persamaan berikut ini: </p>
        </div>
        """,
        unsafe_allow_html=True)
        st.latex(r'''
                Mean = \frac{1}{n} \sum_{i=1}^{n} X_i''')
        st.caption("Dimana X adalah data ke-i, dan n adalah jumlah data")
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <h3 style="text-align:center;">Preprocessing Pada Penelitian</h3>
            <p>Dari tahap preprocessing pada penelitian ini yang menggunakan mean substitution dalam missing value handling, maka didapatkan data yang telah siap digunakan untuk proses selanjutnya. Berikut adalah hasil dari preprocessing dalam penelitian ini.</p>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(data_clear)
        fig = px.line(data_clear, y=['penjualan', 'persediaan', 'produksi'], title='Penjualan, Persediaan, dan Produksi')
        st.plotly_chart(fig)

    elif method_selected == "Statistical Significance :bar_chart:":
        st.markdown(
        """
        <h3 style="text-align: center;">Statistical Significance</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Statistical significance bertujuan memilih fitur yang memungkinkan peramalan tertinggi antar grup. Penggunaan semua fitur dalam peramalan tidak memberikan hasil optimal dalam banyak keadaan. Selain itu, pemilihan fitur membantu individu dalam mendapatkan pemahaman yang lebih baik tentang aspek-aspek yang penting untuk mendiagnosis data yang relevan. Metode yang bisa digunakan adalah analisis korelasi pearson dan uji kolinearitas menggunakan VIF (Variance Inflation Factor). </p>
        </div>
        <h4>Korelasi Pearson</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Korelasi pearson merupakan metode yang digunakan untuk mengukur hubungan antara 2 variabel yang mengahsilkan nilai korelasi linear dalam rentang nilai korelasi -1 sampai 1. Nilai -1 berarti korelasi negatif sempurna, nilai 0 artinya tidak ada korelasi, dan nilai 1 artinya korelasi positif sempurna. Ambang batas korelasi pearson untuk penelitian ini adalah ≥0.5. Persamaan korelasi pearson dapat dilihat pada persamaan (1) dan (2).</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                P(x,y) = \frac{σxy}{σxσy} \cdots (1)\\
                σ(x,y) = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \cdots (2) \\''')
        st.caption("Dimana, P(x,y) adalah korelasi pearson, σxy adalah kovarian dari variabel x dan y, σx adalah standar deviasi dari variabel x, σy adalah standar deviasi (populasi) dari variabel y, x bar adalah rata-rata variabel x, y bar adalah rata-rata variabel y, dan n adalah jumlah data")
        st.markdown(
        """
        <h4>Variance Inflation Factor (VIF)</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Sedangkan untuk VIF digunakan untuk mengetahui apakah variabel independent mempunyai hubungan kolinearitas atau tidak. Jika hasilnya ≤1 maka tidak ada kolinearitas, jika >1 maka ada kolinearitas, sehingga variabel tersebut tidak dapat digunakan karena terdapat informasi yang hampir sama bahkan sama persis dengan variabel lainnya. Persamaan VIF bisa dilihat pada persamaan (3) dan persamaan (4).</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                VIF_i = \frac{1}{1-R_i^2} \cdots (3) \\
                R_i^2 = 1- \frac{\sum_{i=1}^{n} (x_{ij} - \hat{x}_{ij})^2}{\sum_{i=1}^{n} (x_{ij} - \bar{x}_j)^2} \cdots (4) \\''')
        st.caption("Dimana, VIF adalah Variance Inflation Factor ke-i, R squared adalah adalah nilai error R Squared predictor ke-i, xij adalah data ke ke-i pada variabel ke-j, x hat adalah nilai prediksi data ke-i pada variabel ke-j, x bar adalah nilai rata-rata variabel ke-j")
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Untuk mendapatkan nilai R Squared dalam persamaan tersebut, maka disini kami menggunakan Linear regression untuk mendapatkan nilai prediksi, persamaannya dapat dilihat pada persamaan (5) sampai (7).</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                \hat{y}_i = a + bx_i \cdots (5) \\
                a = \frac{n\sum_{i=1}^n y_i - b \sum_{i=1}^n x_i}{n} \cdots (6)\\
                b = \frac{n\sum_{i=1}^n x_i y_i - (\sum_{i=1}^n x_1)(\sum_{i=1}^n y_i)}{n\sum_{i=1}^n x_i^2 - (\sum_{i=1}^n x_i)^2} \cdots (7)''')
        st.caption("Dimana, y hat adalah prediksi ke-i pada variabel dependent, a adalah bias, b adalah bobot, x adalah data ke-i pada variabel independent, n adalah jumlah data")
        st.markdown(
        """
        <h3 style="text-align:center;">Seleksi Fitur Pada Penelitian</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Dari penelitian yang telah dilakukan menggunakan data jamu ratu pil rapet wangi dengan 3 variabel (penjualan, persediaan, dan produksi), maka hasil seleksi fitur menggunakan korelasi pearson dan VIF dapat dilihat pada tabel berikut ini:</p>
        </div>
        """, unsafe_allow_html=True)  
        st.dataframe(pearson) 
        st.dataframe(vif) 
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pada tabel diatas, korelasi penjualan terhadap produksi memiliki nilai 0.0112 yang masih dibawah ambang batas 0.5, begitupun korelasi persediaan terhadap produksi yang memiliki nilai 0.199 yang masih dibawah 0.5 yang artinya kedua variabel tersebut tidak mempunyai korelasi yang kuat atau signifikan terhadap variabel produksi.</p>
            <p>Sedangkan hubungan kolinearitas antar variabel independent baik penjualan maupun persediaan dibawah ambang batas 1 yang artinya kedua variabel tersebut tidak tergantung sama lain.</p>
            <p>Walaupun antar variabel independent tidak mempunyai kolinearitas, tetapi korelasi antar variabel dependent dan independent tidak memenuhi kriteria pada ambang batas, maka tidak ada variabel independent yang terpilih. Artinya, hanya variabel dependent (produksi) saja yang akan digunakan untuk tahap selanjutnya. 
        </div>
        """, unsafe_allow_html=True) 
    elif method_selected == "K-Means  🔍":
        st.markdown(
        """
        <h3 style="text-align: center;">K-Means Clustering</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>K-Means adalah salah satu diantara metode pengelompokkan yang non-hierarki menjadi satu kelompok atau lebih. Karakteristik dalam satu kluster (kelompok) mempunyai ciri-ciri yang sama, sedangkan setiap kluster mempunyai ciri-ciri yang berbeda. Metode K-Means dapat digunakan untuk mendeteksi data outlier.</p>
            <p>Data outlier merupakan data yang berbeda dengan data lainnya, sehingga menyebabkan hasil akhir dari analisis tidak valid. Oleh karena itu, metode untuk mendeteksi dan menghapus data outlier menjadi sangat penting. Berikut beberapa tahap untuk mendeteksi data outlier dengan metode K-Means:</p>
        </div>
        <ol>
            <li>Pemilihan jumlah k atau kluster</li>
            <li>Perhitungan jarak terhadap k menggunakan mahalanobis distance</li>
            <li>Hitung rata-rata centroid berdasarkan member kluster</li>
            <li>Ulangi langkah 1-3 sampai rata-rata cluster tidak berubah atau mencapai maksimum iterasi (100)</li>
            <li>Data yang berada pada cluster dengan jumlah paling sedikit dianggap sebagai data outlier dan dihapus dari dataset.</li>
            <li>Jika hasil akhir menunjukkan panjang dataset baru ≥70% dari dataset lama, maka dataset baru tersebut dapat digunakan untuk proses selanjutnya. Namun, jika Panjang dataset <70% dari dataset asli maka dilakukan klasterisasi ulang.</li>
        </ol>
        <h4>Mahalanobis distance</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Mahalanobis distance merupakan salah satu metode untuk menghitung jarak data yang sering digunakan dalam clustering. Pada penelitian ini, perhitungan jarak mahalanobis digunakan untuk deteksi data outlier pada K-Means clustering. Untuk persamaannya dapat dilihat pada persamaan (1), sedangkan untuk variabel yang jumlahnya 1 dapat dilihat pada persamaan (2).</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                d = \sqrt{(x-\mu)^{T\sum^{-1}}(x-\mu)} \cdots (1)''')
        st.caption("Dimana, x adalah vektor dari variabel x = (x_1,x_2,…,x_k), μ = (μ_1,μ_2,…,μ_k) adalah vektor rata-rata berdimensi k, dan Σ adalah matriks kovarian")
        st.latex(r'''
                d = \sqrt{\frac{(X_i-\bar{X})^2}{s^2}} \cdots (2)''')
        st.caption("Dimana, Dimana X_i adalah data X ke-i, X ̅ adalah rata-rata data X, s adalah standar deviasi, dan s^2 adalah varians")
        st.markdown(
        """
        <h4>Elbow Method</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Untuk mendapatkan nilai k yang terbaik, dilakukan clustering dengan proses yang sama namun dengan percobaan k yang berbeda-beda. Nilai k yang akan digunakan adalah 1 s/d 10. Metode evaluasi yang digunakan yaitu metode elbow yang dikenal paling optimal dalam melakukan pengelompokkan dibandingkan metode silhouette. Berikut merupakan persamaan (3) untuk metode elbow.</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                SSE = \sum_{K=1}^K \sum_{x_i eS_K} ||X_i - C_K ||^2 \cdots (3)''')
        st.caption("Dimana X_i adalah nilai atribut dari data ke-i, k adalah centroid, dan  C_k adalah nilai atribut titik pusat cluster ke-k.")

        st.markdown(
        """
        <h3 style="text-align: center;">Deteksi Outlier Pada Penelitian</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Deteksi outlier pada penelitian ini melalui beberapa tahapan seperti yang telah dijelaskan sebelumnya. Hasilnya adalah sebagai berikut:</p>
        </div>
        <h4>K optimal</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Dari pengelompokan yang dilakukan dengan jumlah k berbeda dari 1 - 10 menggunakan metode Elbow membentuk siku-siku pada jumlah K=3. Oleh sebab itu, maka K yang akan digunakan adalah 3</p>
        </div>
        """, unsafe_allow_html=True)
        st.image('img/elbow.png', caption='Elbow', use_column_width=True)
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Setelah mendapatkan K optimal yaitu k=3. Proses selanjutnya yaitu melakukan cluestering terhadap semua data dan didapatkan hasil jarak dan cluster untuk setiap data sebagai berikut:</p>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(distance)
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Dari clustering yang dilakukan, untuk mengetahui data outlier maka data dikelompokkan berdasarkan clusternya. Member cluster yang anggotaya paling sedikit dianggap sebagai data outlier. Hasil tersebut dapat dilihat ada tabel berikut ini.</p>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(outlier)
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Dari hasil diatas, maka cluster 1 dengan jumlah data 32 dianggap sebagai data outlier dan dihapus dari dataset. Setelah dihapus, panjang dataset yang baru terhadap dataset lama yaitu sebesar 91.0863509749303%. Sehingga, dataset tersebut dapat digunakan untuk proses selanjutnya. Berikut adalah visualisasi dari hasil clustering</p>
        </div>
        """, unsafe_allow_html=True)
        st.image('img/clustering_plot.png', caption='Plotting cluster', use_column_width=True)
    elif method_selected == "ARIMA :chart_with_downwards_trend:":
        st.markdown(
        """
        <h3 style="text-align: center;">ARIMA (Autoregressive Integrated Moving Average)</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>ARIMA merupakan model ML (Machine Learning) terkenal yang sangat populer untuk data deret waktu dan memiliki akurasi baik untuk kumpulan data kecil. ARIMA merupakan peramalan deret waktu statistik yang paling populer dan efektif, ARIMA diciptakan oleh George Box dan Gwilym Jenkins. Dengan menggunakan berbagai data historis dan kesalahan acak, model ARIMA memprediksi nilai masa depan dari suatu asumsi variabel</p>
            <p>ARIMA merupakan pendekatan peramalan deret waktu yang digunakan dalam memprediksi masa depan nilai suatu variabel dari nilai masa lalunya. Menggabungkan urutan perbedaan untuk dihapus tren dan/atau musiman. Model ARIMA meliputi model Autoregressive (AR), model Moving Average (MA), dan model Autoregressive Moving Average (ARMA). Model ARIMA mempunyai parameter (p, d, q)  dimana p adalah jumlah suku autoregresif, d adalah banyaknya proses stasioneritas, dan q adalah suku moving average. Prosess prediksi menggunakan ARIMA terdiri dari identifikasi model, estimasi parameter, verifikasi model, dan prediksi aktual</p>
        </div>
        <h4>Identifikasi Parameter</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Tahapan identifikasi dilakukan untuk penaksiran parameter p, d, dan q. Data yang digunakan haruslah stasioner, untuk mengetahui apakah data yang digunakan sudah stasioner atau tidak dapat menggunakan uji ADF (Augmented Dickey-Fuller) dengan hipotesis sebagai berikut:</p>
        </div>
        <h6>H0: Data tidak stasioner</h6>
        <h6>H1: Data stasioner</h6>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Dengan ketentuan jika t-statistik ≥ADF, H0 diterima. Bisa juga menggunakan nilai probabilitas dengan ketentuan jika probabilitas ≥a maka H0 diterima, namun jika probabilitas < a maka H0 ditolak. Untuk a adalah nilai signifikan, yaitu 0.05</p>
            <p>Persamaan untuk uji ADF dapat dilihat pada persamaan (1) dan (2) yang mana pada persamaan (2) digunakan untuk yang lebih spesifik dengan menggunakan koefisien</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                ∆Y_t = δY_{t-1}+α_i \sum_{i=1}^m ∆Y_{t-i}+ε_t\cdots (1) \\
                ∆Y_t = β_1+β_2 t+δY_{t-1}+α_i \sum_{i=1}^m ∆Y_{t-i} +ε_t \cdots (2)''')
        st.caption("Dimana ∆Y_t variabel yang diamati pada waktu ke-t, α intercept, ε_t residual  pada waktu ke-t, m jumlah lag, dan β koefisien.")
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>JIka hasil menunjukkan data tidak stasioner, maka dilakukan differencing terhadap data menggunakan persamaan (3) dan persamaan (4) untuk second differencing. Proses ini dilakukan untuk mencari nilai parameter d</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                ∆Z_t = Z_t - Z_{t-1} \cdots (3) \\
                ∆^2Z_t =∆Z_t - Z_{t-1} =(Z_t - Z_{t-1}) - (Z_{t-1} - Z_{t-2})  \cdots (4)''')
        st.caption("Dimana Z_t data pada waktu ke-t.")
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Setelah mendapatkan nilai parameter d, selanjutnya menaksirkan nilai parameter p dan q. Untuk dapat mengetahui nilai parameter p dan q menggunakan ACF (Autocorrelation Function) dan PACF (Partial Autocorrelation Function). Untuk persamaan ACF bisa dilihat pada persamaan (5) dan PACF persamaan (6) dan (7) </p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                r_k = \frac{Y_k}{Y_0} = \frac{\sum_{t=k+1}^n(X_t - \bar{X})(X_{t-k} - \bar{X})}{\sum_{t=1}^n(X_t - \bar{X})^2} \cdots (5) \\\
                ∅_{kk} = \frac{r_k-\sum_{j=1}^{k-1}∅_{k-1},jr_{k-j}}{1-\sum_{j=1}^{k-1}∅_{k-1},jr_j}  \cdots (6) \\
                ∅{k,j} = ∅_{k-1,j} - ∅_{kk}∅_{k-1,k-j} \cdots (7)''')
        st.caption("Dimana X_t nilai dari data pada periode ke-t, X ̅ rata-rata data, k waktu lag, n jumlah data, dan j adalah 1,2,…,k-1.")
        
        st.markdown(
        """
        <h4>Estimasi Parameter</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Setelah mendapatkan beberapa model, selanjutnya yaitu mengestimasi nilai parameter dari model-model tersebut. Ada beberapa cara untuk mengestimasi parameter model ARIMA, salah satunya adalah menggunakan MLE (Maximum Likelihood Estimation) yang merupakan salah satu metode estimasi pada ARIMA yang umum digunakan. Fungsi MLE untuk model ARIMA ataupun ARMA dapat dilihat pada persamaan (8)</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                L(∅,θ,σ^2) = ∏_{i=1}^n \frac{1}{√2πσ}exp(-\frac{ε_i^2}{2σ^2}) \cdots (8) ''')
        st.caption("Dimana ∅ merupakan koefisien parameter AR, θ koefisien parameter MA, σ^2 varians, dan ε adalah error.")

        st.markdown(
        """
        <h4>Verifikasi Model</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Untuk memvalidasi model layak digunakan untuk tahap selanjutnya atau tidak dapat dilakukan dengan beberapa cara, diantaranya adalah menggunakan uji residual. Residual  sendiri dapat dihitung dengan cara mencari nilai selisih antara data ramalan dengan data aktual. Dengan menggunakan data residual al, maka bisa dilakukan uji normalitas residual menggunakan uji Kolmogorov-Smirnov dengan menggunakan persamaan (9) dengan hipotesis sebagai berikut:</p>
        </div>
        <h6>H0: Data residual berdistribusi normal</h6>
        <h6>H1: Data residual tidak berdistribusi normal</h6>
        """, unsafe_allow_html=True)
        st.latex(r'''
                Thitung = Maks |F(X) - S(X)| \cdots (9) ''')
        st.caption("Dimana F(X) adalah Fungsi distribusi kumulatif dari distribusi normal dan S(X) Fungsi distribusi kumulatif dari distribusi pengamatan.")
        st.markdown(
        """
        <h4>Prediksi</h4>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Model ARIMA terdiri dari komponen AR dan MA, sehingga terbentuk beberapa model, seperti AR, MA, dan ARMA. Berikut adalah persamaan yang digunakan untuk melakukan prediksi.</p>
        </div>
        <h6>Model AR</h6>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Model AR (Autoregressive) merupakan proses AR time series linear yang berorde p. Persamaan AR dapat dilihat pada persamaan (10) dan persamaan (11) untuk ARX (dengan variabel Exogen)</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                Z_t = ∅_1Z_{t-1}+∅_2Z_{t-2}+...+∅_pZ_{t-p}+α_t \\
                (1-∅_1B-∅_2B^2 - ... -∅_pB^p)Z_t=α_t\\
                ∅_p(B)Z_t = α_t \cdots (10)\\
                Z_t = ∅_1Z_{t-1}+∅_2Z_{t-2}+...+∅_pZ_{t-p}+βx_t+α_t \cdots (11)''')
        st.caption("Dimana Z_t adalah proses AR pada waktu ke-t, α_t galat waktu ke-t, ∅ koefisien parameter AR, B operator backshift AR, β adalah koefisien variabel exogen, dan x adalah variabel exogen ")
        st.markdown(
        """
        <h6>Model MA</h6>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Model MA (Moving Average) juga merupakan model time series linear yang terbentuk dari galat atau error pada waktu ke-t dengan diberi bobot [18], [27]. Persamaan dari model MA dapat dilihat pada persamaan (12) dan persamaan (13) untuk MAX.</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                Z_t = α_t + θ_1 α_{t-1}+θ_2 α_{t-2}+…+θ_q α_{t-q} \\
                Z_t=(1+θ_1 B+θ_2 B^2+…+∅_p B^p ) α_t\\
                Z_t= θ_q (B)α_t \cdots (12)\\
                Z_t = βx_t + α_t + θ_1 α_{t-1}+θ_2 α_{t-2}+…+θ_q α_{t-q} \cdots (13)''')
        st.caption("Dimana Z_t proses MA pada waktu ke-t, α_t galat waktu ke-t, θ koefisien parameter MA, B operator backshift MA, β adalah koefisien variabel exogen, dan x adalah variabel exogen")
        st.markdown(
        """
        <h6>Model ARMA</h6>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Model ARMA merupakan gabungan dari model AR dengan parameter p dan model MA dengan parameter q. persamaan ARMA dapat dilihat pada persamaan (14) dan persamaan (15) untuk ARMAX.</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                ∅_p (B) Z_t=`θ_q (B) α_t \\
                (1-∅_1 B-∅_2 B^2-…-∅_p B^p ) Z_t=(1-θ_1 B-θ_2 B^2-…-∅_p B^p ) α_t\\
                Z_t=∅_1 Z_(t-1)+⋯+∅_p Z_(t-p)+α_t-θ_1 α_(t-1)-…θ_p α_(t-q) \cdots (14)\\
                Z_t=βx_t + ∅_1 Z_(t-1)+⋯+∅_p Z_(t-p)+α_t-θ_1 α_(t-1)-…θ_p α_(t-q) \cdots (15)''')
        st.caption("Dimana Z_t proses MA pada waktu ke-t, α_t galat waktu ke-t, ∅ koefisien parameter AR, θ koefisien parameter MA, B operator backshift, β adalah koefisien variabel exogen, dan x adalah variabel exogen")
        st.markdown(
        """
        <h6>Model ARIMA</h6>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Untuk model ARIMA digunakan untuk data yang stasioner atau telah dilakukan differencing untuk data yang belum stasioner hingga stasioner. Model tersebut mempunyai parameter (p,d,q) yang merupakan gabungan dari model AR (p), MA(q), dan proses differencing (d). Berikut merupakan persamaan ARIMA yang bisa dilihat pada persamaan (16)</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''
                ∅(B) (1-B)^d Z_t=θ_q (B)α_t \\
                Y_t=c+∅_1 Y_(t-1)+⋯+∅_p Y_(t-p)+θ_1 ε_(t-1)+⋯+θ_q ε_(t-q)+ε_t \cdots (16) \\
                Y_t=βx_t + c+∅_1 Y_(t-1)+⋯+∅_p Y_(t-p)+θ_1 ε_(t-1)+⋯+θ_q ε_(t-q)+ε_t \cdots (15)''')
        st.caption("Dimana Z_t proses MA pada waktu ke-t, α_t galat waktu ke-t, ∅ koefisien parameter AR, θ koefisien parameter MA, B operator backshift, β adalah koefisien variabel exogen, dan x adalah variabel exogen")
        st.markdown(
        """
        <h3 style="text-align: center;">ARIMA Pada Penelitian</h3>
        <div style="text-align: justify; text-indent: 30px;">
            <p>Pada penelitian ini, dataset dipisah menjadi data latih dan dat uji menggunakan k-fold cross validation time series split dengan dengan k=5. berikut adalah ilustrasi dari time series split.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image('img/split.png', caption='Time Series split', use_column_width=True)
        st.markdown(
        """
        <div style="text-align: justify; text-indent: 30px;">
            <p>Setelah melakukan split dataset, didapatkan model terbaik terdapat pada fold 2 dengan rincian sebagai berikut:</p>
        </div>
        """, unsafe_allow_html=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------
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
