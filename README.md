# Nama    : Alexander Audric Johansyah

Link Tugas:<br>
[Tugas 2](#tugas-2) <br>
[Tugas 3](#tugas-3) <br>
[Tugas 4](#tugas-4) <br>
[Tugas 5](#tugas-5) <br>
[Tugas 6](#tugas-6) 

# **Tugas 2**
## Membuat sebuah Django Projek
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

## Membuat aplikasi dengan nama main pada proyek tersebut
1. Buka direktori proyek utama dan aktifkan virtual environment.
2. Buat folder baru dengan nama main dengan menjalankan perintah `python manage.py startapp main`
3. Daftarkan aplikasi main ke dalam proyek dengan membuka berkas `settings.py` dan menambahkan `'main'` di variabel `INSTALLED_APPS` di direktori proyek utama

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main
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

## Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib name (CharField), amount (IntegerField), description (TextField)
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

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
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
## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
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

## Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
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

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan](https://raw.githubusercontent.com/audricjohansyah/PBP-Tugas2/9bed03bb2113695a9b8b6997de87d1a0d00a1eed/Bagan%20PBP.jpg)

User akan melakukan request yang merupakan awal dari proses ini Django kemudian akan memproses URL dari client dan menyesuaikannya sesuai dengan file urls.py yang berisi pengaturan URL yang menghubungkan URL yang diminta oleh client dengan view (fungsi) yang akan menangani permintaan tersebut. Lalu, Django akan akan membuka file views.py yang mengontrol logika dan meminta tampilan. Setelah itu, file models.py akan menangani data yang sesuai permintaan user dan folder template akan berisi file dengan extension html. File extension html tersebut akan berisi berbagai kode html untuk mengatur tampilan bagi user. Setelah selesai, tampilan akan muncul untuk user.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Setiap proyek Python dapat memiliki dependensi atau paket Python yang berbeda-beda, dengan versi yang berbeda. Virtual environment memungkinkan kita untuk membuat lingkungan terisolasi yang mandiri untuk setiap proyek, sehingga kita dapat mengelola dependensi dengan lebih baik. Ini membantu menghindari konflik antara paket dan versi yang mungkin digunakan dalam proyek yang berbeda. Proyek Django masih bisa dibuat tanpa menggunakan virtual environment, namun penggunaan virtual environment adalah praktik terbaik dalam pengembangan Python dan dapat menghindari banyak masalah yang mungkin timbul akibat konflik antar-paket dan versi. Dengan virtual environment, kita dapat membuat dan mengelola lingkungan pengembangan yang bersih dan terisolasi untuk setiap proyek Django kita, yang akan membuat proses pengembangan lebih teratur, efisien, dan terkendali.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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

# **Tugas 3**
## Apa perbedaan antara form POST dan form GET dalam Django?
POST biasanya digunakan untuk mengirim data yang akan membuat perubahan di sisi server seperti untuk membuat atau menulis ulang sumber daya/data tertentu. POST biasa digunakan untuk mengirim data yang sensitif seperti password, data tersebut disembunyikan dari URL. Data yang dikirim ke server ini disimpan di badan permintaan permintaan HTTP. Maka dari itu, POST lebih aman daripada GET karena data tidak tampil di URL berarti data sensitif tidak akan tampil secara terbuka.

GET biasanya digunakan di sisi klien (Browser) untuk mengirim permintaan ke server tertentu untuk mendapatkan data atau sumber daya tertentu. GET digunakan untuk permintaan pencarian yang tidak mengubah apapun. GET mengirim data sebagai parameter yang terlihat di URL dan data tersebut terbatas ukurannya. GET digunakan untuk data yang kurang aman karena terlihat di URL dan dapat diakses oleh pihak ketiga

*Source*: https://www.geeksforgeeks.org/difference-between-http-get-and-post-methods/

## Perbedaan Utama Antara XML, JSON, dan HTML Dalam Konteks Pengiriman Data
- ## JSON (*JavaScript Object Notation*)<br>
    JSON didesain menjadi *self-describing*, sehingga mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat di bahasa pemrograman.
    Data pada JSON disimpan dalam bentuk key dan value. Value dapat berupa tipe data primitif (string, number, boolean) ataupun berupa objek. JSON biasa yang digunakan untuk pertukaran data antara aplikasi.

- ## XML (*Extensible Markup Language*)<br>
    XML didesain menjadi *self-descriptive*, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML hanya berisi informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. Dokumen XML membentuk  data dalam struktur tree dengan namespace untuk kategori data yeng berbeda. Hanya dapat di-*parsed* menggunakan pengurai XML Mendukung semua tipe data JSON, Boolean, tanggal, gambar, dan namespace. XML sering digunakan untuk pertukaran data yang terstruktur antara aplikasi.
- ## HTML (*HyperText Markup Language*)<br>
    HTML adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web. HTML fokus pada representasi visual dan interaksi pengguna pada halaman web.

Kesimpulan, XML digunakan untuk mendefinisikan struktur data, JSON digunakan untuk pertukaran data, dan HTML digunakan untuk mengatur tampilan dan interaksi pada halaman web.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Sintaks yang digunakan JSON mudah untuk ditulis dan dibaca oleh manusia
- Sintaks merupakan turunan dari Object JavaScript yang membuat JSON banyak digunakan di aplikasi web dan mobile.
- JSON didesain menyediakan format yang sederhana serta ringkas dan data pada JSON disimpan dalam bentuk key dan value.
- JSON dapat diurai menggunakan fungsi JavaScript standar yang merupakan bahasa pemrograman yang umum digunakan dalam pengembangan aplikasi web. 
- Perbedaan syntax dan ukuran file JSON juga membuat *parsing* JSON lebih cepat dibandingkan XML.
- JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat.
- Penguraian JSON lebih aman dibandingkan XML. Struktur XML rentan *unauthorized modification* dan deklarasi tipe dokumen eksternal yang tidak terstruktur.

## Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Buat berkas baru di direktori main dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data produk baru. Masukkan kode berikut.
    ```python
    #Sesuaikan dengan kebutuhan
    from django.forms import ModelForm
    from main.models import Product

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["album", "year", "artist"]
    ```
2. Buka berkas `views.py` yang ada pada folder main dan tambahkan beberapa import berikut.
    ```python
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    ```
3. Buat fungsi baru dengan nama untuk membuat item pada berkas tersebut yang menerima parameter request dan tambahkan potongan kode di bawah ini untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form.
    ```python
    def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```
4. Ubahlah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut.
    ```python
    #Sesuaikan nama model
    def show_main(request):
        items = Item.objects.all() #Tambahkan ini

        context = {
            ....
            'items': items #Tambahkan ini
            ....
        }

        return render(request, "main.html", context)
    ```
5. Buka `urls.py` yang ada pada folder main dan import fungsi yang sudah dibuat tadi.
    ```python
    from main.views import show_main, create_product
    ```
6. Tambahkan path url ke dalam urlpatterns pada `urls.py` di main untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.
    ```python
    path('create-product', create_product, name='create_product'),
    ```
7. Buat berkas HTML baru pada direktori `main/templates` dan isi dengan kode berikut.
    ```python 
    #Sesuaikan dengan kebutuhan
    {% extends 'base.html' %} 

    {% block content %}
    <h1 class="requestalbum">Request Album</h1>

    <form method="POST">
        {% csrf_token %}
        <table class="table">
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input class="content" type="submit" value="Request"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
8. Buka `main.html` dan tambahkan kode berikut di dalam `{% block content %}` untuk menampilkan data produk dalam bentuk table serta tombol yang akan redirect ke halaman form.
    ```python
    #Ubah sesuai kebutuhan
    ...
    ...
    ...
    <h1 class="addalbum">Request an album</h1>
    <h2 class="albumcount">Album requested: {{item_count}}</h2>
    <table class="tg">
        <tr>
            <th class="tg-tqnx">Album</th>
            <th class="tg-tqnx">Year</th>
            <th class="tg-tqnx">Artist</th>
            <th class="tg-tqnx">Date Requested</th>
        </tr>
        {% for item in items %}
            <tr>
                <td class="tg-hv44">{{item.album}}</td>
                <td class="tg-hv44">{{item.year}}</td>
                <td class="tg-hv44">{{item.artist}}</td>
                <td class="tg-hv44">{{item.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_product' %}">
        <button class="content">
            Request album
        </button>
    </a>
    {% endblock content %}
    ```
## Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
## Mengembalikan Data dalam Bentuk XML
1. Buka `views.py` yang ada pada folder main dan tambahkan import `HttpResponse` dan `Serializer` pada bagian paling atas.
    ```python
    from django.http import HttpResponse
    from django.core import serializers
    ```
2. Buatlah sebuah fungsi yang menerima parameter request dengan nama `show_xml` dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada `Item`. Tambahkan return function berupa *HttpResponse* yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`.
    ```python
    #Sesuaikan dengan nama model
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

3. Buka `urls.py` yang ada pada folder `main` dan import fungsi yang sudah kamu buat tadi.
    ```python
    from main.views import show_main, create_product, show_xml 
    ```

4. Tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('xml/', show_xml, name='show_xml'), 
    ...
    ```
5. Jalankan proyek Django-mu dengan perintah `python manage.py runserver` dan bukalah http://localhost:8000/xml di browser.

## Mengembalikan Data dalam Bentuk JSON
1. Buka `views.py` yang ada pada folder main dan buatlah sebuah fungsi baru yang menerima parameter request dengan nama `show_json` dengan sebuah variabel di dalamnya yang menyimpan hasil query dari seluruh data yang ada pada Item. Tambahkan return function berupa *HttpResponse* yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter `content_type="application/json"`
    ```python
    #Sesuaikan dengan nama model
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")show_xml 
    ```
2. Buka `urls.py` yang ada pada folder `main` dan import fungsi yang sudah kamu buat tadi.
    ```python
    from main.views import show_main, create_product, show_xml, show_json
    ```

3. Tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('json/', show_json, name='show_json'), 
    ...
    ```
4. Jalankan proyek Django-mu dengan perintah `python manage.py runserver` dan bukalah http://localhost:8000/json di browser.

## Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
1. Buka `views.py` yang ada pada folder `main` dan buatlah sebuah fungsi baru yang menerima parameter request dan id dengan nama `show_xml_by_id` dan `show_json_by_id`

2. Buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada Item. Rambahkan return function berupa *HttpResponse* yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter *content_type* dengan value `"application/xml" (untuk format XML)` atau `"application/json" (untuk format JSON)`
    - XML
        ```python
        #Sesuaikan dengan nama model
        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")show_xml 
        ```
    - JSON
        ```python
        #Sesuaikan dengan nama model
        def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```

3. Buka `urls.py` yang ada pada folder `main` dan impor fungsi yang sudah kamu buat tadi.
    ```python
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
    ```
4. Tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ...

    ```
5. Jalankan proyek Django-mu dengan perintah `python manage.py runserver` dan bukalah http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] di browser.

## Screenshot hasil akses URL pada Postman dan HTML
### HTML View
![HTML View](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/HTML%20View.jpg?raw=true)
### JSON View
![JSON View](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/JSON%20View.jpg?raw=true)
## XML View
![XML View](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/XML%20View.jpg?raw=true)

### JSON View by ID
![JSON View by ID](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/JSON%20View%20by%20ID.jpg?raw=true)

### XML View by ID
![XML View by ID](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/XML%20View%20by%20ID.jpg?raw=true)

# **Tugas 4**
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal.

### Kelebihan
- Sudah tersedia implementasi form pendaftaran yang sudah siap untuk dipakai sehingga tidak perlu diprogram kembali dari awal sehingga tidak membuang waktu dan tenaga.
- Form sudah terintegrasi *build-in user authentication system*. Konfigurasi tersebut melakukan kebutuhan umum suatu project dan validasi *password* dan *permissions*. Hal tersebut membuat user yang sudah terdaftar dapat melakukan login dengan mudah setelah pendaftaran.
- Form juga memiliki validasi bawaan untuk user secara otomatis, seperti validasi keunikan alamat email, penilaian tingkat keamanan password, dan mencocokkan konfirmasi kata sandi

### Kekurangan
- Perlu melakukan kustomisasi tambahan untuk mengadaptasinya sesuai dengan kebutuhan aplikasi. Misalnya, jika Anda ingin mengumpulkan informasi tambahan selain nama pengguna (username) dan kata sandi.
-  Tampilan default mungkin tidak sesuai dengan desain visual atau tata letak halaman yang diinginkan dan perlu menyesuaikan tampilan dengan menggunakan CSS atau mengganti template.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
### Autentikasi
Autentikasi adalah proses verifikasi identitas pengguna yang melakukan attempt untuk mengakses aplikasi. Proses ini memeriksa apakah pengguna adalah siapa yang dia klaim sebagai pengguna tersebut. Ini melibatkan verifikasi kredensial pengguna, seperti *username* dan *password*.

### Otorisasi
Otorisasi adalah proses verifikasi apakah suatu pengguna memiliki akses terhadap sesuatu pada aplikasi. Proses ini terjadi setelah autentikasi dan berkaitan dengan apa yang dapat dan tidak dapat dilakukan oleh pengguna dalam aplikasi.

Autentikasi dan otorisasi merupakan lapisan pertahanan keamanan penting dalam aplikasi. Autentikasi memastikan bahwa hanya pengguna yang sah yang memiliki akses ke aplikasi, sementara otorisasi mengendalikan apa yang dapat dilakukan oleh pengguna yang terautentikasi.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah data kecil yang disimpan di peramban web pengguna oleh server web saat berinteraksi dengan situs web. Mereka digunakan untuk berbagai tujuan, termasuk manajemen sesi, penyimpanan preferensi, pelacakan aktivitas pengguna, personalisasi konten, dan analisis penggunaan.

Dalam konteks Django, cookies digunakan untuk mengelola sesi pengguna. Django menyediakan dukungan bawaan untuk mengelola cookies dalam kerangka kerja aplikasi web. Kita dapat menggunakan cookies untuk menyimpan informasi sesi, seperti token otentikasi, preferensi pengguna, ataupun data lainnya.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara umum penggunaan cookie secara default (*session cookie*) yang bersifat sementara relatif aman. *Session cookie* disimpan di memori browser, jika browser ditutup cookie akan dihapus dan bersifat lebih aman karena hanya dapat diakses browser dan tidak bisa digunakan untuk melacak informasi jangka panjang.

Akan tetapi, ada beberapa risiko potensial yang perlu diwaspadai terkait dengan cookies:

1. Cookies dapat digunakan oleh pihak ketiga untuk melacak perilaku pengguna secara online tanpa izin mereka. Ini dapat mempengaruhi privasi pengguna dan menciptakan masalah keamanan.

2. Cookies yang tidak dienkripsi atau tidak diatur dengan baik dapat rentan terhadap serangan pencurian data. 

3. Cookies dapat menjadi sasaran *web application threats* seperti *Cross-Site Scripting* (XSS) dan *Cross Site Request Forgery* (CRSF) jika tidak dielola dengan benar. Developer harus memvalidasi data yang disimpan dalam cookies dan menghindari penyimpanan data sensitif di sana.

## Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. 
### **Membuat Fungsi dan Form Registrasi**
1. Jalankan virtual environment dengan menggunakan perintah `env\Scripts\activate.bat`
2. Tambahkan `import redirect`, `UserCreationForm`, dan `messages` pada bagian paling atas
    ```python
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages  
    ```
3. Buka `views.py` pada subdirektori `main` dan buatlah fungsi dengan nama `register` yang menerima parameter `request`. Isi fungsi tersebut dengan kode berikut
    ```python
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
4. Buatl berkas HTML baru dengan nama `register.html` pada folder `main/templates`. Isi dari `register.html`. Isi file tersebut dengan kode berikut
    ```html
    <!-- Sesuaikan dengan kebutuhan -->
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Register</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
    ```
5. Buka `urls.py` yang ada pada subdirektori `main` dan impor fungsi yang sudah dibuat tadi.
    ```python
    from main.views import register
    ```
6. Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('register/', register, name='register'),
    ...
    ```
### Membuat Fungsi Login
1. Buka `views.py` yang ada pada subdirektori `main` dan buatlah fungsi dengan nama `login_user` yang menerima parameter `request`.

2. Tambahkan `import authenticate` dan `login` pada bagian paling atas.
    ```python
    from django.contrib.auth import authenticate, login
    ```
3. Tambahkan kode di bawah ini ke dalam fungsi login yang sudah kamu buat sebelumnya.
    ```python
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```
4. Buatlah berkas HTML baru dengan nama `login.html` pada folder `main/templates`. Isi `login.html` dapat dengan template berikut.
    ```html
    <!-- Sesuaikan dengan kebutuhan -->
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %}
    ```
5. Buka `urls.py` yang ada pada subdirektori `main` dan impor fungsi yang sudah kamu buat tadi.
    ```python
    from main.views import login_user
    ```
6. Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('login/', login_user, name='login'),
    ...
    ```
### **Membuat Fungsi Logout**
1. Buka `views.py` yang ada pada subdirektori `main` dan buatlah fungsi dengan nama `logout_user` yang menerima parameter `request`.

2. Tambahkan import logout pada bagian paling atas.
    ```python
    from django.contrib.auth import logout
    ```

3. Tambahkan potongan kode di bawah ini ke dalam fungsi logout yang sudah kamu buat sebelumnya.
    ```python
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

4.  Bukalah berkas` main.html` yang ada pada folder `main/templates`. Tambahkan potongan kode di bawah ini setelah hyperlink tag untuk `Add New Product` pada berkas `main.html`
    ```html
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
5. Buka `urls.py` yang ada pada subdirektori main dan impor fungsi yang sudah dibuat tadi.
    ```python
    from main.views import logout_user
    ```

6. Tambahkan path url ke dalam `urlpatterns` untuk 
mengakses fungsi yang sudah diimpor tadi.
    ```python
    ...
    path('logout/', logout_user, name='logout'),
    ...
    ```
### **Merestriksi Akses Halaman Main**
1. Buka views.py yang ada pada subdirektori main dan tambahkan `import login_required` pada bagian paling atas.
    ```python
    from django.contrib.auth.decorators import login_required
    ```

2. Tambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
    ```python
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ```
### **Menggunakan Data Dari Cookies**
1. Lakukan `logout` jika sedang menjalankan aplikasi Django-mu.

2. Buka `views.py` yang ada pada subdirektori main dan tambahkan `import HttpResponseRedirect`, `reverse`, dan `datetime` pada bagian paling atas.
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
3. Pada fungsi `login_user`, tambahkan fungsi untuk menambahkan `cookie` yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan login. Ganti kode yang ada pada blok `if user is not None` menjadi potongan kode berikut.
    ```python
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
4. Pada fungsi show_main, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`. Berikut contoh kode yang sudah diubah.
    ```python
    context = {
        'name': 'Audric', #Sesuaikan dengan kebutuhan
        'class': 'PBP C', #Sesuaikan dengan kebutuhan
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }
    ```
5. Ubah fungsi `logout_user` menjadi seperti potongan kode berikut.
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
6. Buka berkas main.html dan tambahkan potongan kode berikut di antara tabel dan tombol logout untuk menampilkan data last login.
    ```html
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

7. Refresh halaman login (atau jalankan proyek Django-mu dengan perintah `python manage.py runserver` jika belum menjalankan proyekmu) dan login. Data `last login` akan muncul di halaman `main`
 
## Menghubungkan model Item dengan User. 
1. Buka `models.py `yang ada pada subdirektori `main` dan tambahkan kode berikut pada dibawah kode untuk mengimpor model:
    ```python
    ...
    from django.contrib.auth.models import User
    ...
    ```

2. Pada model `Item` yang sudah dibuat, tambahkan potongan kode berikut:
    ```python
    class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
3. Buka `views.py` yang ada pada subdirektori `main`, dan ubah potongan kode pada fungsi `create_product` menjadi sebagai berikut:
    ```python
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```
4. Ubah fungsi `show_main` menjadi sebagai berikut.
    ```python
    def show_main(request):
        products = Item.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
        ...
    ...
    ```
5. Simpan semua perubahan, dan lakukan migrasi model dengan `python manage.py makemigrations`.

6. Pilih `1` untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data.

7. Ketik angka `1` lagi untuk menetapkan *user* dengan `ID 1` (yang sudah kita buat sebelumnya) pada model yang sudah ada.

8. Lakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.

# **Tugas 5**
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
### **Element Selector**
Element selector digunakan untuk memilih elemen berdasarkan nama elemen tertentu. Ini akan memengaruhi semua elemen teks paragraf pada halaman web sehingga cocok ingin mengubah gaya semua teks paragraf secara seragam. Contoh:
```css
p {
  text-align: center;
  color: red;
}
```

### **ID Selector**
 ID selector digunakan untuk memilih elemen dengan ID tertentu. ID harus unik dalam satu halaman sehingga cocok digunakan untuk mengidentifikasi elemen tertentu. Contoh:
 ```css
#para1 {
  text-align: center;
  color: red;
}
```

### **Class Selector**
Menggunakan class selector memungkinkan kita untuk mengganti gaya elemen dengan class tertentu. Ini  berguna saat ingin menerapkan gaya yang sama pada beberapa elemen, tetapi tidak semua elemen dengan tag yang sama. Contoh:
```css
.center {
  text-align: center;
  color: red;
}
```
### **Universal Selector**
Universal selector akan mempengaruhi semua elemen pada halaman. DIgunakan jika ingin mengubah semua elemen pada halaman dengan gaya yang seragam. Contoh:
```css
* {
  text-align: center;
  color: blue;
}
```
### **Grouping Selector**
Grouping selector digunakan untuk mengubah gaya elemen yang berbeda-beda. Kita bisa mendefinisikan gaya elemen yang berbeda-beda tersebut ke dalam satu grup.
```css
h1, h2, p {
  text-align: center;
  color: red;
}
```
## Jelaskan HTML5 Tag yang kamu ketahui.
- `<table>`   : Membuat suatu tabel
- `<tbody>`   : Membuat badan tabel
- `<td>`      : Membuat *cell* tabel
- `<thead>`   : Membuat header tabel
- `<tr>`      : Membuat baris tabel
- `<header>`    : Memmbuat header
- `<h1> - <h6>`  : Membuat header 1 sampai 6
- `<p>`   : Membuat paragraf
- `<div>` :	Menentukan bagian dalam halaman
- `<body>`:	Menentukan badan suatu elemen
- `<style>`: Spesifikasi gaya suatu elemen
- `<title>`: Menentukan judul
- `<html>`	: Spesifikasi dokumen HTML

## Jelaskan perbedaan antara margin dan padding
### Margin
Margin adalah ruang di sekitar suatu elemen. Margin digunakan untuk memindahkan elemen ke atas atau ke bawah pada halaman serta ke kiri atau ke kanan. Margin sepenuhnya transparan dan tidak memiliki warna latar belakang apa pun. Ini membersihkan area di sekitar elemen. Setiap sisi elemen memiliki ukuran margin yang dapat diubah satu per satu. Dalam menciptakan celah, margin mendorong elemen-elemen yang berdekatan menjauh.

### Padding
Padding adalah ruang antara elemen dan konten terkait di dalamnya. Ini menentukan bagaimana elemen terlihat dan ditempatkan di dalam wadah. Ini juga menunjukkan latar belakang wadah di sekitar elemen di dalamnya. Padding dapat dipengaruhi oleh warna latar belakang karena membersihkan area di sekitar konten. Untuk menciptakan celah, itu akan memperbesar ukuran elemen atau memperkecil konten di dalamnya. Secara default, ukuran elemen bertambah.

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
### Bootstrap
Bootstrap adalah framework CSS yang sudah lama ada dan mencakup berbagai komponen UI siap pakai, grid system, dan gaya bawaan yang memudahkan desain web responsif. Ini cocok untuk pengembang yang ingin cepat membangun situs dengan komponen siap pakai.

### Tailwind CSS
Tailwind adalah framework CSS yang memfokuskan pada utilitas. Ini tidak menyediakan komponen UI siap pakai, tetapi memungkinkan untuk membangun tampilan dengan menentukan gaya melalui kelas-kelas utilitas di HTML. Ini cocok untuk pengembang yang ingin lebih kontrol dalam desain tampilan mereka.

Kapan sebaiknya digunakan tergantung pada preferensi dan kebutuhan. Bootstrap cocok jika ingin menghemat waktu dengan komponen UI siap pakai. Tailwind cocok jika ingin lebih fleksibel dalam mendefinisikan gaya sendiri.

## Kustomisasi *design* pada template HTML
1. Mendefinisikan style CSS sesuai dengan kebutuhan pada `base.html`. Style ini akan digunakan untuk mengubah tampilan di 
    ```css
        <style type="text/css">
            /* Your common CSS styles here */
            ....
            .container {
                text-align: center;
                margin-top: 40px;
                margin-bottom: 50px;
            }
            .heading {
                margin-top: 40px;
                font-size: 100px;
                font-family: "Impact";
                margin-bottom: -15px;
            }
            .content {
                font-size: 19px;
                font-family: "Courier New";
                font-weight: bold;
            }
            .... 
            /* other style goes here */
        <style>
    ```
2. Implementasi style CSS yang sudah dibuat di `base.html` pada `register.html`, `login.html`, `create_product.html`, `main.html`, dan `delete_product.html`.
3. Jalankan virtual environment dengan `env\Scripts\activate.bat`, nyalakan server `python manage.py runserver`, dan buka http://localhost:8000 untuk melihat hasilnya dan lakukan pembenaran dan penyesuaian.

# **Tugas 6**
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
### Asynchronous
 Kode dirancang agar dapat tugas dapat berjalan bersamaan. Saat tugas yang memakan waktu sedang berjalan, program dapat menjalankan tugas lain tanpa harus menunggu. Program adalah *multi-thread*, yang berarti program dapat berjalan parallel. Selain itu *asynchronous programming* itu *non-blocking*, yang berarti mereka akan mengirim banyak *request* ke server

 ### Synchronous
 Kode dijalankan satu per satu, dan program harus menunggu tugas sebelum melanjutkan ke tugas berikutnya. Ini bisa menjadi lambat jika ada tugas yang memakan waktu. Program adalah *single-thread*, yang berarti program hanya menjalankan satu operasi. Selain itu *synchronous programming* itu *blocking*, yang berarti mereka hanya mengirim satu *request* ke server dan menunggu *request* tersebut terjawab oleh server

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma pemrograman berbasis peristiwa adalah cara pemrograman di mana program merespons peristiwa yang terjadi, seperti tindakan pengguna, input, atau perubahan lainnya. Program akan menunggu dan bereaksi terhadap peristiwa yang terjadi. Paradigma ini dapat digunakan sebagian dalam program, hanya untuk fungsi atau operasi tertentu yang akan dijalankan saat peristiwa terjadi.

Contoh penerapan pemrograman berbasis peristiwa dalam program adalah ketika pengguna menekan tombol `Request Album` pada main page web Setelah menekan tombol tersebut,  web akan menampilkan *pop-up* yang terdapat sebuah "form" untuk mengisi detail album yang ingin diminta. Setelah hal tersebut diisi, dan tombol `Request Album` (di dalam *pop-up*) ditekan, sebuah objek XMLHttpRequest akan dibuat oleh JavaScript dan akan mengirimkan permintaan ke server. Server akan memproses permintaan tersebut dan menjawab respons kembali ke web dan dibaca JavaScript. Terakhir, web akan diperbarui berdasarkan respons dan menampilkan item baru yang diterima.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX mengacu pada kemampuan untuk melakukan operasi tanpa harus menunggu hasilnya secara langsung, sehingga program dapat menjalankan tugas lain tanpa terblokir oleh operasi yang sedang berlangsung. Ini sangat berguna dalam kasus seperti permintaan HTTP atau pengambilan data dari server, di mana waktu yang diperlukan untuk mengambil data dapat bervariasi Dalam AJAX, asynchronous programming memungkinkan JavaScript untuk melakukan permintaan ke server dan menerima respons dari server tanpa menghentikan eksekusi program utama atau halaman web.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
### Fetch API
- Fetch API adalah bagian dari JavaScript yang sudah terintegrasi dalam browser. Ini berarti tidak perlu mengunduh atau mengimpor pustaka tambahan seperti jQuery untuk menggunakannya.
- Fetch API lebih ringan dalam hal ukuran dan kinerja dibandingkan dengan jQuery. Hal ini cocok untuk mengembangkan aplikasi web yang memerlukan efisiensi dan kecepatan.
- Fetch API mengembalikan objek `Promise`, yang membuat pengelolaan *asynchronous* code menjadi lebih mudah dibaca dan dimengerti.

### jQuery
- jQuery mendukung *browser* yang lebih lama dan baru, sehingga cocok dengan beragam jenis *browser*
- jQuery memiliki *plugin* yang sangat besar dan kuat yang dapat digunakan untuk menambahkan berbagai fitur dan fungsi ke situs web dengan mudah
- Terdapat jQuery UI yang menyediakan komponen antarmuka pengguna yang siap pakai sehingga mempercepat pengembangan antarmuka pengguna.

### Pendapat
Saya cenderung lebih suka menggunakan Fetch API. Fetch API lebih modern, ringan, dan merupakan standar yang direkomendasikan. Ini adalah pilihan yang baik untuk proyek-proyek baru dan ingin fokus pada pengembangan dengan JavaScript. Selain itu, dengan AJAX dalam memproses request *asynchronous* dapat lebih mudah diproses di dalam Fetch API.

## JavaScript dan Asynchronous JavaScript
### Membuat Fungsi untuk Mengembalikan Data JSON
1. Buat fungsi baru pada `views.py` dengan nama `get_product_json` yang menerima parameter `request`
    ```python
    def get_product_json(request):
        product_item = Item.objects.filter(user = request.user) #Filter product berdasarkan user
        return HttpResponse(serializers.serialize('json', product_item))
    ```
2. Buka `urls.py` dan impor fungsi `get_product_json` Tambahkan routing untuk fungsi dengan memasukkan *path url* ke `urlpatterns`.
    ```python
    ...
    path('get-product/', get_product_json, name='get_product_json'),
    ...
    ```

### Membuat Fungsi untuk Menambahkan Produk dengan AJAX
1. Buat fungsi baru pada `views.py` dengan nama `add_product_ajax` yang menerima parameter `request`.

2. Impor `from django.views.decorators.csrf import csrf_exempt` pada berkas `views.py`.

3. Tambahkan dekorator `@csrf_exempt` di atas fungsi `add_product_ajax`
    ```python
    @csrf_exempt
    def add_product_ajax(request):
        if request.method == 'POST':
            album = request.POST.get("album")
            year = request.POST.get("year")
            artist = request.POST.get("artist")
            amount = request.POST.get("amount")
            user = request.user

            new_product = Item(album=album, year=year, artist=artist, amount=amount, user=user)
            new_product.save()

            return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
    ```
4. Buka `urls.py` dan impor fungsi `add_product_ajax` Tambahkan routing untuk fungsi dengan memasukkan *path url* ke `urlpatterns`.
    ```python
    ...
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
    ...
    ```
### Menampilkan Data Product dengan Fetch() API
1. Buka berkas `main.html` pada `main/templates` dan **hapuslah** bagian kode tabel yang menampilan product yang sudah ditambahkan. Gantilah kode table tersebut dengan kode berikut sebagai structure table.
    ```html
    <table id="product_table"></table>
    ```
2. Buatlah block `<Script>` di bagian bawah berkas dan buatlah fungsi baru pada block `Script>` tersebut dengan nama `getProducts()`. Setelah itu, Buatlah fungsi baru pada block `<Script>` dengan nama `refreshProducts()` yang digunakan untuk me-*refresh* data produk secara *asynchronous*.


    ```html
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }

        async function refreshProducts() {
            document.getElementById("product_table").innerHTML = ""
            const products = await getProducts()
            let htmlString = `<tr>
                <th>No.</th>
                <th>Album</th>
                <th>Year</th>
                <th>Artist</th>
                <th>Amount</th>
                <th>Edit</th>
                <th>Date Requested</th>
                <th>Remove</th>
            </tr>`
            products.forEach((item, index, array) => {
                const isLastRow = index === array.length - 1;
                const rowClass = isLastRow ? "last-item" : "";
                htmlString += `\n<tr class="${rowClass}">
                <td >${index + 1}</td>
                <td>${item.fields.album}</td>
                <td>${item.fields.year}</td>
                <td>${item.fields.artist}</td>
                <td>${item.fields.amount}</td>
                <td>
                <form method="POST" action="increment-amount/${item.pk}/">
                    {% csrf_token %}
                    <button class="buttonincdec" type="submit">+</button>
                </form>
                <form method="POST" action="decrement-amount/${item.pk}/">
                    {% csrf_token %}
                    <button class="buttonincdec" type="submit">-</button>
                </form>
                </td>
                <td>${item.fields.date_added}</td>
                <td>
                    <a href="delete-product/${item.pk}">
                        <button>
                            Remove
                        </button>
                    </a>
                </td>
            </tr>` 
            })
            document.getElementById("product_table").innerHTML = htmlString
        }
        refreshProducts()
    </script>
    ```
### Membuat Modal Sebagai Form untuk Menambahkan Produk
1. Jika belum menambahkan Bootstrap CSS dan JS, buka file `base.html` pada folder `templates` di root project. Tambahkan kode berikut.
    #### Bootstrap CSS
    ```html
    <head>
        {% block meta %}
            ...
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    ```

    #### JS
    ```html
    <head>
        ...
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    </head>
    ```

2. Pada `main.html` di `main/templates`, tambahkan kode ini di atas untuk mengimplementasikan modal Bootstrap yang akan menampilkan form.
    ```html
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Request Album</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="album" class="col-form-label">Album:</label>
                            <input type="text" class="form-control" id="album" name="album">
                        </div>
                        <div class="mb-3">
                            <label for="year" class="col-form-label">Year:</label>
                            <input type="number" class="form-control" id="year" name="year">
                        </div>
                        <div class="mb-3">
                            <label for="artist" class="col-form-label">Artist:</label>
                            <input type="text" class="form-control" id="artist" name="artist">
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Request Album</button>
                </div>
            </div>
        </div>
    </div>
    ```
3. Tambahkan button yang berfungsi untuk menampilkan modal.
    ```html
     <a>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" style="margin-bottom: 40px;">Request Album</button>
    </a>
    ```

### Menambahkan Data Product dengan AJAX
1. Buatlah fungsi baru pada block `<Script>` dengan nama `addProduct()`. Isilah fungsi tersebut dengan kode berikut.
    ```html
    <script>
        ...
        function addProduct() {
            fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)

            document.getElementById("form").reset()
            return false
        }
    </script>
    ```

2. Tambahkan fungsi *onclick* pada button `"Request Album"` pada modal untuk menjalankan fungsi `addProduct()` dengan menambahkan kode berikut.
    ```html
    <script>
        ...
        document.getElementById("button_add").onclick = addProduct
    </script>
    ```