# 🐍 Python Beginner Projects

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-F5A623?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-7AB648?style=for-the-badge)

> First Python scripts built as part of my **Technical Certificate in Data Analytics** at Universidad Cenfotec, Costa Rica 🇨🇷

---

## 📋 About

This repository contains my first Python programs, written during **Week 1 and Week 3** of my Data Analytics program. These projects cover Python fundamentals including:

- Variables and data types (`int`, `float`, `str`)
- User input with `input()`
- Arithmetic operations
- String formatting with f-strings
- Conditional logic (`if`, `elif`, `else`)

---

## 📂 Projects

---

### 🔷 1. Rectangle Area Calculator — `CalculoRectangulo.py`

**Concept:** Variables, `float()`, arithmetic operations, `print()`

```python
largo = float(input("Digite el largo : "))
ancho = float(input("Digite el ancho : "))
area = largo * ancho
print("El area del rectangulo es : ", area)
```

---

### 🔷 2. Currency Converter — `ConversorMoneda.py`

**Concept:** Division, f-strings, formatting

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

### 🔷 3. Student Grade Status — `ResultadoNotas.py`

**Concept:** Conditionals, logical operators

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

### 🔷 4. Sales Commission Calculator — `CalculoComisiones.py`

**Concept:** Multi-branch conditionals, percentages

```python
monto_venta = float(input("Ingrese el monto de la venta: "))

if monto_venta >= 250000:
    comision = monto_venta * 0.10
elif monto_venta < 200000:
    comision = monto_venta * 0.05
else:
    # Este rango cubre entre 200000 y 250000 inclusive
    comision = monto_venta * 0.07

print(f"La comisión total es: ₡{comision:,.2f}")
```

---

## 📚 Course Context

| Detail | Info |
|--------|------|
| 🎓 Program | Technical Certificate in Data Analytics |
| 🏫 Institution | Universidad Cenfotec, Costa Rica |
| 📅 Period | Feb 2026 – Nov 2026 |
| 📖 Topics | Python basics, variables, operators, conditionals |

---

## 🚀 How to Run

```bash
python CalculoRectangulo.py
python ConversorMoneda.py
python ResultadoNotas.py
python CalculoComisiones.py
```

---

## 🗺️ Learning Roadmap

- [x] Variables and data types  
- [x] User input and type casting  
- [x] Arithmetic operators  
- [x] F-strings and formatting  
- [x] Conditionals  
- [ ] Loops — Coming soon  
- [ ] Functions — Coming soon  
- [ ] Data structures — Coming soon  

---

## 👩‍💻 Author

**Jennifer Victoria Arriola Salazar**

- 💼 [LinkedIn](https://www.linkedin.com/in/jennifervictoriaarriolasalazar/)  
- 🐙 [GitHub](https://github.com/jenvic96)
