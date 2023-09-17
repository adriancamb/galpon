
// Manejar el evento submit del formulario
document.getElementById('miFormulario').addEventListener('submit', function (event) {
    // Evitar que el formulario se envíe de manera predeterminada
    event.preventDefault();

    // Validar el formulario
    if (this.checkValidity()) {
        // Validar el formato del correo electrónico
        const email = document.getElementById('email').value;
        if (!validarCorreo(email)) {
            alert('Por favor, ingrese un correo electrónico válido.');
            return;
        }

        // Si el formulario es válido, recopilar los datos
        const nombre = document.getElementById('nombre').value;
        const mensaje = document.getElementById('mensaje').value;

        // Mostrar la información en el modal
        const modalContent = document.querySelector('#mensajeModal .modal-body');
        modalContent.innerHTML = `
            <p>Asunto: Nuevo mensaje de contacto</p>
            <p>Nombre: ${nombre}</p>
            <p>Email: ${email}</p>
            <p>Mensaje:</p>
            <p>${mensaje}</p>
        `;

        // Abre el modal
        const mensajeModal = new bootstrap.Modal(document.getElementById('mensajeModal'));
        mensajeModal.show();
    }
});

// Función para validar el formato del correo electrónico
function validarCorreo(email) {
    const regex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/;
    return regex.test(email);
}
