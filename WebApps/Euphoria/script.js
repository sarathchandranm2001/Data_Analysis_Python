$(document).ready(function() {
    $('#registrationForm').on('submit', function(e) {
        e.preventDefault();

        var formData = {
            'entry.2098250331': $('#name').val(),
            'entry.1567800022': $('#email').val(),
            'entry.2112353005': $('#phone').val()
        };

        $.ajax({
            url: 'https://docs.google.com/forms/d/e/1FAIpQLSfLZHK_PFcTIx_7upzyxxR92GIPPRbTDqgNMwYNT_ANxbb2UA/formResponse',
            type: 'POST',
            data: formData,
            dataType: 'xml',
            success: function() {
                $('#successMessage').show();
                $('#registrationForm').trigger('reset');
            },
            error: function() {
                alert('There was an error submitting the form. Please try again.');
            }
        });
    });
});
