# Name Recomonder Web App

Repository ini berisi file untuk deployment model _machine learning_ yaitu sitem rekomondasi dengan metode _COntent-based filtering_ adapun value yang diambil adalah:

- Deskripsi yang dijadikan dalam bentuk vector dengan pembobotan TFIDF
- Hasil kemudian di Hitung dengan persamaaan _Cosine Simalirity_

---

## Beberapa deskripsi file dalam repository

- index.html --> sebuah file untuk halaman pembuka berisi tentang website tersebut
- df_nodc.csv --> merupakan data yang berisi nama-nama dalam berbagai bahasa yaitu indonesaia, jawa dan arab

- app.py --> meupakan konfigurasi untuk pemanggilan api
- app_recom.html --> merupakan fitur utama dalam website yang menampilkan hasil dari deskripsi tersebuat

### Tampilan

adapun tmapilan akan menjadi seperti ini:

<div  align="center" >
<img src="landing-page.png" width ="100"/>
<img src="page.png" width="100"/>

</div>
