/* --------------------------------------------------------------------------*/
/* ----------------------  DELETE  ------------------------------------------*/
/* --------------------------------------------------------------------------*/
/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteModalPost` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModalPost`) to prompt 
 * the user for confirmation before deletion.
 */

var deleteModalPost = new bootstrap.Modal(document.getElementById("deleteModalPost"));
var deleteButtonsPost = document.getElementsByClassName("btn-delete");
var deleteConfirmPost = document.getElementById("deletePostConfirm");

for (let button of deleteButtonsPost) {
    button.addEventListener("click", (e) => {
        var postId = e.target.getAttribute("data-post_id");
        deleteConfirmPost.href = `delete_post/${postId}`;
        deleteModalPost.show();
    });
}
