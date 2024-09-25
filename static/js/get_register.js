$(document).ready(function () {
        function validateField(input, pattern = null) {
            const value = $(input).val();
            const valid = pattern ? pattern.test(value) : value.trim() !== '';
            $(input).toggleClass('is-invalid', !valid);
            $(input).toggleClass('is-valid', valid);
        }

        function validatePasswordMatch() {
            const password = $('#password').val();
            const confirmPassword = $('#confirmPassword').val();
            const match = password === confirmPassword && password !== '';
            $('#confirmPassword').toggleClass('is-invalid', !match);
            $('#confirmPassword').toggleClass('is-valid', match);
        }

        // Real-time validation on input change
        $('#firstName, #lastName, #address, #gender, #birthday, #contact, #email, #password, #confirmPassword').on('input change', function () {
            const id = $(this).attr('id');
            if (id === 'contact') {
                validateField(this, /^[0-9]+$/); // Validates contact to contain only numbers
            } else if (id === 'email') {
                validateField(this, /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/); // Validates email format
            } else if (id === 'confirmPassword') {
                validatePasswordMatch(); // Check if passwords match
            } else {
                validateField(this); // General validation for empty fields
            }
        });

        // On form submit
        $('#myForm').on('submit', function (event) {
            event.preventDefault();

            let isValid = true;

            $('#loginLoading').show()
            $('#btnLogin').hide()

            setTimeout(() => {
                // Validate all fields again on submit
                $('#firstName, #lastName, #address, #gender, #birthday, #contact, #email, #password, #confirmPassword').each(function () {
                    const id = $(this).attr('id');
                    if (id === 'contact') {
                        validateField(this, /^[0-9]+$/); // Validate contact
                    } else if (id === 'email') {
                        validateField(this, /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/); // Validate email
                    } else if (id === 'confirmPassword') {
                        validatePasswordMatch(); // Validate password match
                    } else {
                        validateField(this); // General validation
                    }
                    if ($(this).hasClass('is-invalid')) {
                        isValid = false;
                    }
                });

                if (isValid) {
                    // Gather form data
                    const formData = {
                        firstName: $('#firstName').val(),
                        lastName: $('#lastName').val(),
                        address: $('#address').val(),
                        gender: $('#gender').val(),
                        birthday: $('#birthday').val(),
                        contact: $('#contact').val(),
                        email: $('#email').val(),
                        password: $('#password').val(),
                        confirmPassword: $('#confirmPassword').val()
                    };

                    // AJAX POST request to Flask route
                    $.ajax({
                        url: '/createAccount', // Flask route
                        type: 'POST',
                        contentType: 'application/json',
                        data: JSON.stringify(formData), // Send the form data as JSON
                        success: function (response) {
                            // Handle success response (e.g., show a success message)
                            console.log(response)
                            $('#createAccount').show()
                            $('#loginLoading').hide()
                            $('#btnLogin').show()
                            setTimeout(() => {
                                $('#createAccount').hide()
                                setTimeout(() => {
                                    // Redirect to the login page
                                    window.location.href = "/";
                                }, 1000);
                            }, 1000);


                        },
                        error: function (xhr, status, error) {
                            // Handle error response (e.g., show an error message)
                            alert('Error: ' + error);
                        }
                    });
                } else {
                    $('#loginLoading').hide()
                    $('#btnLogin').show()
                }
            }, 3000);
        });
    });