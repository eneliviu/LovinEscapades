document.addEventListener("DOMContentLoaded", function () {
    let form = document.getElementById("addTripForm");
    let button = document.getElementById("submitButton");

    form.addEventListener("submit", function (e) {
        // Prevent the form from submitting
        // e.preventDefault();

        // Retrieve the start and end dates
        let startDateValue = document.getElementById("id_start_date").value;
        let endDateValue = document.getElementById("id_end_date").value;
        let tripStatus = document.getElementById("id_trip_status");

        let selectedIndex = tripStatus.selectedIndex;
        let selectedOption = tripStatus.options[selectedIndex].value;
        console.log(selectedOption);

        // Convert the date strings to Date objects
        let startDate = new Date(startDateValue);
        let endDate = new Date(endDateValue);

        let currentDate = new Date().toLocaleDateString();

        let errMsg;
        
        // Check if end date is earlier than start date
        if (endDate < startDate) {
            errMsg = "Error: End date cannot be earlier than start date.";
        }
        if ((selectedOption === 'Planned') && (startDate < currentDate)) {
            console.log(startDate < currentDate)
            errMsg = "Error: Cannot plan a trip on past dates.";
        }
        if ((selectedOption === 'Ongoing') &&
            ((currentDate < startDate) || (currentDate > endDate))) {
            errMsg = "Error: Ongoing trip must include the current date.";
        }
        if ((selectedOption === 'Completed') &&
            ((startDate > currentDate) || (currentDate < endDate))) {
            console.log('OK');
            errMsg = "Error: Completed trip cannot have an end date in the future.";
        }

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
});