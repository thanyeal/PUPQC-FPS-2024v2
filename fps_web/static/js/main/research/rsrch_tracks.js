$(document).ready(function () {
    $('#rsrch_dtble').DataTable({
        "ajax": {
            "url": "rsrch_tracking",
            "dataSrc": ""
        },
        "columns": [
            { "data": "Author" },
            { "data": "Research Title" },
            { "data": "Publication Year" },
            { "data": "Publisher" },
            { "data": "Category" },
            { "data": "Author Type" }

        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#rsrch_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});