import matplotlib.pyplot as plt
import pandas as pd

class SecantMethod:
    """
    Class Metode Secant untuk mencari akar persamaan f(x)=0
    """

    def __init__(self, func, x0, x1, tol, max_iter):
        self.func = func
        self.x0 = x0
        self.x1 = x1
        self.tol = tol
        self.max_iter = max_iter
        self.history = []

    def iterate(self):
        x_prev = self.x0
        x_curr = self.x1

        for i in range(self.max_iter):
            f_prev = self.func(x_prev)
            f_curr = self.func(x_curr)

            if abs(f_curr - f_prev) < 1e-15: 
                print("Peringatan: Pembagi nol atau terlalu kecil!")
                break

            x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
            error = abs(x_next - x_curr)

            self.history.append({
                "iterasi": i + 1,
                "x": x_next,
                "error": error
            })

            if error < self.tol:
                self.root = x_next
                return x_next

            x_prev = x_curr
            x_curr = x_next

        self.root = x_curr
        return x_curr

    def show_solution(self):
        if self.root is not None:
            print(f"Akar Hampiran = {self.root}")
        else:
            print("Metode belum dijalankan. Panggil iterate() terlebih dahulu.")

        df = pd.DataFrame(self.history)
        print("\nTABEL ITERASI:")
        print(df.to_string(index=False))
        print(f"\n{'='*30}")
        
    def plot(self):
        if not self.history:
            print("Tidak ada data untuk diplot.")
            return
        
        print("RINGKASAN SOLUSI")
        print(f"{'='*30}")
        print(f"Akar (x)        : {self.root:.10f}")
        print(f"Nilai f(x)      : {self.func(self.root):.2e}")
        print(f"Total Iterasi   : {len(self.history)}")
        print(f"Galat Terakhir  : {self.history[-1]['error']:.2e}")
        print(f"{'='*30}")

        xs = [h["x"] for h in self.history]
        it = [h["iterasi"] for h in self.history]

        plt.figure(figsize=(8, 4))
        plt.plot(it, xs, marker="o", linestyle='-', color='b')
        plt.xlabel("Iterasi")
        plt.ylabel("Nilai x")
        plt.title("Konvergensi Metode Secant")
        plt.grid(True)
        plt.show()