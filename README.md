# **Tugas 2 PBP**

Nama    : Alexander Audric Johansyah <br>
NPM     : 2206815466 <br>
Kelas   : PBP <br>
App     : 

# Membuat sebuah Django Projek
1. Buat direktori yang ingin kita gunakan untuk membuat proyek Django
2. Buka command prompt di dalam direktori yang sudah kita buat sebelumnya
3. Buatlah virtual enviroment dengan menjalankan perintah `python -m venv env` pada command prompt untuk mengisolasi package dan dependencies dari aplikasi lain
4. Aktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (Windows) atau `source env/bin/activate` (Linux/Mac).
5. Siapkan dependencies dengan membuat file pada direktori yang sama, dan diberi nama `requirements.txt` lalu tambahkan dependencies: `django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3`
6. Install dependencies yang diperlukan dengan perintah `pip install -r requirements.txt` dengan menjalankan virtual environment
7. Buat proyek Django dengan menjalankan perintah `django-admin startproject (nama_aplikasi) .`
8. Buka file `settings.py` yang ada di dalam folder proyek, lalu cari variabel `ALLOWED_HOSTS` dan ubah nilainya menjadi `["*"]` untuk mengizinkan akses dari semua host
9. Kembali ke command prompt, jalankan perintah `python manage.py runserver` di dalam direktori proyek untuk menjalankan server
10. Buka proyek Django baru di browser dengan mengakses http://localhost:8000
11. Untuk menghentikan server,  tekan `Ctrl+C` (Windows) atau `Control+C` (Mac)
12. Nonaktifkan virtual environment dengan perintah `deactivate`

# Membuat aplikasi dengan nama main pada proyek tersebut
1. Buka direktori proyek utama dan aktifkan virtual environment.
2. Buat folder baru dengan nama main dengan menjalankan perintah `python manage.py startapp main`
3. Daftarkan aplikasi main ke dalam proyek dengan membuka berkas `settings.py` dan menambahkan `'main'` di variabel `INSTALLED_APPS` di direktori proyek utama

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main
1.  Buat berkas `urls.py` di dalam direktori main dan isi dengan kode berikut:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
2. Berkas `urls.py` pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib name (CharField), amount (IntegerField), description (TextField)
1. Buka berkas `models.py` dan isi file tersebut dengan kode ini:
    ```python
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()
    ```
2. Migrasi model dengan menjalankan perintah `python manage.py makemigrations`
3. Jalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam basis data lokal

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
1. Buat direktori baru bernama templates di direktori main
2. Di dalam direktori templates, buat berkas baru bernama main.html
3. Buka berkas `views.py` yang ada di berkas aplikasi main, tambahkan baris impor berikut di bagian atas:
    ```python
    from django.shortcuts import render
    ```
4. Tambahkan fungsi show_main di bawah impor:
    ```python
    def show_main(request):
        context = {
            (isi dengan data yang akan dikirim ke tampilan, dalam bentuk dictionary)
        }

        return render(request, "main.html", context)
    ```
5. Buka berkas `main.html` dan ubah sesuai dengan kententuan soal. Sebagai contoh:
    ```html
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    <h5>NPM: </h5>
    <p>{{ npm }}<p>
    ```
# Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. Buka berkas `urls.py` di dalam direktori proyek utama, bukan yang ada di dalam direktori aplikasi main
2. Impor fungsi include dari django.urls
    ```python
    from django.urls import path, include
    ```
3. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns:
    ```python
    urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
    ]
    ```
4. Jalankan proyek Django dengan perintah `python manage.py runserver`
5. Bukalah http://localhost:8000/main/ di peramban web untuk melihat halaman yang sudah kamu buat

# Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
1. Buat akun `Adaptable.io` menggunakan akun GitHub yang digunakan untuk membuat proyek tugas 2 ini
2. Login dan tekan tombol New App. Pilih `Connect an Existing Repository`
3. Hubungkan `Adaptable.io` dengan GitHub dan pilih `All Repositories` pada proses instalasi
4. Pilihlah repositori proyek yang diinginkan sebagai basis aplikasi yang akan di-deploy. Pilih branch yang ingin dijadikan sebagai deployment branch
5. Pilihlah `Python App Template` sebagai template deployment
6. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
7. Sesuaikan versi Python dengan spesifikasi aplikasi. 
8. Pada bagian Start Command masukkan perintah `python manage.py migrate && gunicorn (nama direktori utama).wsgi`
9. Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu
10. Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi

# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
User akan melakukan request yang merupakan awal dari proses ini Django kemudian akan memproses URL dari client dan menyesuaikannya sesuai dengan file urls.py yang berisi pengaturan URL yang menghubungkan URL yang diminta oleh client dengan view (fungsi) yang akan menangani permintaan tersebut. Lalu, Django akan akan membuka file views.py yang mengontrol logika dan meminta tampilan. Setelah itu, file models.py akan menangani data yang sesuai permintaan user dan folder template akan berisi file dengan extension html. File extension html tersebut akan berisi berbagai kode html untuk mengatur tampilan bagi user. Setelah selesai, tampilan akan muncul untuk user.

# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Setiap proyek Python dapat memiliki dependensi atau paket Python yang berbeda-beda, dengan versi yang berbeda. Virtual environment memungkinkan kita untuk membuat lingkungan terisolasi yang mandiri untuk setiap proyek, sehingga kita dapat mengelola dependensi dengan lebih baik. Ini membantu menghindari konflik antara paket dan versi yang mungkin digunakan dalam proyek yang berbeda. Proyek Django masih bisa dibuat tanpa menggunakan virtual environment, namun penggunaan virtual environment adalah praktik terbaik dalam pengembangan Python dan dapat menghindari banyak masalah yang mungkin timbul akibat konflik antar-paket dan versi. Dengan virtual environment, kita dapat membuat dan mengelola lingkungan pengembangan yang bersih dan terisolasi untuk setiap proyek Django kita, yang akan membuat proses pengembangan lebih teratur, efisien, dan terkendali.

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
 MVC, MVT, dan MVVM adalah tiga kerangka arsitektur *software* yang berbeda digunakan dalam *software development*. Mereka memiliki konsep dasar yang serupa, yaitu memisahkan komponen dalam aplikasi agar lebih terorganisir dan mudah dikelola. 

1. MVC (Model-View-Controller):
    Model: Representasi data dan logika dari aplikasi. Model mengelola data, berisi logika, dan mengurus komunikasi dengan database atau sumber data lainnya.
    View: Menampilkan data dari Model kepada pengguna. View menggambarkan tampilan *user interface*.
    Controller: Bertindak sebagai penghubung antara Model dan View. Controller mengatur aliran data antara Model dan View, mengolah input dari pengguna, dan memutuskan bagaimana merespons perubahan-perubahan dalam Model.

    MVC digunakan dalam pengembangan aplikasi web, desktop, mobile. Controller bertanggung jawab memperbarui Model dan View sesuai kebutuhan.

2. MVT (Model-View-Template):
    Model: Model menangani logika dan data seperti MVC
    View: Tampilan *user interface* yang menampilkan data Model. Tidak memiliki logika seperti MVC.
    Template:  Menangani bagaimana data Model ditampilkan dalam View. Template memisahkan kode HTML dari kode Python (atau bahasa pemrograman lainnya) yang digunakan untuk mengisi data dalam tampilan.

    MVT biasanya digunakan dalam kerangka kerja web yang didasarkan pada Python. Perbedaan utama antara MVT dengan MVC adalah Template dan View. Template memisahkan tampilan dari logika.

3. MVVM (Model-View-ViewModel):
    Model: Model mengelola data dan logika mirip seperti MVC.
    View: Ini adalah tampilan *user interface* yang menampilkan data dari ViewModel.
    ViewModel: ViewModel menghubungkan Model dan View. Ini berisi kode yang memformat dan mengelola data dari Model agar sesuai dengan tampilan yang diperlukan oleh View. ViewModel juga menerima input dari View dan memperbarui Model jika diperlukan.

    MVVM digunakan untuk merancang aplikasi berbasis *user interface* yang kompleks, seperti aplikasi mobile atau aplikasi desktop dengan tampilan yang dinamis. Ini memungkinkan pemisahan yang kuat antara logika dan tampilan.