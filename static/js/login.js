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

        // Log email and password to the console if valid
        if (isValid) {
            // console.log('Email:', email);
            // console.log('Password:', password);

            // Here you can add AJAX call to send email and password to the server if needed
            $.ajax({
                url: '/loginAccount', // Your server endpoint
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ email: email, password: password }),
                success: function(response) {
                    // Handle successful login
                    // console.log(response);
                    window.location.href = '/home'
                },
                error: function(xhr, status, error) {
                    // Handle login error
                    // console.error('Login failed', error);
                    $('#loginFailed').show()
                }
            });
        }
    });
});