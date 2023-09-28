$(document).ready(function () {
    $('#AvestudRate').DataTable({
        "ajax": {
            "url": "eval_analytics",  // Use the URL associated with your view
            "dataSrc": ""
        },
        "columns": [
            { "data": "facultyname" },
            { "data": "stud_rating" },
            { "data": "stud_interp" },
            { "data": "semester" },
        ]
    });

    if (dataTable.data().count() === 0) {
        $('#AvestudRate tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});