# 🐍 Python Beginner Projects

**Python Level: Beginner → Early Intermediate**

This repository contains my first Python programs, developed as part of my **Technical Certificate in Data Analytics** at **Universidad Cenfotec, Costa Rica 🇨🇷**.

---

# 📋 About

These projects represent my first steps in Python programming and problem-solving.

Through these exercises, I have built a strong foundation in:

* Variables and data types (`int`, `float`, `str`)
* User input with `input()`
* Arithmetic operations
* String formatting with f-strings
* Conditional logic (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Counters and accumulators
* Basic data processing logic

---

# 📂 Projects

## 🔷 Basic Programs (Week 1)

### 1. Rectangle Area Calculator — `CalculoRectangulo.py`

**Concepts:** Variables, `float()`, arithmetic operations

```python
largo = float(input("Digite el largo : "))
ancho = float(input("Digite el ancho : "))
area = largo * ancho
print("El area del rectangulo es : ", area)
```

---

### 2. Currency Converter — `ConversorMoneda.py`

**Concepts:** Division, formatting, f-strings

```python
monto_colones = float(input("Ingrese el monto en colones: "))

tipo_cambio_dolar = 464
tipo_cambio_euro = 543

dolares = monto_colones / tipo_cambio_dolar
euros = monto_colones / tipo_cambio_euro

print(f"Monto en Dólares: ${dolares:,.2f}")
print(f"Monto en Euros: €{euros:,.2f}")
```

---

### 3. Student Grade Status — `ResultadoNotas.py`

**Concepts:** Conditional logic, logical operators

```python
nota = int(input("Ingrese la nota del alumno (0-100): "))

if nota < 60:
    print("Resultado: Reprobó")
elif nota >= 60 and nota <= 69:
    print("Resultado: Aplazó")
else:
    print("Resultado: Aprobó")
```

---

### 4. Sales Commission Calculator — `CalculoComisiones.py`

**Concepts:** Multi-branch conditionals, percentages

```python
monto_venta = float(input("Ingrese el monto de la venta: "))

if monto_venta >= 250000:
    comision = monto_venta * 0.10
elif monto_venta < 200000:
    comision = monto_venta * 0.05
else:
    comision = monto_venta * 0.07

print(f"La comisión total es: ₡{comision:,.2f}")
```

---

# 🔷 Loop-Based Programs (Week 3)

These exercises introduce **iteration and data processing**, key concepts for data analysis.

---

### 5. Sum Until Zero — `SumaHastaCero.py`

**Concepts:** `while`, accumulators, break

```python
acum = 0

while True:
    num = float(input("Digite un número: "))
    acum += num
    if num == 0:
        break

print("El total es:", acum)
```

---

### 6. Product of Numbers — `ProductoNumeros.py`

**Concepts:** `while`, counters, multiplication

```python
acum = 1
cont = 1

while cont <= 7:
    num = float(input("Digite un número: "))
    acum *= num
    cont += 1

print("El total es:", acum)
```

---

### 7. Even and Odd Processing — `ParesImpares.py`

**Concepts:** conditionals inside loops

```python
producto_pares = 1
suma_impares = 0
cont = 1

while cont <= 12:
    num = int(input("Digite un número: "))

    if num % 2 == 0:
        producto_pares *= num
    else:
        suma_impares += num

    cont += 1

print("Producto de pares:", producto_pares)
print("Suma de impares:", suma_impares)
```

---

### 8. Average Calculator — `PromedioEdades.py`

**Concepts:** accumulators, counters

```python
acum = 0
cont = 1

while cont <= 10:
    edad = int(input("Digite una edad: "))
    acum += edad
    cont += 1

promedio = acum / 10

print("El promedio es:", promedio)
```

---

### 9. Sum of Odd Numbers (For Loop) — `SumaImparesFor.py`

**Concepts:** `for`, `range()`, conditionals

```python
acum = 0

for num in range(10):
    valor = int(input("Digite un número entero: "))
    if valor % 2 == 1:
        acum += valor

print("La suma de impares es:", acum)
```

---

# 📊 Data Thinking (Early Stage)

Although these are beginner exercises, they already simulate basic data analysis tasks:

* Aggregation → sum, product, average
* Filtering → even vs odd, conditional thresholds
* Iteration → processing multiple inputs
* Logical evaluation → decision-making based on conditions

---

# 📚 Course Context

| Detail         | Info                                               |
| -------------- | -------------------------------------------------- |
| 🎓 Program     | Technical Certificate in Data Analytics            |
| 🏫 Institution | Universidad Cenfotec, Costa Rica                   |
| 📅 Period      | Feb 2026 – Nov 2026                                |
| 📖 Topics      | Python fundamentals, logic, loops, problem solving |

---

# 🚀 How to Run

```bash
python CalculoRectangulo.py
python ConversorMoneda.py
python ResultadoNotas.py
python CalculoComisiones.py
```

---

# 🗺️ Learning Roadmap

✔ Variables and data types
✔ User input and type casting
✔ Arithmetic operations
✔ String formatting (f-strings)
✔ Conditionals
✔ Loops (`while`, `for`)

⬜ Functions — Coming soon
⬜ Data structures — Coming soon
⬜ Pandas / NumPy — Coming soon
⬜ Data analysis projects — Coming soon

---

# 👩‍💻 Author

**Jennifer Victoria Arriola Salazar**

💼 LinkedIn
🐙 GitHub
