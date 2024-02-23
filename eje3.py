# Un estudiante debe realizar su proceso de matritula teniendo en cuenta los siguiente:
#monto:?


cons_credito1Str = 28000
cons_credito2Str = 35000
cons_credito3Str = 40000
cons_credito4Str = 45000
cons_credito5Str = 55000
cons_credito6Str = 60000
cons_credito7Str = 75000
cons_credito8Str = 80000
cons_credito9Str = 95000
cons_credito10Str = 110000

var_nombreStr = input('Nombre')
var_contactoStr = input('Contacto')
var_montoFlt = float(input('Monto disponible ->'))
var_creditosStr = int(input(' --Crédito--\n\n1. 15 créditos \n2. 10 créditos \n3. 12 créditos\n4. 11 créditos\n5. 16 créditos\n6. 17 créditos\n7. 9 créditos\n8. 18 créditos\n9. 12 créditos\n10. 17 créditos\n ->'))

if var_creditosStr == 1:
    var_opcionInt = 15
    var_totalFlt = cons_credito1Str * 15
    
if var_creditosStr == 2:
    var_opcionInt   = 10
    var_totalFlt = cons_credito2Str * 10

if var_creditosStr == 3:
    var_opcionInt   = 12
    var_totalFlt = cons_credito3Str * 12


if var_creditosStr == 4:
    var_opcionInt  = 11
    var_totalFlt = cons_credito4Str * 11

if var_creditosStr == 5:
    var_opcionInt  = 16
    var_totalFlt = cons_credito5Str * 16

if var_creditosStr == 6:
    var_opcionInt   = 17
    var_totalFlt = cons_credito6Str * 17

if var_creditosStr == 7:
    var_opcionInt   = 9
    var_totalFlt = cons_credito7Str * 9

if var_creditosStr == 8:
    var_opcionInt  = 18
    var_totalFlt = cons_credito8Str * 18

if var_creditosStr == 9:
    var_opcionInt  = 12 
    var_totalFlt = cons_credito9Str * 12

if var_creditosStr == 10:
    var_opcionInt  = 17
    var_totalFlt = cons_credito10Str * 17

var_totalmatricula = var_totalFlt

print ('<<<REPORTE>>>\n')
print('NOMBRE.................', var_nombreStr)
print('CONTACTO...............', var_contactoStr)
print('MONTO..................', var_montoFlt)
print('CREDITOS...............', var_opcionInt)
print('TOTAL A PAGAR..........', var_totalFlt)

if var_totalmatricula >= var_montoFlt:
    print('No cuentas con los fondos suficientes para matricular este credito')
else:
    print('Cuentas con los fondos suficientes para matricular este credito')


