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
            {
                "data": null,
                "render": function (data, type, full, meta) {
                    return '<center><button type="button" class="btn btn-sm btn-primary attendees-btn">Performances</button></center>';
                }
            }
        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#merit_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});
