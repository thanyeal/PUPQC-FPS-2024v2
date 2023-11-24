$(document).ready(function () {
    var tableTwo, tableThree;

    $.ajax({
        url: 'prodev_attendance',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            tableTwo = $('#prodev_dtble').DataTable({
                data: data.table_two_data,
                columns: [
                    { "data": "faculty_no" },
                    { "data": "training_title" },
                    { "data": "description" },
                    { "data": "training_date" },
                    { "data": "training_time" },
                    { "data": "duration" },
                    { "data": "location" },
                    {
                        "data": null,
                        "render": function (data, type, full, meta) {
                            return '<center><button type="button" class="btn btn-sm btn-primary attendees-btn" data-bs-toggle="modal" data-bs-target="#myannouncementModal">Attendees</button></center>';
                        }
                    }
                ]
            });

            tableThree = $('#prodev_dtble_modal').DataTable({
                data: data.table_three_data,
                columns: [
                    { "data": "faculty_name" },
                    { "data": "time_in" },
                    { "data": "time_out" },
                    { "data": "training_title" },
                ]
            });

            $('#prodev_dtble').on('click', '.attendees-btn', function () {
                var rowData = $(this).closest('tr');
                var data = tableTwo.row(rowData).data();
                var selectedTrainingTitle = data.training_title;
                tableThree.column(3).search(selectedTrainingTitle).draw();
            });
        }
    });
});