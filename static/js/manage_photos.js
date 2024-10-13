/* --------------------------------------------------------------------------*/
/* ----------------------  DELETE  ------------------------------------------*/
/* --------------------------------------------------------------------------*/
/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For  the `deleteButtons` btn:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteImageConfirm` link's href to point to the 
 * deletion endpoint for the specific photo.
 * - Displays a confirmation modal (`deleteImageConfirm`) to prompt 
 * the user for confirmation before deletion.
 */

let deleteImageModal = new bootstrap.Modal(document
        .getElementById("deleteImageModal"));
let deleteImageButtons = document.getElementsByClassName("btn-delete");
let deleteImageConfirm = document.getElementById("deleteImageConfirm");
for (let button of deleteImageButtons) {
        button.addEventListener("click", (e) => {
                let photoId = e.target.getAttribute("data-photo_id");
                let tripId = e.target.getAttribute("data-trip_id");
                deleteImageConfirm.href = `/delete_photo/${photoId}`;
                deleteImageModal.show();
        });
    }



