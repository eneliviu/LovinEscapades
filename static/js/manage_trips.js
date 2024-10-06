
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

// var editButtons = document.getElementsByClassName("btn-edit");
// var tripText = document.getElementById("id_body");
// var tripForm = document.getElementById("editTripModal");
// var submitButton = document.getElementById("editButton");

// var editConfirm = document.getElementById("deleteConfirm");
// for (let button of editButtons) {
//     button.addEventListener("click", (e) => {
//         var tripId = e.target.getAttribute("data-trip_id");
//         let tripContent = document.getElementById(`trip${tripId}`).innerText;
//         //tripText.value = tripContent;
//         editConfirm.href = `user/edit_trip/${tripId}`;
//         submitButton.innerText = "Update";
//         //noteForm.setAttribute("action", `edit_note/${tripId}`);
//         editModal.show();
//     });

// }



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

// let deleteModal = bootstrap.Modal.getOrCreateInstance("deleteModal")
let deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
let deleteButtons = document.getElementsByClassName("btn-delete");
let deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let tripId = e.target.getAttribute("data-trip_id");
        deleteConfirm.href = `/delete_trip/${tripId}`;
        deleteModal.show();
    });
}

/*--------------------------------------------------------------------*/
/* ADD TRIPS */

document.addEventListener("DOMContentLoaded", function () {
    let add_form = document.getElementById("addTripForm");
    //let button = document.getElementById("submitButton");
    let cancelButton_add = document.getElementById("cancelButton");

    add_form.addEventListener("submit", function (e) {
        
        // Retrieve the start and end dates
        let startDateValue = document.getElementById("id_start_date").value;
        let endDateValue = document.getElementById("id_end_date").value;
        let tripStatus = document.getElementById("id_trip_status");

        let selectedIndex = tripStatus.selectedIndex;
        let selectedOption = tripStatus.options[selectedIndex].value;
        console.log(selectedOption)

        // Convert the date strings to Date objects
        let startDate = new Date(startDateValue).toLocaleDateString();
        let endDate = new Date(endDateValue).toLocaleDateString();

        // let currentDate = new Date(new Date().toDateString());

        let currentDate = new Date().toLocaleDateString();
        let errMsg;
    
        // Check if end date is earlier than start date
        if (endDate < startDate) {
            errMsg = "Error: End date cannot be earlier than start date.";
        };
        if ((selectedOption === 'Planned') && (startDate < currentDate)) {
            // Validate dates for Planned trips
            errMsg = "Error: Cannot plan a trip on past dates.";
        };
        if ((selectedOption === 'Ongoing') && 
            !((startDate <= currentDate) && (endDate >= currentDate) )) {
            // Validate dates for Ongoing trips
            errMsg = "Error: Ongoing trip must include the current date.";
        };
        if ((selectedOption === 'Completed') &&
            ((startDate > currentDate) || (currentDate < endDate))) {
            // Validate dates for Completed trips
            errMsg = "Error: Completed trip cannot have an end date in the future.";
        };

        if (errMsg) {
            // Prevent default submission if there is an error.      
            e.preventDefault();
            alert(errMsg);
        }
        // Otherwise, allows the form to be submitted naturally 
        // if validations passes (standard HTTP form submission).
        // The form data will be sent to the server, and Django will handle the form processing
        // and validation on the server-side.
    });

    cancelButton_add.addEventListener('click', function (e) {
        document.getElementById("addTripForm").reset();
    })

    /*--------------------------------------------------------------------*/
    /* Edit TRIPS */
    // let edit_form = document.getElementById("editTripForm");
    // //let button = document.getElementById("submitButton");
    // let cancelButton_edit = document.getElementById("cancelButton");

    // edit_form.addEventListener("submit", function (e) {
        
    //     // Retrieve the start and end dates
    //     let startDateValue = document.getElementById("id_start_date").value;
    //     let endDateValue = document.getElementById("id_end_date").value;
    //     let tripStatus = document.getElementById("id_trip_status");

    //     let selectedIndex = tripStatus.selectedIndex;
    //     let selectedOption = tripStatus.options[selectedIndex].value;
    //     console.log(selectedOption)

    //     // Convert the date strings to Date objects
    //     let startDate = new Date(startDateValue).toLocaleDateString();
    //     let endDate = new Date(endDateValue).toLocaleDateString();

    //     // let currentDate = new Date(new Date().toDateString());

    //     let currentDate = new Date().toLocaleDateString();
    //     let errMsg;
    
    //     // Check if end date is earlier than start date
    //     if (endDate < startDate) {
    //         errMsg = "Error: End date cannot be earlier than start date.";
    //     };
    //     if ((selectedOption === 'Planned') && (startDate < currentDate)) {
    //         // Validate dates for Planned trips
    //         errMsg = "Error: Cannot plan a trip on past dates.";
    //     };
    //     if ((selectedOption === 'Ongoing') && 
    //         !((startDate <= currentDate) && (endDate >= currentDate) )) {
    //         // Validate dates for Ongoing trips
    //         errMsg = "Error: Ongoing trip must include the current date.";
    //     };
    //     if ((selectedOption === 'Completed') &&
    //         ((startDate > currentDate) || (currentDate < endDate))) {
    //         // Validate dates for Completed trips
    //         errMsg = "Error: Completed trip cannot have an end date in the future.";
    //     };

    //     if (errMsg) {
    //         // Prevent default submission if there is an error.      
    //         e.preventDefault();
    //         alert(errMsg);
    //     }
    //     // Otherwise, allows the form to be submitted naturally 
    //     // if validations passes (standard HTTP form submission).
    //     // The form data will be sent to the server, and Django will handle the form processing
    //     // and validation on the server-side.
    // });

    // cancelButton_edit.addEventListener('click', function (e) {
    //     document.getElementById("EditTripForm").reset();
    // })


});

/*--------------------------------------------------------------------*/
/* Edit TRIPS */
