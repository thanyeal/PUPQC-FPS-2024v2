$(document).ready(function () {
    $('#feedback_dtble').DataTable({
        "ajax": {
            "url": "fac_contents",
            "dataSrc": ""
        },
        "columns": [
            { "data": "eval_faculty" },
            { "data": "eval_type" },
            { "data": "eval_person" },
            { "data": "eval_score" },
            { "data": "eval_comms" }
        ],
        // "pageLength": 12,
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#feedback_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});