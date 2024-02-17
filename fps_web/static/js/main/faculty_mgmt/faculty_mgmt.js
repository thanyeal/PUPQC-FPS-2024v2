function getCSRFToken() {
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    return csrfToken;
}

$(document).ready(function () {
    $('#fac_dtble').DataTable({
        "ajax": {
            "url": "mrt_promotion",
            "dataSrc": ""
        },
        "columns": [
            { "data": "merit_faculty_name" },
            { "data": "merit_faculty_status" },
            {
                "data": null,
                "render": function (data, type, full, meta) {
                    return '<center><button type="button" class="btn btn-sm btn-primary attendees-btn" data-bs-toggle="modal" data-bs-target="#faculty_mgmt_modal"  data-faculty-name="'+ full.merit_faculty_name + '">Performances</button></center>';
                }
            }
        ],
        "columnDefs": [
            { targets: [2], orderable: false }
        ]
    });
    if (dataTable.data().count() === 0) {
        $('#fac_dtble tbody').html('<tr><td colspan="9">There is currently no data in the database.</td></tr>');
    }
});


var faculty_chart;
var rsrch_chart;

$('#fac_dtble tbody').on('click', 'button.attendees-btn', function() {
    var clickedFacultyName = $(this).data('faculty-name');
    console.log('clicked: ', clickedFacultyName)

    $('.modal-content').hide();
    $('#chart-loader').show();

    $.ajax({
        url: "fac_mgmnt",
        type: "POST",
        data: {
            csrfmiddlewaretoken: getCSRFToken(),
            faculty_name: clickedFacultyName
        },

        success: function(response) {
            $('#chart-loader').fadeOut();
            $('.modal-content').show();

            var test_data = response.faculty_mgmt
            console.log(test_data);

            if ($.isEmptyObject(test_data)) {
                $('#param_content .luh, #param_content2 .luh2').html   (`
                    <div class="modal-body text-center p-5">
                        <lord-icon src="https://cdn.lordicon.com/tdrtiskw.json" trigger="loop" colors="primary:#e76f2e,secondary:#346cbe" style="width:130px;height:130px">
                        </lord-icon>
                        <div class="mt-4 pt-4">
                            <h4>Uh oh, something went wrong!</h4>
                            <p class="text-muted"> The performance analytics of this user for this section is currently unavailable.</p>
                        </div>
                    </div>
                `);
            }
            else {

                function FacultyPerformance() {
                    var faculty_dataa = response.faculty_mgmt;
                    var semesterData = [
                        {
                            name: 'First Semester',
                            data: [
                                faculty_dataa.Supervisor_First[0],
                                faculty_dataa.Student_First[0],
                                faculty_dataa.Peer_First[0],
                                faculty_dataa.Self_First[0]
                            ]
                        },
                        {
                            name: 'Second Semester',
                            data: [
                                faculty_dataa.Supervisor_Second[0],
                                faculty_dataa.Student_Second[0],
                                faculty_dataa.Peer_Second[0],
                                faculty_dataa.Self_Second[0]
                            ]
                        },
                    ];
                    var options = {
                        chart: {
                            type: 'bar',
                            height: 345,
                            zoom: { enabled: true },
                            toolbar: { show: false },
                        },
    
                        plotOptions: {
                            bar: {
                                horizontal: false,
                                columnWidth: '60%',
                                endingShape: 'rounded',
                            },
                        },
    
                        colors: [
                            getComputedStyle(document.documentElement).getPropertyValue('--vz-info'),
                            getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
                            getComputedStyle(document.documentElement).getPropertyValue('--vz-secondary')
                        ],
    
                        xaxis: {
                            categories: ['Supervisor Evaluation', 'Student Evaluation', 'Peer Evaluation', 'Self Evaluation'],
                            title: {
                                text: 'Rating',
                            },
                        },
    
                        yaxis: {
                            title: {
                                text: 'Evaluation Scores',
                            },
                        },
                        
                        series: semesterData,
                    };
                    if (faculty_chart) {
                        faculty_chart.destroy();
                        faculty_chart = new ApexCharts(document.querySelector("#faculty-mgmt-chart"), options);
                        faculty_chart.render();
                    } else {
                        faculty_chart = new ApexCharts(document.querySelector("#faculty-mgmt-chart"), options);
                        faculty_chart.render();
                    }
                } FacultyPerformance();

                function ResearchPerformance() {
                    var f_research_data = response.publication_counts;
                    var years = Object.keys(f_research_data);
                    var counts = years.map(year => f_research_data[year].count);
                    var options = {
                        chart: {
                            height: 380,
                            type: "bar",
                            zoom: { enabled: false },
                            toolbar: { show: false },
                        },
                        
                        colors: [
                            getComputedStyle(document.documentElement).getPropertyValue('--vz-info'),
                            getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
                            getComputedStyle(document.documentElement).getPropertyValue('--vz-secondary'),
                        ],
                        
                        dataLabels: {
                            enabled: !1
                        },
    
                        stroke: {
                            width: [3, 3],
                            curve: "straight"
                        },
    
                        series: [
                            {
                                name: 'No. of Research Published',
                                data: counts
                            },
                        ],
    
                        grid: {
                            row: { colors: ["transparent", "transparent"], opacity: 0.2 },
                            borderColor: "#f1f1f1",
                        },
    
                        markers: {
                            style: "inverted",
                            size: 6
                        },
    
                        xaxis: {
                            categories: years,
                            title: { text: "Academic Year" },
                        },
    
                        yaxis: {
                            title: {
                                text: "Research Count"
                            },
                            min: 0,
                            max: 10
                        },
    
                        legend: {
                            position: "top",
                            horizontalAlign: "right",
                            floating: !0,
                            offsetY: -25,
                            offsetX: -5,
                        },
    
                        responsive: [
                            {
                                breakpoint: 600,
                                options: { chart: { toolbar: { show: !1 } }, legend: { show: !1 } },
                            },
                        ],
                    }
                    if (rsrch_chart) {
                        rsrch_chart.destroy();
                        rsrch_chart = new ApexCharts(document.querySelector("#rsrch_performance"), options);
                        rsrch_chart.render();
                    } else {
                        rsrch_chart = new ApexCharts(document.querySelector("#rsrch_performance"), options);
                        rsrch_chart.render();
                    }
                } ResearchPerformance();
            }

            $('#chart-loader').hide();
        },
        error: function(error) {
            $('#faculty-mgmt-chart').html('<p>An error occurred while fetching data. Please try again later.</p>');

        }
    });
        
    $('#param_content .luh, #param_content2 .luh2').empty();
    $('#faculty_mgmt_modal').on('hidden.bs.modal', function () {    
        if (faculty_chart) {
            faculty_chart.destroy();
        }

        if (rsrch_chart) {
            rsrch_chart.destroy();
        }
    });
    
});
