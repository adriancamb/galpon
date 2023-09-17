const navbarHTML = `
<nav class="navbar navbar-expand-lg bg-light rounded" aria-label="Thirteenth navbar example" >
    <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample11"
        aria-controls="navbarsExample11" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse d-lg-flex" id="navbarsExample11">
        <a class="navbar-brand col-lg-2 me-0" href="#" style="padding:0px"><img src="/img/logo.gif" height="60" alt="Logo galpon" ;> </a>
        <div id="nav-container"></div>

        <ul id="json" class="navbar-nav col-lg-6 justify-content-lg-center"></ul>

                    <!-- CTRL + K + C comentario  -->




        <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Búsqueda" aria-label="Search" id="searchInput">
        <button class="btn btn-outline-warning" type="button" id="searchButton">Buscar</button>
        </form>
        <div id="searchResults" class="grid-container">
        <!-- <script src="/js/busqueda.js"></script> -->
            <!-- Aquí se mostrarán los resultados de búsqueda en la grilla -->
        </div>
        <!-- Icono Usuario -->
        <div id="User" style="display: flex; margin: 7px; align-items: center;">
        <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" enable-background="new 0 0 16 16" version="1.1" viewBox="0 0 16 16" xml:space="preserve"><path id="path7" fill="#231f20" stroke="none" d="M8 .986A7.022 7.022 0 0 0 .986 8c0 1.874.73 3.635 2.055 4.959A6.965 6.965 0 0 0 8 15.014 7.022 7.022 0 0 0 15.014 8 7.022 7.022 0 0 0 8 .986zm0 1A6.021 6.021 0 0 1 14.014 8a5.984 5.984 0 0 1-1.606 4.074 5.836 5.836 0 0 0-2.564-1.754 2.999 2.999 0 0 0 1.11-2.326A2.997 2.997 0 0 0 7.94 5.006a2.997 2.997 0 0 0-2.988 3.012c0 .929.436 1.75 1.104 2.298a5.846 5.846 0 0 0-2.526 1.698A5.964 5.964 0 0 1 1.986 8 6.021 6.021 0 0 1 8 1.986zm-.035 4.02c1.097 0 1.988.892 1.988 2.012A1.988 1.988 0 0 1 8.03 10c-.029 0-.057-.006-.086-.006-.025 0-.049.005-.074.006a1.994 1.994 0 0 1-1.916-2.006c0-1.096.892-1.988 2.012-1.988zm-.096 4.992c.024.001.048.008.072.008h.024c.022 0 .04-.007.062-.008a4.84 4.84 0 0 1 3.643 1.752A5.963 5.963 0 0 1 8 14.014a5.965 5.965 0 0 1-3.742-1.31 4.848 4.848 0 0 1 3.611-1.706z"></path></svg>
        <p style="margin: 0; align-self: center;">Mi cuenta</p>
        </div>
        <!-- Icono carrito -->

        <div class="cart-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-cart" viewBox="0 0 16 16">
            <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
        </svg>
        <div class="cart-badge"><!-- al final está el script con la variable--></div>  
        </div>

    </div>
    </div>
</nav>
`

document.addEventListener("DOMContentLoaded", function () {
    // Agrega el código del navbar al elemento con el ID "Navbar"
    document.getElementById("Navbar").innerHTML = navbarHTML;
  });



