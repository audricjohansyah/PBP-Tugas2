Nama    : Alexander Audric Johansyah <br>
NPM     : 2206815466 <br>
Kelas   : PBP <br>

Link Tugas:<br>
[Tugas 2](#tugas-2) <br>
[Tugas 3](#tugas-3)

# **Tugas 2**
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
![Bagan](https://raw.githubusercontent.com/audricjohansyah/PBP-Tugas2/9bed03bb2113695a9b8b6997de87d1a0d00a1eed/Bagan%20PBP.jpg)

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

# **Tugas 3**
# Apa perbedaan antara form POST dan form GET dalam Django?
POST biasanya digunakan untuk mengirim data yang akan membuat perubahan di sisi server seperti untuk membuat atau menulis ulang sumber daya/data tertentu. POST biasa digunakan untuk mengirim data yang sensitif seperti password, data tersebut disembunyikan dari URL. Data yang dikirim ke server ini disimpan di badan permintaan permintaan HTTP. Maka dari itu, POST lebih aman daripada GET karena data tidak tampil di URL berarti data sensitif tidak akan tampil secara terbuka.

GET biasanya digunakan di sisi klien (Browser) untuk mengirim permintaan ke server tertentu untuk mendapatkan data atau sumber daya tertentu. GET digunakan untuk permintaan pencarian yang tidak mengubah apapun. GET mengirim data sebagai parameter yang terlihat di URL dan data tersebut terbatas ukurannya. GET digunakan untuk data yang kurang aman karena terlihat di URL dan dapat diakses oleh pihak ketiga

*Source*: https://www.geeksforgeeks.org/difference-between-http-get-and-post-methods/

# Perbedaan Utama Antara XML, JSON, dan HTML Dalam Konteks Pengiriman Data
- ## JSON (*JavaScript Object Notation*)<br>
    JSON didesain menjadi *self-describing*, sehingga mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat di bahasa pemrograman.
    Data pada JSON disimpan dalam bentuk key dan value. Value dapat berupa tipe data primitif (string, number, boolean) ataupun berupa objek. JSON biasa yang digunakan untuk pertukaran data antara aplikasi.

- ## XML (*Extensible Markup Language*)<br>
    XML didesain menjadi *self-descriptive*, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML hanya berisi informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. Dokumen XML membentuk  data dalam struktur tree dengan namespace untuk kategori data yeng berbeda. Hanya dapat di-*parsed* menggunakan pengurai XML Mendukung semua tipe data JSON, Boolean, tanggal, gambar, dan namespace. XML sering digunakan untuk pertukaran data yang terstruktur antara aplikasi.
- ## HTML (*HyperText Markup Language*)<br>
    HTML adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web. HTML fokus pada representasi visual dan interaksi pengguna pada halaman web.

Kesimpulan, XML digunakan untuk mendefinisikan struktur data, JSON digunakan untuk pertukaran data, dan HTML digunakan untuk mengatur tampilan dan interaksi pada halaman web.

# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Sintaks yang digunakan JSON mudah untuk ditulis dan dibaca oleh manusia
- Sintaks merupakan turunan dari Object JavaScript yang membuat JSON banyak digunakan di aplikasi web dan mobile.
- JSON didesain menyediakan format yang sederhana serta ringkas dan data pada JSON disimpan dalam bentuk key dan value.
- JSON dapat diurai menggunakan fungsi JavaScript standar yang merupakan bahasa pemrograman yang umum digunakan dalam pengembangan aplikasi web. 
- Perbedaan syntax dan ukuran file JSON juga membuat *parsing* JSON lebih cepat dibandingkan XML.
- JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat.
- Penguraian JSON lebih aman dibandingkan XML. Struktur XML rentan *unauthorized modification* dan deklarasi tipe dokumen eksternal yang tidak terstruktur.

# Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Buat berkas baru pada direktori main dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data produk baru. Tambahkan kode berikut ke dalam berkas `forms.py`.
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["album", "year", "artist"]
    ```
2. Buka berkas `views.py` yang ada pada folder main dan tambahkan beberapa import berikut pada bagian paling atas.
    ```python
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    ```
3. Buat fungsi baru dengan nama `create_product` pada berkas tersebut yang menerima parameter request dan tambahkan potongan kode di bawah ini untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form.
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
    def show_main(request):
        items = Item.objects.all() #Tambahkan ini

        context = {
            ....
            'items': items #Tambahkan ini
            ....
        }

        return render(request, "main.html", context)
    ```
5. Buka `urls.py` yang ada pada folder main dan import fungsi `create_product` yang sudah kamu buat tadi.
    ```python
    from main.views import show_main, create_product
    ```
6. Tambahkan path url ke dalam urlpatterns pada `urls.py` di main untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.
    ```python
    path('create-product', create_product, name='create_product'),
    ```
7. Buat berkas HTML baru dengan nama `create_product.html` pada direktori `main/templates`. Isi `create_product.html` dengan kode berikut.
    ```python
    #Ubah sesuai kebutuhan
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
8. Buka `main.html` dan tambahkan kode berikut di dalam `{% block content %}` untuk menampilkan data produk dalam bentuk table serta tombol `"Request Album"` yang akan redirect ke halaman form.
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
# Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
## Mengembalikan Data dalam Bentuk XML
1. Buka `views.py` yang ada pada folder main dan tambahkan import `HttpResponse` dan `Serializer` pada bagian paling atas.
    ```python
    from django.http import HttpResponse
    from django.core import serializers
    ```
2. Buatlah sebuah fungsi yang menerima parameter request dengan nama `show_xml` dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada `Item`. Tambahkan return function berupa *HttpResponse* yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`.
    ```python
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
        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")show_xml 
        ```
    - JSON
        ```python
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

# Screenshot hasil akses URL pada Postman dan HTML
## HTML View
![HTML View](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/HTML%20View.jpg?raw=true)
## JSON View
![JSON View](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/JSON%20View.jpg?raw=true)
## XML View
![XML View](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/XML%20View.jpg?raw=true)

## JSON View by ID
![JSON View by ID](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/JSON%20View%20by%20ID.jpg?raw=true)

## XML View by ID
![XML View by ID](https://github.com/audricjohansyah/PBP-Tugas2/blob/b8c758a8a8bce5e11a10fbc72f911f73dcdd721f/Images/XML%20View%20by%20ID.jpg?raw=true)



