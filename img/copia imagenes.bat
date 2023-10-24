

set "sourceFile=logo.jpg"
set "destinationFolder=." 


set "imageNames=arrollamanguera-1.jpg arrollamanguera-2.jpg bebedero-hoja-de-parra.jpg bebedero-mini.jpg bebedero-ostra.jpg llamador-1.jpg llamador-2.jpg veleta-1.jpg veleta-2.jpg jardin-en-fundicion-de-aluminio-1.jpg jardin-en-fundicion-de-aluminio-2.jpg jardin-en-fundicion-de-hierro-1.jpg jardin-en-fundicion-de-hierro-2.jpg jardin-en-hierro-forjado-1.jpg jardin-en-hierro-forjado-2.jpg accesorio-para-parrilla-1.jpg accesorio-para-parrilla-2.jpg asador-1.jpg asador-2.jpg herraje-1.jpg herraje-2.jpg parrilla-a-carbon-o-lena-1.jpg parrilla-a-carbon-o-lena-2.jpg parrilla-a-gas-1.jpg parrilla-a-gas-2.jpg hogar-1.jpg hogar-2.jpg farol-1.jpg farol-2.jpg farol-con-columna-1.jpg farol-con-columna-2.jpg caldero-en-hierro-1.jpg caldero-en-hierro-2.jpg cacerola-de-fundicion-enlozada-1.jpg cacerola-de-fundicion-enlozada-2.jpg cacerola-de-fundicion-sin-enlozar-1.jpg cacerola-de-fundicion-sin-enlozar-2.jpg cacerola-de-fundicion-ovalada-1.jpg cacerola-de-fundicion-ovalada-2.jpg cacerola-de-fundicion-doble-funcion-1.jpg cacerola-de-fundicion-doble-funcion-2.jpg plancha-para-bifes-lisa-1.jpg plancha-para-bifes-lisa-2.jpg plancha-para-bifes-rayada-enlozada-1.jpg plancha-para-bifes-rayada-enlozada-2.jpg plancha-para-bifes-rayada-sin-enlozar-1.jpg plancha-para-bifes-rayada-sin-enlozar-2.jpg provoletera-de-fundicion-mango-de-madera-enlozada-1.jpg provoletera-de-fundicion-mango-de-madera-enlozada-2.jpg provoletera-de-fundicion-mango-de-madera-sin-enlozar-1.jpg provoletera-de-fundicion-mango-de-madera-sin-enlozar-2.jpg provoletera-de-fundicion-mango-de-fundicion-enlozada-1.jpg provoletera-de-fundicion-mango-de-fundicion-enlozada-2.jpg provoletera-de-fundicion-mango-de-fundicion-sin-enlozar-1.jpg provoletera-de-fundicion-mango-de-fundicion-sin-enlozar-2.jpg provoletera-de-15-porciones-enlozada-1.jpg provoletera-de-15-porciones-enlozada-2.jpg provoletera-de-15-porciones-sin-enlozar-1.jpg provoletera-de-15-porciones-sin-enlozar-2.jpg asadera-en-chapa-plegada-1.jpg asadera-en-chapa-plegada-2.jpg paellera-con-2-asas-enlozada-1.jpg paellera-con-2-asas-enlozada-2.jpg paellera-con-2-asas-sin-enlozar-1.jpg paellera-con-2-asas-sin-enlozar-2.jpg wok-enlozado-1.jpg wok-enlozado-2.jpg wok-sin-enlozar-1.jpg wok-sin-enlozar-2.jpg sarten-mango-de-planchuela-1.jpg sarten-mango-de-planchuela-2.jpg pizzera-en-chapa-enlozada-1.jpg pizzera-en-chapa-enlozada-2.jpg"

for %%i in (%imageNames%) do (
    copy /y "%sourceFile%" "%destinationFolder%\%%i"
)

echo Copia de imágenes completa.
pause