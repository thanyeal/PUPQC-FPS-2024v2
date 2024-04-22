$(document).ready(function () {
    var dataTable = $('#datatable').DataTable({
        "processing": true,
        "searching": true,
        "paging": true,
        "lengthChange": true,
        "ordering": true,
        "ajax": {
            "url": "evales_em",
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
    });

    $('#searchFaculty, #searchSvRating, #searchStRating, #searchPeerRating, #searchSelfRating, #searchSemesters, #searchAcadYear').on('keyup', function () {
        dataTable.column($(this).parent().index() + ':visible').search(this.value).draw();
    });

    if (dataTable.data().count() === 0) {
        $('#datatable tbody').html('<tr><td colspan="9"><center>There is currently no data in the database.</center></td></tr>');
    }
});