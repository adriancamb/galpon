$(document).ready(function () {
    // Hace una solicitud AJAX al archivo JSON
    $.getJSON("categorias.json", function (data) {
        // Crea un elemento <ul> para contener los elementos de navegación
        var navList = $("<ul>");

        // Recorre los elementos de navegación del archivo JSON
        $.each(data.nav_items, function (index, item) {
            // Crea un elemento <li> para cada elemento de navegación
            var navItem = $("<li>");

            // Si el elemento de navegación es la página actual, agrega la clase "active"
            if (item.current_page) {
                navItem.addClass("active");
            }

            // Crea un enlace <a> con el texto y URL del elemento de navegación
            var navLink = $("<a>").attr("href", item.url).text(item.text);

            // Si el elemento de navegación tiene un menú desplegable, crea el menú desplegable
            if (item.dropdown) {
                var dropdownMenu = $("<ul>").addClass("dropdown-menu");

                // Recorre los elementos del menú desplegable
                $.each(item.dropdown_items, function (index, dropdownItem) {
                    // Crea un elemento <li> para cada elemento del menú desplegable
                    var dropdownMenuItem = $("<li>");

                    // Crea un enlace <a> con el texto y URL del elemento del menú desplegable
                    var dropdownMenuLink = $("<a>").attr("href", dropdownItem.url).text(dropdownItem.text);

                    // Agrega el enlace al elemento <li> del menú desplegable
                    dropdownMenuItem.append(dropdownMenuLink);

                    // Agrega el elemento <li> al menú desplegable
                    dropdownMenu.append(dropdownMenuItem);
                });

                // Agrega la clase "dropdown-toggle" al enlace de navegación
                navLink.addClass("dropdown-toggle");

                // Agrega los atributos data-bs-toggle y aria-expanded al enlace de navegación
                navLink.attr("data-bs-toggle", "dropdown");
                navLink.attr("aria-expanded", "false");

                // Agrega el menú desplegable al elemento <li> del elemento de navegación
                navItem.append(navLink);
                navItem.append(dropdownMenu);
            } else {
                // Si el elemento de navegación no tiene un menú desplegable, simplemente agrega el enlace al elemento <li>
                navItem.append(navLink);
            }

            // Agrega el elemento <li> al elemento <ul> de navegación
            navList.append(navItem);
        });

        // Agrega la clase "navbar-nav" y "col-lg-6 justify-content-lg-center" al elemento <ul> de navegación
        navList.addClass("navbar-nav col-lg-6 justify-content-lg-center");

        // Agrega el elemento <ul> de navegación al contenedor de navegación en el archivo HTML
        $("#nav-container").append(navList);
    });
});
