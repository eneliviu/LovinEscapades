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

var deleteModal2 = new bootstrap.Modal(document.getElementById("deleteModal2"));
var deleteButtons2 = document.getElementsByClassName("btn-delete");
var deleteConfirm2 = document.getElementById("deleteConfirm2");

for (let button of deleteButtons2) {
    button.addEventListener("click", (e) => {
        var postId = e.target.getAttribute("data-post_id");
        // console.log(postId)
        deleteConfirm2.href = `delete_post/${postId}`;
        deleteModal2.show();
    });
}