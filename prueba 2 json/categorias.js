$(document).ready(function() {
    $.getJSON("categorias.json", function(data) {
      var nav = $("<ul>").addClass("navbar-nav col-lg-6 justify-content-lg-center");
      $.each(data, function(categoria, subcategorias) {
        var dropdown = $("<li>").addClass("nav-item dropdown");
        var link = $("<a>").addClass("nav-link dropdown-toggle").attr({
          "href": "#",
          "data-bs-toggle": "dropdown",
          "aria-expanded": "false"
        }).text(categoria);
        var menu = $("<ul>").addClass("dropdown-menu");
        $.each(subcategorias, function(index, subcategoria) {
          var item = $("<li>").addClass("nav-item");
          var sublink = $("<a>").addClass("dropdown-item").attr("href", "#").text(subcategoria);
          item.append(sublink);
          menu.append(item);
        });
        dropdown.append(link, menu);
        nav.append(dropdown);
      });
      $("#nav-container").html(nav);
    });
  });
  