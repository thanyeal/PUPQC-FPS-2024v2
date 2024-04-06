$(document).ready(function () {
    $('#datatable').DataTable({
        "ajax": {
            "url": "eval_list",
            "dataSrc": ""
        },  
        "columns": [
            //{ "data": "faculty_num" },
            { "data": "Name" },
            { "data": "acad_head_ave" },
            { "data": "student_ave" },
            { "data": "peer_ave" },
            { "data": "self_ave" },
            //{ "data": "load_rating" },
            //{ "data": "load_interp" },
            //{ "data": "faculty_stat"},
            { "data": "semester" },
            { "data": "school_year" },
        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#datatable tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});