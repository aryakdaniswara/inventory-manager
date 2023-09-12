# inventory-manager

### Membuat sebuah proyek Django baru
<details>
<summary> Membuat proyek Django baru </summary>
  
1. Buat sebuah direktori (_folder_) baru di tempat yang ada inginkan dengan nama `inventory_manager`
2. Klik kanan pada folder yang telah Anda buat dan pilih `Copy as path`
3. Tekan Win + X dan pilih 'Terminal (Admin)'
4. Pada Terminal ketik 'cd' dan tekan Ctrl + V untuk _paste_ alamat dari direktori yang sudah kita buat. Tampilan dari kode Anda harusnya terlihat sepeti ini:
```
cd "C:\Users\direktoriAnda\inventory_manager"
```
- Tekan enter untuk pindah ke direktori `inventory_manager` pada Terminal.
5. Buat virtual environment baru dengan perintah berikut
```
 python -m venv env
```
6. Aktivasi virtual environment dengan perintah berikut
```
 env\Scripts\activate.bat
```
<p align="center"> atau </p>

```
 env\Scripts\activate
```
- Jika virtual environment sudah menyala akan ditandai dengan `(env)` pada Terminal
7. Dalam direktori yang sama buat sebuah file `requirements.txt` yang berisi dependencies:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
8. Pastikan virtual environment menyala dan install dependencies dengan perintah berikut:
  ```
    pip install -r requirements.txt
  ```
9. Buat proyek Django baru dengan nama `inventory_manager` dengan perintah berikut:
  ```
    django-admin startproject invenetory .
  ```
10. Tambahkan `*` ke `ALLOWED_HOST` di `settings.py` untuk keperluan deployment dengan perintah berikut
 ```
 ...
 ALLOWED_HOSTS = ["*"]
 ...

 ```
</details>
<details>
<summary> Memeriksa proyek Django yang sudah dibuat </summary>

1. Jalankan server untuk mengecek apakah proyek Django sudah berjalan. 
```
python manage.py runserver
```
2. Buka `http://localhost:8000` di peramban Anda. Jika ada animasi roket maka proyek Django Anda sudah berjalan.

</details>

---
### Membuat aplikasi dengan nama main pada proyek tersebut.
<details>
<summary> Membuat aplikasi main pada proyek Anda </summary>
  
  1. Buka terminal di direktori proyek Django Anda dan jalakan virtual environment
  
  ```
  cd "C:\Users\direktoriAnda\inventory_manager"
  env\Scripts\activate.bat
  ```

2. Buat aplikasi main dengan perintah berikut.
  ```
  python manage.py startapp main
  ```
3. Tambahkan aplikasi main ke INSTALLED_APPS di settings.py inventory_manager agar aplikasi tersebut dapat diakses

```python
INSTALLED_APPS = [
...,
'main',
...
]    
```
</details>
<details>
<summary> Membuat templates dan mengisinya </summary>
  
1. Buat direktori baru bernama `templates` pada direktori `main`
2. Buat sebuah file baru bernama `main.html` yang berisi
  
```
<h1>Inventory Manager 00</h1>

<h5>Nama: </h5>
<p>{{ myName }}<p>
<h5>Kelas: </h5>
<p>{{ class }}<p>
<h5>Nama Aplikasi: </h5>
<p>{{ appName }}<p>

<h5>Nama Produk: </h5>
<p>{{ name }}<p>
<h5>Jumlah: </h5>
<p>{{ amount }}<p>
<h5>Deskripsi: </h5>
<p>{{ description }}<p>
```

- Sesuaikan isi `main.html` dengan preferensi Anda
</details>

---
### Melakukan routing agar aplikasi main dapat berjalan dan terpetakan.
<details>
<summary> Konfigurasi untuk menjalankan aplikasi main </summary>

1. Buat file baru bernama `urls.py` pada direktori `main`
```
from django.urls import path #Definisi pola URL
from main.views import show_main #Fungsi dari views.py untuk tampilan

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Buka direktori `inventory_manager` dan cari file `urls.py` (berbeda dari file di direktori `main`)
3. Tambahkan fungsi `include` dengan perintah
```
...
from django.urls import path, include 
...
```

4. Tambahkan rute url yang akan mengarahkan tampilan ke `main `
```
urlpatterns = [
...
path('main/', include('main.urls')),
...
]
```
</details>

---
### Membuat model pada aplikasi main dan migrasi
<details>
<summary> Konfigurasi model pada aplikasi </summary>

1. Buat model dengan cara membuka direktori aplikasi main di `models.py`
```
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField(default=0)
```

2. Lakukan migrasi agar perubahan model dapat tersimpan
```
python manage.py makemigrations
python manage.py migrate
```
</details>

---
### Membuat fungsi pada views.py
<details>
<summary> Konfigurasi views.py</summary>

1. Buka file `views.py` di direktori `main` dan tambahkan kode beikut
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'myName' : 'Arya Kusuma Daniswara',
        'class' : 'PBP B',
        'appName' : 'inventory00',
        'name': 'Botol',
        'amount': '2',
        'description' : 'Botol 500 ml yang sangat bagus'
    }

    return render(request, "main.html", context)
```
- File `views.py` akan melengkapi template `main.html` yang sudah dibuat
</details>

