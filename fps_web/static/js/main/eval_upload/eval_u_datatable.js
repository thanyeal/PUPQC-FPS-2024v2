$(document).ready(function () {
    $('#datatable').DataTable({
        "ajax": {
            "url": "eval_upload",
            "dataSrc": ""
        },
        "columns": [
            //{ "data": "faculty_num" },
            { "data": "FacultyName" },
            { "data": "Supervisor Rating" },
            { "data": "Supervisor Interpretation" },
            { "data": "Students Rating" },
            { "data": "Students Interpretation" },
            { "data": "Peer Rating" },
            { "data": "Peer Interpretation" },
            { "data": "Self Rating" },
            { "data": "Self Interpretation" },
            //{ "data": "load_rating" },
            //{ "data": "load_interp" },
            //{ "data": "faculty_stat"},
            { "data": "Semester" },
            { "data": "Year" },
        ]
        //"pageLength": 25
    });

    // Check if the table has no data
    if (dataTable.data().count() === 0) {
        $('#datatable tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});