
var editButtons = document.getElementsByClassName("btn-edit");
var tripText = document.getElementById("id_body");
var tripForm = document.getElementById("editTripModal");
var submitButton = document.getElementById("editButton");

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


var editConfirm = document.getElementById("deleteConfirm");
for (var button of editButtons) {
    button.addEventListener("click", (e) => {
        var postId = e.target.getAttribute("data-posts_id");
        //var tripContent = document.getElementById(`trip${tripId}`).innerText;
        //tripText.value = tripContent;
        editConfirm.href = `user/profile/${postId}`;
        submitButton.innerText = "Update";
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


//var deleteModal = new bootstrap.Modal(document.getElementById("deleteModal2"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var deleteConfirm = document.getElementById("deleteConfirm");

for (var button of deleteButtons) {
    button.addEventListener("click", (e) => {
        var postId = e.target.getAttribute("data-post_id");
        console.log(postId)
        deleteConfirm.href = `user/profile/${postId}`;
        console.log('OK')
        //deleteModal.show();
    });
}