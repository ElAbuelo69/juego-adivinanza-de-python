
tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

tipo_conversion = input("ingrese la moneda de origen para la conversión EUR o USD")
monto_a_convertir = float(input("Ingrese el monto a convertir:"))

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es:",resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es:",resultado)
else:
    print("Input no disponible")