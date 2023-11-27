$(document).ready(function () {
    $('#recog_dtble').DataTable({
        "ajax": {
            "url": "awards_recog",
            "dataSrc": ""
        },
        "columns": [
            { "data": "awards_faculty" },
            { "data": "awards_title" }  ,
            { "data": "awards_date" }   ,
            { "data": "awards_type" }   ,
            { "data": "awards_status" }
        ],
        // "pageLength": 12,
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#recog_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});