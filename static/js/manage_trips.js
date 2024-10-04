const editButtons = document.getElementsByClassName("btn-edit");
const tripText = document.getElementById("id_body");
const tripForm = document.getElementById("editTripModal");
const submitButton = document.getElementById("editButton");

/* --------------------------------------------------------------------------*/
/* ----------------------  EDIT  ------------------------------------------*/
/* --------------------------------------------------------------------------*/
/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated note's ID upon click.
 * - Fetches the content of the corresponding note.
 * - Populates the `noteText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_note/{noteId}` endpoint.
 */

const editConfirm = document.getElementById("deleteConfirm");
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let tripId = e.target.getAttribute("data-trip_id");
        //let tripContent = document.getElementById(`trip${tripId}`).innerText;
        //tripText.value = tripContent;
        editConfirm.href = `user/edit_trip/${tripId}`;
        submitButton.innerText = "Update";
        //noteForm.setAttribute("action", `edit_note/${tripId}`);
        editModal.show();
    });

}


// OPEN FORM 



/* --------------------------------------------------------------------------*/
/* ----------------------  DELETE  ------------------------------------------*/
/* --------------------------------------------------------------------------*/
/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let tripId = e.target.getAttribute("data-trip_id");
        deleteConfirm.href = `/delete_trip/${tripId}`;
        deleteModal.show();
    });
}