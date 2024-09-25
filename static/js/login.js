$(document).ready(function () {
    $('#loginForm').on('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get email and password
        const email = $('#loginemail').val();
        const password = $('#loginpassword').val();

        // Validate email and password
        let isValid = true;

        // Email validation (basic format check)
        if (!email || !/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
            $('#loginemail').addClass('is-invalid').removeClass('is-valid');
            isValid = false;
        } else {
            $('#loginemail').addClass('is-valid').removeClass('is-invalid');
        }

        // Password validation
        if (!password) {
            $('#loginpassword').addClass('is-invalid').removeClass('is-valid');
            isValid = false;
        } else {
            $('#loginpassword').addClass('is-valid').removeClass('is-invalid');
        }

        // If form is valid, make AJAX request
        if (isValid) {
            $.ajax({
                url: '/loginAccount', // Your server endpoint
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ email: email, password: password }),
                success: function(response) {
                    if (response.success) {
                        // Redirect to home page or show success message
                        window.location.href = '/home';
                    } else {
                        // If login fails, mark both fields as invalid
                        $('#loginemail').addClass('is-invalid').removeClass('is-valid');
                        $('#loginpassword').addClass('is-invalid').removeClass('is-valid');

                        // Reset and show the login failed alert
                        $('#loginFailed').hide().show(); // Ensures the alert is shown again if dismissed earlier
                    }
                },
                error: function(xhr, status, error) {
                    // If login fails, mark both fields as invalid
                    $('#loginemail').addClass('is-invalid').removeClass('is-valid');
                    $('#loginpassword').addClass('is-invalid').removeClass('is-valid');

                    // Reset and show the login failed alert
                    $('#loginFailed').hide().show(); // Ensures the alert is shown again if dismissed earlier
                }
            });
        }
    });

    // Optional: Handle the dismiss button click to just hide the alert
    $('.btn-close').on('click', function() {
        $('#loginFailed').hide(); // Just hide it instead of letting Bootstrap remove it from the DOM
    });
});
