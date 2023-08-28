

set "sourceFile=logo.jpg"
set "destinationFolder=." 


set "imageNames=Jardin.jpg Llamadores.jpg Veletas.jpg Muebles-de-Jardin.jpg Fundicion-de-aluminio.jpg Funcion-de-hierro.jpg Hierro-forjado.jpg Parrillas.jpg Accesorios-para-parrillas.jpg Asadores.jpg Herrajes.jpg Parrillas-a-carbon-o-leña.jpg Parrillas-a-gas.jpg Calefaccion.jpg Hogares.jpg Iluminacion.jpg Faroles.jpg Faroles-con-columnas.jpg Gastronomia.jpg Calderos-en-hierro.jpg Cacerolas-de-fundicion.jpg Cacerolas-de-fundicion-enlonzadas.jpg Cacerolas-de-fundicion-sin-enlonzar.jpg Cacerolas-de-fundicion-Ovaladas.jpg Cacerolas-de-fundicion-doble-funcion.jpg Planchas-para-bifes.jpg Planchas-para-bifes-lisas.jpg Planchas-para-bifes-rayadas.jpg Planchas-para-bifes-rayadas-enlonzadas.jpg Planchas-para-bifes-rayadas-sin-enlonzar.jpg Provoleteras-de-fundicion.jpg Provoleteras-de-fundicion-mangos-de-madera.jpg Provoleteras-de-fundicion-mangos-de-madera-enlonzadas.jpg Provoleteras-de-fundicion-mangos-de-madera-sin-enlonzar.jpg Provoleteras-de-fundicion-mangos-de-fundicion.jpg Provoleteras-de-fundicion-mangos-de-enlonzadas.jpg Provoleteras-de-fundicion-mangos-de-sin-enlonzar.jpg Provoleteras-de-15-porciones.jpg Provoleteras-de-15-porciones-enlonzadas.jpg Provoleteras-de-15-porciones-sin-enlonzar.jpg Asaderas-en-chapa-plegada.jpg Paelleras-con-2-asas.jpg Paelleras-con-2-asas-enlonzadas.jpg Paelleras-con-2-asas-sin-enlonzar.jpg Woks.jpg Woks-enlonzados.jpg Woks-sin-enlonzar.jpg Sartén-mango-de-planchuela.jpg Pizzera-en-chapa-enlozada.jpg"

for %%i in (%imageNames%) do (
    copy /y "%sourceFile%" "%destinationFolder%\%%i"
)

echo Copia de imágenes completa.
pause