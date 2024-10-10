$(document).ready(function() {
    // Define a function to toggle class based on window width
    function imageResize() {
        if (window.innerWidth < 768) {
            $('#hero-img').addClass('img-fluid').removeClass('c-img');
        } else {
            $('#hero-img').addClass('c-img').removeClass('img-fluid');
        }
    }

    // Initial check when the document is ready
    imageResize();

    // Check on window resize
    $(window).resize(imageResize);
});