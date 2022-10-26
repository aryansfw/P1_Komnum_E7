# Praktikum Komputasi Numerik Kelompok 7: Metode Bolzano
Anggota:
- Muhammad Daffa Harits (5025211005)
- Aryan Shafa Wardana (5025211031)
- Syukra Wahyu Ramadhan (5025211037)

![image](https://user-images.githubusercontent.com/115603634/197460774-b755e92e-b548-42ca-b650-effcdf6cb9a5.png)

## Cara Menggunakan
#### Clone
Clone repo ini ke directory tujuan menggunakan
```
$ git clone https://github.com/yannnshafaw/P1_Komnum_E7.git
```
atau langsung download dan extract zip.

#### Library
Install library MatPlotLib dan NumPy menggunakan
```
$ pip install matplotlib numpy
```
#### Mengatur Fungsi
Dalam file `bolzano.py`, pada line 111, terdapat fungsi
```py
def f(x):
    return None
```
Fungsi tersebut dibiarkan jika ingin memasukkan fungsi menggunakan input program. Jika ingin menggunakan fungsi custom, ubah `return None` menjadi fungsi yang diinginkan. Contoh:
```py
def f(x):
    return x**2 + x + 1
```
Fungsi juga dapat menggunakan konstanta dan fungsi dari library seperti `math.e` dan `math.sin()`.

#### Menjalankan Program
Program dapat dijalankan dengan memasukkan command berikut ke dalam terminal.
```
$ python bolzano.py
```
Kemudian akan diminta input fungsi (jika `f(x) return None`), interval, dan banyaknya iterasi.
```
Input persamaan (Misal: x + 3x - 1 = 0 -> 1 3 -1):
Input interval (Misal: x1 = 0, x2 = 1 -> 0 1):
Input banyak iterasi:
```

## Contoh Penggunaan
#### Fungsi Input Program
Misalkan kita ingin mendapatkan akar persamaan dari fungsi
<code>f(x) = 6x<sup>2</sup> + 9x - 4</code>
maka kita membuat grafiknya terlebih dahulu. Menggunakan www.desmos.com, diperoleh grafik sebagai berikut. Dapat dilihat potongan fungsi dengan sumbu x adalah ketika nilai `x` berada di antara `-2` dan `-1` atau di antara `0` dan `1`.\
![image](https://user-images.githubusercontent.com/115603634/198007349-d673808e-9eef-4367-a09f-6af38bde4339.png)\
Untuk contoh ini akan digunakan interval `0` dan `1`.\
\
Dalam file bolzano.py line 111, fungsi `f(x)` dibiarkan `return None`.
```py
def f(x):
    return None
```
Selanjutnya, ketika program dijalankan, akan diminta input fungsi. Untuk kasus ini kita akan input `6 9 -   4`. Lalu akan diminta untuk input interval sehingga kita akan input `0 1` karena akar persamaan terletak pada interval `0` dan `1`. Terakhir, akan diminta input berapa iterasi, kita mencoba input `20` iterasi.
```
$ python bolzano.py
Input persamaan (Misal: x + 3x - 1 = 0 -> 1 3 -1): 6 9 -4
Input interval (Misal: x1 = 0, x2 = 1 -> 0 1): 0 1
Input banyak iterasi: 20
```
Jika di-enter lagi akan muncul sebagai berikut.\
![demo1](https://user-images.githubusercontent.com/115603634/198011247-ae0b59cd-0f73-4285-979d-5e72e8b6c131.gif)\
Pada setiap iterasi, nilai <code>x<sub>3</sub></code> akan semakin mendekati nilai akar persamaan. Semakin banyak iterasi maka semakin tinggi presisi nilai akar persamaan. Pada akhir semua iterasi, diperoleh `x = 0.35868`.

#### Fungsi Custom
Misalkan kita ingin mendapatkan akar persamaan dari fungsi
<code>f(x) = e<sup>x</sup> - x<sup>2</sup></code>
maka kita membuat grafiknya terlebih dahulu. Menggunakan www.desmos.com didapatkan grafik seperti berikut. Dapat dilihat bahwa potongan fungsi dengan sumbu x adalah ketika nilai `x` berada di antara `-1` dan `0`. \
![image](https://user-images.githubusercontent.com/115603634/197846013-122fd048-33c4-42f8-bdd9-b8c528410442.png)\
\
Lanjut ke program, dalam fungsi `f(x)` di file bolzano.py line 111 diganti menjadi
```py
def f(x):
    return math.e**x - x**2
```
Kemudian, ketika program dijalankan, akan diminta untuk memasukkan interval. Untuk kasus ini kita akan input `-1 0` karena akar persamaan berada di antara `-1` dan `0`. Selain itu akan diminta untuk memasukkan berapa iterasi, kita mencoba input `20` iterasi.
```
$ python bolzano.py
Input interval (Misal: x1 = 0, x2 = 1 -> 0 1): -1 0
Input banyak iterasi: 20
```
Kemudian jika di-enter lagi akan muncul seperti berikut.
![demo (1)](https://user-images.githubusercontent.com/115603634/198006634-3442bb08-5903-431c-935c-81b0b8c73464.gif)
Pada akhir iterasi, diperoleh `x = -0.70347`.

## Penjelasan Kode
Dalam file `bolzano.py` terdapat fungsi `__init__` untuk menetapkan variable-variable yang dibutuhkan untuk melakukan metode bolzano.
```py
def __init__(this, interval, iterasi, persamaan=None):
    this.persamaan = persamaan # Menyimpan persamaan hasil input (jika ada)
    this.interval = interval # Menyimpan list
    this.iterasi = iterasi
    this.useF = f(1)
    (this.x, this.x1, this.x2, this.x3, this.y, this.y1, this.y2) = this.setup()
    (this.fig, this.ax, this.curve, this.xl, this.xr, this.xl_point, this.xr_point) = this.init_plot()
```        
