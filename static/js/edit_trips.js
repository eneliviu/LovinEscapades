
document.addEventListener("DOMContentLoaded", function () {
    let edit_form = document.getElementById("editTripForm");
    let cancelButton_edit = document.getElementById("cancelButtonTrip");
    console.log('OK')

    edit_form.addEventListener("submit", (e) => {
        
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

        // console.log(selectedOption);
        // console.log(startDateValue);
        // console.log(endDateValue);
        // console.log(currentDate);

    
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

    cancelButton_edit.addEventListener('click', (e) => {
        document.getElementById("editTripForm").reset();
    })

    


});

/*--------------------------------------------------------------------*/

