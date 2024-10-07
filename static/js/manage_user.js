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


/* --------------------------------------------------------------------------*/
/* ----------------------  EDIT  ------------------------------------------*/
/* --------------------------------------------------------------------------*/
/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 

var editButtonsPost = document.getElementsByClassName("btn-edit");
var postTextPost = document.getElementById("id_body");
var postFormPost = document.getElementById("addTestimonialForm");
var submitButtonPost = document.getElementById("submitButton");

for (let button of editButtonsPost) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        let commentContent = document.getElementById(`body${postId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${postId}`);
    });
}

*/