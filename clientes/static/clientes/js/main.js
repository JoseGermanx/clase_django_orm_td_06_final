

document.addEventListener('DOMContentLoaded', () => {
    let urlEliminar = null;
    let idEliminar = null;

    document.querySelectorAll('.btn-eliminar').forEach(btn => {
        btn.addEventListener('click', function () {
            urlEliminar = this.dataset.url;
            idEliminar = this.dataset.id;
            const nombre = this.dataset.nombre;
            document.getElementById('nombreCliente').textContent = nombre;


            const modal = new bootstrap.Modal(document.getElementById('modalEliminar'));
            modal.show();
        });
    });

        document.getElementById('btnCancelarEliminar').addEventListener('click', function () {
        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
        document.body.classList.remove('modal-open');
        document.body.style.removeProperty('padding-right');
        document.body.style.removeProperty('overflow');
        
    }
    )

    document.getElementById('btnConfirmarEliminar').addEventListener('click', function () {
        if (!urlEliminar || !idEliminar) return;

        fetch(urlEliminar, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error en la solicitud: ' + response.status);
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    window.location.href = '/clientes';
                }
            })
            .catch(error => {
                console.error('Error al eliminar:', error);
                alert("Ocurrio un error.")
            });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});