$(document).ready(function () {
    $('#datatable').DataTable({
        "ajax": {
            "url": "eval_upload",  // Use the URL associated with your view
            "dataSrc": ""
        },
        "columns": [
            { "data": "facultyname" },
            { "data": "spvs_rating" },
            { "data": "spvs_interp" },
            { "data": "stud_rating" },
            { "data": "stud_interp" },
            { "data": "peer_rating" },
            { "data": "peer_interp" },
            { "data": "self_rating" },
            { "data": "self_interp" },
            { "data": "semester" }
        ],
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        // Replace the table body with the message
        $('#datatable tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});e