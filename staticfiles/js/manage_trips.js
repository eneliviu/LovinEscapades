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

// let deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
// let deleteButtons = document.getElementsByClassName("btn-delete");
// let deleteConfirm = document.getElementById("deleteConfirm");
// for (let button of deleteButtons) {
//     button.addEventListener("click", (e) => {
//         let tripId = e.target.getAttribute("data-trip_id");
        
//         deleteConfirm.href = `/delete_trip/${tripId}`;
//         deleteModal.show();
//     });
// }

document.addEventListener("DOMContentLoaded", function() {
    // Check if the deleteModal element exists before using it
    let deleteModalElement = document.getElementById("deleteModal");
    if (deleteModalElement) {
        let deleteModal = new bootstrap.Modal(deleteModalElement);
        let deleteButtons = document.getElementsByClassName("btn-delete");
        let deleteConfirm = document.getElementById("deleteConfirm");

        // Ensure deleteConfirm exists before proceeding
        if (deleteConfirm) {
            for (let button of deleteButtons) {
                button.addEventListener("click", (e) => {
                    let tripId = e.target.getAttribute("data-trip_id");
                    
                    deleteConfirm.href = `/delete_trip/${tripId}`;
                    deleteModal.show();
                });
            }
        } else {
            console.error("Element with ID 'deleteConfirm' is not found.");
        }
    } else {
        console.error("Element with ID 'deleteModal' is not found.");
    }
});

/*--------------------------------------------------------------------*/
/* ADD TRIPS */

document.addEventListener("DOMContentLoaded", function () {
    let add_form = document.getElementById("addTripForm");
    //let button = document.getElementById("submitButton");
    let cancelButton_add = document.getElementById("cancelButton");
    
    add_form.addEventListener("submit", function (e) {
       
        let title = document.getElementById("id_title").value.trim();
        let place = document.getElementById("id_place").value.trim();
        let country = document.getElementById("id_country").value.trim();
        
        // Retrieve the start and end dates
        let startDateValue = document.getElementById("id_start_date").value;
        let endDateValue = document.getElementById("id_end_date").value;
        let tripStatus = document.getElementById("id_trip_status");

        let selectedIndex = tripStatus.selectedIndex;
        let selectedOption = tripStatus.options[selectedIndex].value;

        // Convert to Unix time
        let startDate = new Date(startDateValue).getTime();
        let endDate = new Date(endDateValue).getTime();
        let currentDate = new Date().getTime();

        let errMsg = [];

        // Datetime inputs:

        // Check if end date is earlier than start date
        if (endDate < startDate) {
            errMsg.push("Error: End date cannot be earlier than start date.");
        };
        if ( (selectedOption === 'Planned') && (startDate < currentDate) ) {
            // Validate dates for Planned trips
            errMsg.push("Error: Cannot plan a trip on past dates.");
        };
        if ( (selectedOption === 'Ongoing') && 
            !( (startDate <= currentDate) && (endDate >= currentDate)) ) {
            // Validate dates for Ongoing trips
            errMsg.push("Error: Ongoing trip must include the current date.");
        };
        if ( (selectedOption === 'Completed') && 
             (startDate>currentDate && endDate > currentDate) ) {
            // Validate dates for Completed trips
            errMsg.push("Error: Completed trip cannot have an end date in the future.");
        };

        // Text inputs

        if(title.length === 0){
            errMsg.push("Error: Title cannot be empty string.");
        }
        if(place.length === 0){
            errMsg.push("Error: Place cannot be empty string.");
        }
        if(country.length === 0){
            errMsg.push("Error: Country cannot be empty string.");
        }

        // Show errors
        if (errMsg.length>0) {
            // Prevent default submission if there is an error.      
            e.preventDefault();
            alert(errMsg.join('\n'));
        }
        // Otherwise, allows the form to be submitted naturally 
        // if validations passes (standard HTTP form submission).
        // The form data will be sent to the server, and Django will handle the form processing
        // and validation on the server-side.
    });

    cancelButton_add.addEventListener('click', function (e) {
        document.getElementById("addTripForm").reset();
    })

});
