
$(document).ready(function () {
    var dataTable = $('#prodev_table_programs').DataTable({
        "processing": true,
        "searching": true,
        "paging": true,
        "lengthChange": true,
        "ordering": true,
        "ajax": {
            "url": "prodev_attendance",
            "dataSrc": ""
        },
        "columns": [
            { "data": "Program_Title" },
            { "data": "Program_Start" },
            { "data": "Program_End" },
            { "data": "Program_Speaker" },
            { "data": "Program_Type" }
        ],
        "columnDefs": [
            { targets: [4], orderable: false }
        ]
    });

    $('#searchTitle, #searchStart, #searchEnd, #searcherSpeaker, #searchType').on('keyup', function () {
        dataTable.column($(this).parent().index() + ':visible').search(this.value).draw();
    });

    if (dataTable.data().count() === 0) {
        $('#prodev_table_programs tbody').html('<tr><td colspan="9"><center>There is currently no data in the database.</center></td></tr>');
    }
});