---
### Melakukan deployment ke Adaptable 
<details>
<summary> Konfigurasi Github</summary>

1. Buat repositori baru dengan nama `inventory_manager`
2. Tambahkan file `.gitignore`
 ```
  # Django
  *.log
  *.pot
  *.pyc
  __pycache__
  db.sqlite3
  media

  # Backup files
  *.bak 

  # If you are using PyCharm
  # User-specific stuff
  .idea/**/workspace.xml
  .idea/**/tasks.xml
  .idea/**/usage.statistics.xml
  .idea/**/dictionaries
  .idea/**/shelf

  # AWS User-specific
  .idea/**/aws.xml

  # Generated files
  .idea/**/contentModel.xml

  # Sensitive or high-churn files
  .idea/**/dataSources/
  .idea/**/dataSources.ids
  .idea/**/dataSources.local.xml
  .idea/**/sqlDataSources.xml
  .idea/**/dynamic.xml
  .idea/**/uiDesigner.xml
  .idea/**/dbnavigator.xml

  # Gradle
  .idea/**/gradle.xml
  .idea/**/libraries

  # File-based project format
  *.iws

  # IntelliJ
  out/

  # JIRA plugin
  atlassian-ide-plugin.xml

  # Python
  *.py[cod] 
  *$py.class 

  # Distribution / packaging 
  .Python build/ 
  develop-eggs/ 
  dist/ 
  downloads/ 
  eggs/ 
  .eggs/ 
  lib/ 
  lib64/ 
  parts/ 
  sdist/ 
  var/ 
  wheels/ 
  *.egg-info/ 
  .installed.cfg 
  *.egg 
  *.manifest 
  *.spec 

  # Installer logs 
  pip-log.txt 
  pip-delete-this-directory.txt 

  # Unit test / coverage reports 
  htmlcov/ 
  .tox/ 
  .coverage 
  .coverage.* 
  .cache 
  .pytest_cache/ 
  nosetests.xml 
  coverage.xml 
  *.cover 
  .hypothesis/ 

  # Jupyter Notebook 
  .ipynb_checkpoints 

  # pyenv 
  .python-version 

  # celery 
  celerybeat-schedule.* 

  # SageMath parsed files 
  *.sage.py 

  # Environments 
  .env 
  .venv 
  env/ 
  venv/ 
  ENV/ 
  env.bak/ 
  venv.bak/ 

  # mkdocs documentation 
  /site 

  # mypy 
  .mypy_cache/ 

  # Sublime Text
  *.tmlanguage.cache 
  *.tmPreferences.cache 
  *.stTheme.cache 
  *.sublime-workspace 
  *.sublime-project 

  # sftp configuration file 
  sftp-config.json 

  # Package control specific files Package 
  Control.last-run 
  Control.ca-list 
  Control.ca-bundle 
  Control.system-ca-bundle 
  GitHub.sublime-settings 

  # Visual Studio Code
  .vscode/* 
  !.vscode/settings.json 
  !.vscode/tasks.json 
  !.vscode/launch.json 
  !.vscode/extensions.json 
  .history
  ```

3. Inisiasi git directory, tambahkan perubahan, _push_, dan _commit_
    ```
    git init
    git remote add origin https://github.com/aryakdaniswara/inventory_manager.git
    git branch -M main
    git add .
    git commit -m "<pesan>"
    git push origin main

    ```
</details>
<details>
<summary> Membuat test unit </summary>

1. Buat test unit dengan membuka file `tests.py` di direktori main
```
  from django.test import TestCase, Client

  class mainTest(TestCase):
      def test_main_url_is_exist(self):
          response = Client().get('/main/')
          self.assertEqual(response.status_code, 200)

      def test_main_using_main_template(self):
          response = Client().get('/main/')
          self.assertTemplateUsed(response, 'main.html')
  ```
2. Jalankan tes dengan perintah
  ```
  python manage.py test
  ```
</details>
<details>
<summary> Konfigurasi Adaptable </summary>

1. Buka situs https://adaptable.io/ dan login menggunakan github Anda
2. Klik `New app` dan pilih `Connect an Existing Repository`
3. Pilih repositori github `inventotry_manager` yang telah Anda buat
4. Pilih branch `main`
5. Pilih `python app template`
6. Pilih `PostgeSQL`
7. Pilih versi python yang Anda gunakan misal `3.11`
8. Isi start command dengan `start command sebagai berikut `python manage.py migrate && gunicorn inventory_manager.wsgi`
9. Pilih nama domain yang Anda inginkan
10. Centang `HTTP Listener Port
</details>

---








