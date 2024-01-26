print("Bienvenido a su supermercado favorito")
unidades=eval(input("Por favor ingrese la cantidad de unidades del producto"))
descuento=0
regalo=0
precio=5000

docenas = unidades//12
if(docenas>0 and docenas<=3):
    descuento=0.1
    regalo=0
elif(docenas>3):
    descuento=0.15
    regalo=docenas-3

Monto = unidades*precio
descuentoTotal=unidades*precio*descuento
MontoPagar = Monto - descuentoTotal

print("Monto sin descuento:", Monto)
print("Descuento: ", descuentoTotal)
print("Monto a pagar: ", MontoPagar)
print("Regalo de unidades:",  regalo)
print("Nuevo total de unidades: ", unidades + regalo)