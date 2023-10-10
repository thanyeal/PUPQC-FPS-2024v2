$(document).ready(function () {
    $('#datatable').DataTable({
        "ajax": {
            "url": "eval_upload",
            "dataSrc": ""
        },
        "columns": [
            { "data": "faculty_num" },
            { "data": "facultyname" },
            { "data": "spvs_rating" },
            { "data": "spvs_interp" },
            { "data": "stud_rating" },
            { "data": "stud_interp" },
            { "data": "peer_rating" },
            { "data": "peer_interp" },
            { "data": "self_rating" },
            { "data": "self_interp" },
            //{ "data": "load_rating" },
            //{ "data": "load_interp" },
            //{ "data": "faculty_stat"},
            { "data": "semester" }
        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#datatable tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});