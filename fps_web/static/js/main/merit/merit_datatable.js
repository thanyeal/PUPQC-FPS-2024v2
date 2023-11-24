$(document).ready(function () {
    $('#merit_dtble').DataTable({
        "ajax": {
            "url": "mrt_promotion",
            "dataSrc": ""
        },
        "columns": [
            { "data": "merit_faculty_name" },
            { "data": "merit_faculty_status" },
            { "data": "merit_ave_dept_rate" },
            { "data": "merit_rsrch_publish" },
            { "data": "merit_training_attended" },
            { "data": "merit_promotion" },
        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#merit_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});

$(document).ready(function() {
    // Click event on faculty list items
    $(document).on('click', '.candidate-list-item', function(e) {
        e.preventDefault();

        var candidateName = $(this).find('.candidate-name').text();
        var candidatePosition = $(this).find('.candidate-position').text();

        // Remove existing details on the right side
        $('.promoting').remove();

        // Create and append new details for the clicked candidate
        var detailsContainer = $('<div>', {
            'class': 'promoting',
            'style': 'text-align: center !important;'
        });

        var name = $('<h5>', {
            'class': 'mb-0'
            
        }).text(candidateName);

        var position = $('<p>', {
            'class': 'text-muted'
        }).text(candidatePosition);

        detailsContainer.append(name).append(position);
        $('.col-lg-6:last').append(detailsContainer); // Appending to the last column (right side)
    });

    // Fetch data and populate the left side candidate list
    $.ajax({
        url: 'mrt_promotion',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if (data) {
                var candidateList = $('#candidate-list');

                $.each(data, function(index, item) {
                    var li = $('<li>', {
                        'class': 'candidate-list-item'
                    });

                    var a = $('<a>', {
                        'href': '#', 'class': 'd-flex align-items-center py-2'
                    });

                    var div1 = $('<div>', {
                        'class': 'flex-shrink-0 me-2'
                    }).html('<div class="avatar-xs"><img src="https://lh3.googleusercontent.com/a/default-user=s75-c" alt="" class="img-fluid rounded-circle candidate-img"></div>');

                    var div2 = $('<div>', {
                        'class': 'flex-grow-1', 'style': 'margin: 10px 0px;'
                    }).html('<h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">' + item.merit_faculty_name + '</span></h5><div class="candidate-position" style="color: gray;">' + item.merit_faculty_status + '</div>');

                    a.append(div1).append(div2);
                    li.append(a);
                    candidateList.append(li);
                });
            }
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
});

$(document).ready(function() {
    document.getElementById("sa-warningz").addEventListener("click", function () {
        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonClass: 'btn btn-primary w-xs me-2 mt-2',
            cancelButtonClass: 'btn btn-danger w-xs mt-2',
            confirmButtonText: 'Yes',
            buttonsStyling: false,
            showCloseButton: true,
        }).then(function(result) {
            // On 'Yes' click in the confirmation modal
            if (result.value) {
                // Fetch faculty name from the right side of the HTML
                var facultyName = $('#candidate-name').text().trim();

                // Display a modal with the faculty name and promotion/demotion status
                Swal.fire({
                    title: facultyName + ' is successfully promoted!', // Corrected the concatenation here
                    icon: 'success',
                    confirmButtonClass: 'btn btn-primary w-xs mt-2',
                    buttonsStyling: false,
                });

                // Log 'TRUE' in the console for promotion or 'FALSE' for demotion
                // This is a placeholder, you'll replace it with the actual logic
                console.log(true); // Changed TRUE to true

                // Change the button span text from 'Promote' to 'Demote'
                $('#sa-warningz .icon-on').html('<i class="ri-user-unfollow-line align-bottom me-1"></i>Demote');
            }
        });
    });
});
