monto_venta = float(input("Ingrese el monto de la venta: "))

if monto_venta >= 250000:
    comision = monto_venta * 0.10
elif monto_venta < 200000:
    comision = monto_venta * 0.05
else:
    # Este rango cubre entre 200000 y 250000 inclusive
    comision = monto_venta * 0.07

print(f"La comisión total es: ₡{comision:,.2f}")
