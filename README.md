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

Prompts the user to enter the length and width of a rectangle, then calculates and displays the area.

**How it works:**
```python
largo = float(input("Digite el largo : "))
ancho = float(input("Digite el ancho : "))
area = largo * ancho
print("El area del rectangulo es : ", area)
```

**Sample output:**
```
Digite el largo : 5
Digite el ancho : 3
El area del rectangulo es :  15.0
```

**Skills demonstrated:** `input()`, `float()` casting, arithmetic operators, `print()` with concatenation

---

### 🔷 2. Currency Converter (Colones → USD / Euros) — `ConversorMoneda.py`

**Concept:** Variables, division, f-strings, number formatting

Converts a Costa Rican Colón amount into US Dollars and Euros using fixed exchange rates.

**How it works:**
```python
monto_colones = float(input("Ingrese el monto en colones: "))

tipo_cambio_dolar = 464
tipo_cambio_euro = 543

dolares = monto_colones / tipo_cambio_dolar
euros = monto_colones / tipo_cambio_euro

print(f"Monto en Dólares: ${dolares:,.2f}")
print(f"Monto en Euros: €{euros:,.2f}")
```

**Sample output:**
```
Ingrese el monto en colones: 50000
Monto en Dólares: $107.76
Monto en Euros: €92.08
```

**Skills demonstrated:** `float()`, division, f-strings, `:,.2f` number formatting

---

## 📚 Course Context

These programs were developed as part of:

| Detail | Info |
|--------|------|
| 🎓 Program | Technical Certificate in Data Analytics |
| 🏫 Institution | Universidad Cenfotec, Costa Rica |
| 📅 Period | Feb 2026 – Nov 2026 |
| 📖 Topics | Python basics, variables, operators, conditionals |

**Coursework covers:** Python fundamentals, SQL, R, Power BI, data visualization, EDA, machine learning basics

---

## 🚀 How to Run

1. Make sure **Python 3.x** is installed on your machine
2. Clone this repo or download the `.py` files
3. Open a terminal and run:

```bash
python CalculoRectangulo.py
```
```bash
python ConversorMoneda.py
```

---

## 🗺️ Learning Roadmap

- [x] Variables and data types
- [x] User input and type casting
- [x] Arithmetic operators
- [x] F-strings and number formatting
- [ ] Conditionals (if / elif / else) — *Week 3*
- [ ] Loops (for / while) — *Coming soon*
- [ ] Functions — *Coming soon*
- [ ] Data structures (lists, dictionaries) — *Coming soon*
- [ ] Pandas & data analysis — *Coming soon*

---

## 👩‍💻 Author

**Jennifer Victoria Arriola Salazar**
- 🎓 Technical Certificate in Data Analytics — Universidad Cenfotec
- 💼 [LinkedIn](https://www.linkedin.com/in/jennifervictoriaarriolasalazar/)
- 🐙 [GitHub](https://github.com/jenvic96)
