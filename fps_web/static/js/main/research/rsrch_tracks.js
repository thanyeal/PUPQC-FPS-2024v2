$(document).ready(function () {
    var dataTable = $('#rsrch_dtble').DataTable({
        "processing": true,
        "searching": true,
        "paging": true,
        "lengthChange": true,
        "ordering": true,
        "ajax": {
            "url": "public_tb",
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
    });

    $('#searchAuthor, #searchTitle, #searchYear, #searchPublisher, #searchCategory, #searchAuthorType').on('keyup', function () {
        dataTable.column($(this).parent().index() + ':visible').search(this.value).draw();
    });

    if (dataTable.data().count() === 0) {
        $('#rsrch_dtble tbody').html('<tr><td colspan="9"><center>There is currently no data in the database.</center></td></tr>');
    }
});