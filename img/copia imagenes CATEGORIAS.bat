

set "sourceFile=logo.jpg"
set "destinationFolder=." 


set "imageNames=jardin.jpg arrollamangueras.jpg bebederos.jpg llamadores.jpg veletas.jpg muebles-de-jardin.jpg muebles-de-jardin-fundicion-de-aluminio.jpg muebles-de-jardin-fundicion-de-hierro.jpg muebles-de-jardin-en-hierro-forjado.jpg parrillas.jpg accesorios-para-parrillas.jpg asadores.jpg herrajes.jpg parrillas-a-carbon-o-lena.jpg parrillas-a-gas.jpg calefaccion.jpg hogares.jpg iluminacion.jpg faroles.jpg faroles-con-columnas.jpg gastronomia.jpg calderos-en-hierro.jpg cacerolas-de-fundicion.jpg cacerolas-de-fundicion-enlozadas.jpg cacerolas-de-fundicion-sin-enlozar.jpg cacerolas-de-fundicion-ovaladas.jpg cacerolas-de-fundicion-doble-funcion.jpg planchas-para-bifes.jpg planchas-para-bifes-lisas.jpg planchas-para-bifes-rayadas.jpg planchas-para-bifes-rayadas-enlozadas.jpg planchas-para-bifes-rayadas-sin-enlozar.jpg provoleteras-de-fundicion.jpg provoleteras-de-fundicion-mango-de-madera.jpg provoleteras-de-fundicion-mango-de-madera-enlozadas.jpg provoleteras-de-fundicion-mango-de-madera-sin-enlozar.jpg provoleteras-de-fundicion-mango-de-fundicion.jpg provoleteras-de-fundicion-mango-de-enlozadas.jpg provoleteras-de-fundicion-mango-de-sin-enlozar.jpg provoleteras-de-15-porciones.jpg provoleteras-de-15-porciones-enlozadas.jpg provoleteras-de-15-porciones-sin-enlozar.jpg asaderas-en-chapa-plegada.jpg paelleras-con-2-asas.jpg paelleras-con-2-asas-enlozadas.jpg paelleras-con-2-asas-sin-enlozar.jpg woks.jpg woks-enlozados.jpg woks-sin-enlozar.jpg sarten-mango-de-planchuela.jpg pizzera-en-chapa-enlozada.jpg"

for %%i in (%imageNames%) do (
    copy /y "%sourceFile%" "%destinationFolder%\%%i"
)

echo Copia de imágenes completa.
pause