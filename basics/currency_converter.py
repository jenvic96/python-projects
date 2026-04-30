# Programa para convertir colones a: USD/Euro

monto_colones = float(input("Ingrese el monto en colones: "))

tipo_cambio_dolar = 464
tipo_cambio_euro = 543

dolares = monto_colones / tipo_cambio_dolar
euros = monto_colones / tipo_cambio_euro

print(f"Monto en Dólares: ${dolares:,.2f}")
print(f"Monto en Euros: €{euros:,.2f}")
