$(document).ready(function () {
    $('#workload_dtble').DataTable({
        "ajax": {
            "url": "workload_dat",
            "dataSrc": ""
        },
        "columns": [
            { "data": "workload_faculty" },
            { "data": "workload_semester" },
            { "data": "workload_course" },
            { "data": "workload_types" },
            { "data": "workload_duties" },
            { "data": "workload_total" }
        ],
        // "pageLength": 12,
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#workload_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});