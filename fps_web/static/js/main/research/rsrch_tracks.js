$(document).ready(function () {
    $('#rsrch_dtble').DataTable({
        "ajax": {
            "url": "rsrch_tracking",
            "dataSrc": ""
        },
        "columns": [
            { "data": "rsrch_author" },
            { "data": "rsrch_title" },
            { "data": "rsrch_year" },
            { "data": "rsrch_publisher" }
        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#rsrch_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});