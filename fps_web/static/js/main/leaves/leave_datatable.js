$(document).ready(function () {
    $('#leave_dtble').DataTable({
        "ajax": {
            "url": "attendance_leaves",
            "dataSrc": ""
        },
        "columns": [
            { "data": "leave_faculty" },
            { "data": "leave_type" },
            { "data": "leave_start" },
            { "data": "leave_end" },
            { "data": "leave_duration" },
            { "data": "leave_status" }
        ],
        // "pageLength": 12,
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#leave_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});