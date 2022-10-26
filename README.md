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
Selanjutnya, ketika program dijalankan, akan diminta input fungsi. Untuk kasus ini kita akan input `6 9 -4`. Lalu akan diminta untuk input interval sehingga kita akan input `0 1` karena akar persamaan terletak pada interval `0` dan `1`. Terakhir, akan diminta input berapa iterasi, kita mencoba input `20` iterasi.
```
$ python bolzano.py
Input persamaan (Misal: x + 3x - 1 = 0 -> 1 3 -1): 6 9 -4
Input interval (Misal: x1 = 0, x2 = 1 -> 0 1): 0 1
Input banyak iterasi: 20
```
Jika di-enter lagi akan muncul sebagai berikut. (file gif mungkin lama untuk load)\ 
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
Kemudian jika di-enter lagi akan muncul seperti berikut. (file gif mungkin lama untuk load)
![demo (1)](https://user-images.githubusercontent.com/115603634/198006634-3442bb08-5903-431c-935c-81b0b8c73464.gif)
Pada akhir iterasi, diperoleh `x = -0.70347`.

## Penjelasan Kode
#### Class Bolzano
Dalam file `bolzano.py` terdapat `class Bolzano()`. Dalam class tersebut terdapat fungsi `__init__` untuk menetapkan variable-variable yang dibutuhkan untuk melakukan metode bolzano.
```py
def __init__(this, interval, iterasi, persamaan=None):
    this.persamaan = persamaan # Menyimpan persamaan hasil input (jika ada) dalam bentuk list
    this.interval = interval # Menyimpan interval dalam bentuk list [a, b]
    this.iterasi = iterasi # Menyimpan banyaknya iterasi
    this.useF = f(1) # Akan berisi None jika tidak menggunakan persamaan custom
    (this.x, this.x1, this.x2, this.x3, this.y, this.y1, this.y2) = this.setup() # Variabel-variabel untuk metode bolzano
    (this.fig, this.ax, this.curve, this.xl, this.xr, this.xl_point, this.xr_point) = this.init_plot() # Variabel-variabel untuk plotting grafik
```
Kemudian terdapat fungsi `calc_func` yang digunakan untuk menghitung y untuk grafik dan y<sub>1</sub>, y<sub>2</sub>, dan yx<sub>3</sub> untuk metode bolzano.
```py
def calc_func(this, x, x1, x2, x3):
    y = y1 = y2 = y3 = 0
    if this.useF: # Jika menggunakan fungsi custom
        y = f(x)
        y1 = f(x1)
        y2 = f(x2)
        y3 = f(x3)
    else: # Jika menggunakan fungsi input program
        n = len(this.persamaan)
        for i in range(0, n):
            coeff = this.persamaan[i]
            y += coeff * x**(n - i - 1)
            y1 += coeff * x1**(n - i - 1)
            y2 += coeff * x2**(n - i - 1)
            y3 += coeff * x3**(n - i - 1)

    return y, y1, y2, y3
```
Lalu terdapat fungsi `setup` untuk menginialisasikan variabel-variabel yang digunakan untuk metode bolzano.
```py
def setup(this):
    x1 = this.interval[0]
    x2 = this.interval[1]
    x3 = 1
    x = np.linspace(x1, x2) # Generasi nilai-nilai x yang digunakan untuk plotting grafik

    y, y1, y2, y3 = this.calc_func(x, x1, x2, x3)

    return x, x1, x2, x3, y, y1, y2
```

Kemudian untuk bagian plotting dan animasi grafik terdapat fungsi `step`, `init_plot`, `clear_plot`, dan `animate`. Plotting dan animasi grafik dijalankan dengan fungsi `plot`.
```py
# Fungsi untuk setiap iterasi metode bolzano
def step(this, n):
    x1 = this.x1
    x2 = this.x2
    this.x3 = (x1 + x2) / 2

    fx, fx1, fx2, fx3 = this.calc_func(this.x, x1, x2, this.x3)

    print(f"{n + 1}  {x1:.5f} {x2:.5f} {this.x3:.5f} {fx1:.5f} {fx2:.5f} {fx3:.5f}")

    if (fx1 * fx3 > 0): # Jika hasil perkalian f(x1) dan f(x3) positif maka x1 diubah menjadi nilai x3
        this.x1 = this.x3
    elif (fx1 * fx3 < 0): # Jika hasil perkalian f(x1) dan f(x3) negatif maka x2 diubah menjadi nilai x3
        this.x2 = this.x3

def init_plot(this):
    fig = plt.figure()
    epsilon = 0.5
    ax = plt.axes(xlim=(this.x1 - epsilon, this.x2 + epsilon), ylim=(this.y1, this.y2))
    curve, = ax.plot([], [], color="blue", label="f(x)")
    xl, = ax.plot([], [], color="red")
    xr, = ax.plot([], [], color="red")
    xl_point, = ax.plot([], [], marker="o", color="red", markersize="2", label="x1")
    xr_point, = ax.plot([], [], marker="o", color="green", markersize="2", label="x2")
    return fig, ax, curve, xl, xr, xl_point, xr_point

def clear_plot(this):
    this.xl_point.set_data([], [])
    this.xr_point.set_data([], [])
    this.xl.set_data([], [])
    this.xr.set_data([], [])
    return this.xl_point, this.xr_point, this.xl, this.xr

def animate(this, it):
    this.step(it)
    this.xl_point.set_data([this.x1], [0])
    this.xr_point.set_data([this.x2], [0])
    this.xl.set_data([this.x1, this.x1], [this.y1, this.y2])
    this.xr.set_data([this.x2, this.x2], [this.y1, this.y2])
    this.curve.set_data(this.x, this.y)
    return this.xl, this.xr, this.curve, this.xl_point, this.xr_point

def plot(this):
    print("No    x1      x2      x3      f(x1)   f(x2)   f(x3)")
    animation = FuncAnimation(this.fig, this.animate, this.iterasi, this.clear_plot, interval=250, blit=True, repeat=False) # Fungsi yang digunakan untuk animasi grafik
    plt.axvline(x=0, c="black")
    plt.axhline(y=0, c="black")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.plot()
    plt.show()
    return this.x3
```
Di luar `class Bolzano()` terdapat fungsi `prompt` yang digunakan untuk mendapat input dari user dan fungsi `f(x)` yang digunakan untuk menyimpan fungsi custom (jika ada).
```py
def prompt():
    persamaan = None
    if f(1) == None:
        persamaan = [float(x) for x in input("Input persamaan (Misal: x + 3x - 1 = 0 -> 1 3 -1): ").split()] # Dapatkan input persamaan jika tidak ada fungsi custom
        assert len(persamaan) >= 2, "Harus berupa persamaan dengan minimal 1 x."

    interval = [float(x) for x in input("Input interval (Misal: x1 = 0, x2 = 1 -> 0 1): ").split()] # Dapatkan input interval dan simpan dalam list
    assert len(interval) == 2, "Interval harus di antara 2 x."

    iterasi = int(input("Input banyak iterasi: ")) # Dapatkan input banyaknya iterasi

    return persamaan, interval, iterasi

# Biarkan fungsi ini return None jika ingin memasukkan fungsi di input
# Ubah return menjadi fungsi yang diinginkan (misal: x**2 + x + 1) jika ingin fungsi yang custom
def f(x):
    return None
```
Terakhir, terdapat kode main-nya yang menjalankan semua fungsi yang ada.
```py
if __name__ == "__main__":
    (persamaan, interval, iterasi) = prompt() # Dapatkan input

    bolzano = Bolzano(interval, iterasi, persamaan) # Membuat instance class Bolzano
    akar = bolzano.plot() # Jalankan plotting dan animasi grafik fungsi

    print(f"x = {akar:.5f}") # Print hasil x setelah iterasi
```
## Terima Kasih
