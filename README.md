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
atau langsung download dan extract zip

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
Program dapat dijalankan dengan enter command berikut di terminal.
```
$ python bolzano.py
```

## Contoh Penggunaan
Misalkan kita ingin mendapatkan akar persamaan dari fungsi
<code>f(x) = e<sup>x</sup> - x<sup>2</sup></code>
maka kita membuat grafiknya terlebih dahulu. Menggunakan `desmos.com` didapatkan grafik seperti berikut.\
![image](https://user-images.githubusercontent.com/115603634/197846013-122fd048-33c4-42f8-bdd9-b8c528410442.png)\
Jika diobservasi, akar persamaan terletak di antara `-1` dan `0`.\
\
Lanjut ke program, dalam fungsi `f(x)` di file bolzano.py line 111 diganti menjadi
```py
def f(x):
    return math.e**x - x**2
```

