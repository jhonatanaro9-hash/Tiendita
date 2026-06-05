x = 5
contador = 0
while True :
 if x < 1.5 :
  break

 print ("su saldo es de ", x, "Bs.")
 print("Puedes comprar:")
 print("1. Papas (Bs. 1.50) ")
 print("2. Chocolate (Bs. 2.00)")
 print("3. Reffresco (Bs. 2.50)")
 print("4. Salir")
 op=int(input("ingrese una opcion; "))
 if op == 1 :
   precio = 1.5
 elif op == 2 :
   precio = 2
 elif op == 3 :
   precio = 2.5
 else :
   precio = 5 

 if precio == 5 :
  print("Gracias por su preferencia")
  x=0 
 else :
  if x>=precio :
   x = x - precio
   contador = contador +1 
   print("Gracias por su compra")
   print("Productos comprados", contador)
  else :
   print ("saldo insuficiente")
if x == 0 :
 print ("Saldo restante 5 Bs.")
else :
 print ("Saldo restante", x, "Bs.")