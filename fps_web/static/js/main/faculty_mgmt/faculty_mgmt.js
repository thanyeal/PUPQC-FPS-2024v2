function getCSRFToken() {
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    return csrfToken;
}
$(document).ready(function () {
    var dataTable = $('#fac_dtble').DataTable({
        "processing": true,
        "searching": true,
        "paging": true,
        "lengthChange": true,
        "ordering": true,
        "ajax": {
            "url": "faculty_info",
            "dataSrc": ""
        },
        "columns": [
            { "data": "Faculty_name" },
            { "data": "Faculty_type" },
            { "data": "Faculty_rank" },
            {
                "data": null,
                "render": function (data, type, full, meta) {
                    return  '<center>' + '<button type="button" style="margin-right:10px !important;" class="btn btn-sm btn-primary attendees-btn" data-bs-toggle="modal" data-bs-target="#faculty_mgmt_modal"  data-faculty-name="'+ full.Faculty_name + '">Performances</button>' + '<button type="button" class="btn btn-sm btn-danger reports-btn" data-bs-toggle="" data-bs-target="#"  data-faculty-name="'+ full.Faculty_name + '">Reports</button>' + '</center>'; 
                }
            }
        ],
        "columnDefs": [
            { targets: [3], orderable: false }
        ]
    });

    $('#searchName, #searchType, #searchRank').on('keyup', function () {
        dataTable.column($(this).parent().index() + ':visible').search(this.value).draw();
    });

    if (dataTable.data().count() === 0) {
        $('#fac_dtble tbody').html('<tr><td colspan="9"><center>There is currently no data in the database.</center></td></tr>');
    }
});



var faculty_chart;
var rsrch_chart;
var ovc_chart;

$('#fac_dtble tbody').on('click', 'button.attendees-btn', function() {
    var clickedFacultyName = $(this).data('faculty-name');

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
            //console.log(response)
            $('#chart-loader').fadeOut();
            $('.modal-content').show();

            var test_data = response.faculty_mgmt;
            // console.log(test_data);

            var test_datz = response.publication_counts;
            // console.log(test_datz);

            var test_overall = response.overall;
            // console.log(test_overall);

            var thefaculty = response.the_faculty;
            // console.log(thefaculty);

            var theprogress = response.the_progress;
            // console.log(theprogress);

            if ($.isEmptyObject(test_data)) {
                $('#param_content .luh').html   (`
                    <div class="modal-body text-center p-5">
                        <lord-icon src="https://cdn.lordicon.com/tdrtiskw.json" trigger="loop" colors="primary:#e76f2e,secondary:#346cbe" style="width:130px;height:130px">
                        </lord-icon>
                        <div class="mt-4 pt-4">
                            <h4>Uh oh, something went wrong!</h4>
                            <p class="text-muted"> The performance analytics of this user for Evaluation Performance is currently unavailable.</p>
                        </div>
                    </div>
                `);
            }

            if ($.isEmptyObject(test_datz)) {
                $('#param_content2 .luh2').html   (`
                    <div class="modal-body text-center p-5">
                        <lord-icon src="https://cdn.lordicon.com/tdrtiskw.json" trigger="loop" colors="primary:#e76f2e,secondary:#346cbe" style="width:130px;height:130px">
                        </lord-icon>
                        <div class="mt-4 pt-4">
                            <h4>Uh oh, something went wrong!</h4>
                            <p class="text-muted"> The performance analytics of this user for Research Performance is currently unavailable.</p>
                        </div>
                    </div>
                `);
            }

            if ($.isEmptyObject(test_overall)) {
                $('#param_content3 .luh3').html   (`
                    <div class="modal-body text-center p-5">
                        <lord-icon src="https://cdn.lordicon.com/tdrtiskw.json" trigger="loop" colors="primary:#e76f2e,secondary:#346cbe" style="width:130px;height:130px">
                        </lord-icon>
                        <div class="mt-4 pt-4">
                            <h4>Uh oh, something went wrong!</h4>
                            <p class="text-muted"> The performance analytics of this user for Overall Evaluation Performance is currently unavailable.</p>
                        </div>
                    </div>
                `);
            }

            if (theprogress && theprogress.overall_percent) {
                var overallPercentage = theprogress.overall_percent;

                $('#progress-bar').css('width', overallPercentage + '%');
                $('#progress-bar .label').text(overallPercentage + '%');
                $('#progress-bar').attr('aria-valuenow', overallPercentage);
            }
            else {
                var overallPercentage = 0;

                $('#progress-bar').css('width', overallPercentage + '%');
                $('#progress-bar .label').text(overallPercentage + '%');
                $('#progress-bar').attr('aria-valuenow', overallPercentage);
            }

            function updateFacultyInfo() {
                var indiv_information = response.the_faculty;
                if (indiv_information != null) {
                    document.getElementById('facultyName').textContent = indiv_information.faculty_name || "Information not available";
                    document.getElementById('facultyType').textContent = indiv_information.faculty_type || "Information not available";
                    document.getElementById('facultyAddr').textContent = indiv_information.faculty_addr || "Information not available";
                    document.getElementById('facultyMail').textContent = indiv_information.faculty_mail || "Information not available";
                    document.getElementById('facultyNumb').textContent = indiv_information.faculty_numb || "Information not available";
                    document.getElementById('facultyDegr').textContent = indiv_information.faculty_degr || "Information not available";
                }
                else {
                    document.getElementById('facultyName').textContent = "Information not available";
                    document.getElementById('facultyType').textContent = "Information not available";
                    document.getElementById('facultyAddr').textContent = "Information not available";
                    document.getElementById('facultyMail').textContent = "Information not available";
                    document.getElementById('facultyNumb').textContent = "Information not available";
                    document.getElementById('facultyDegr').textContent = "Information not available";
                }
            }   updateFacultyInfo();

            function FacultyOverall(response) {
                var overall_data = response.overall;
                var overall_years = Object.keys(overall_data);
                
                var semData = [
                    {
                        name: 'First Semester',
                        data: [
                            overall_data[overall_years[0]].first_sem_rating.acadhead_rating,
                            overall_data[overall_years[0]].first_sem_rating.individs_rating,
                            overall_data[overall_years[0]].first_sem_rating.director_rating,
                            overall_data[overall_years[0]].first_sem_rating.students_rating
                        ]
                    },
                    {
                        name: 'Second Semester',
                        data: [
                            overall_data[overall_years[0]].second_sem_rating.acadhead_rating,
                            overall_data[overall_years[0]].second_sem_rating.individs_rating,
                            overall_data[overall_years[0]].second_sem_rating.director_rating,
                            overall_data[overall_years[0]].second_sem_rating.students_rating
                        ]
                    },
                ];
            
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
            
                    stroke: {
                        width: [3, 3],
                        curve: "straight"
                    },
                    
                    series: semData,
            
                    xaxis: {
                        categories: ['Academic Head Rating', 'Self Rating', 'Director Rating', 'Student Rating'],
                        title: { text: "Categories" },
                    },
            
                    yaxis: {
                        title: {
                            text: "Rating"
                        }
                    },
                };

                if (ovc_chart) {
                    ovc_chart.destroy();
                    ovc_chart = new ApexCharts(document.querySelector("#faculty_overall"), options);
                    ovc_chart.render();
                } else {
                    ovc_chart = new ApexCharts(document.querySelector("#faculty_overall"), options);
                    ovc_chart.render();
                };

                var year_drop = document.getElementById('yeardrop_per_rating');
                year_drop.innerHTML = '';
                overall_years.forEach(overall_years => {
                    var ent_options = document.createElement('option');
                    ent_options.value = overall_years;
                    ent_options.text = overall_years;
                    year_drop.add(ent_options);
                });
            
                year_drop.addEventListener('change', function (event) {
                    event.preventDefault();
                    event.stopPropagation();
                    var selectedYear = this.value;
                    filterDataByYear(selectedYear);
                });
                
            
                function filterDataByYear(selectedYear) {
                    var semData = [
                        {
                            name: 'First Semester',
                            data: [
                                overall_data[selectedYear].first_sem_rating.acadhead_rating,
                                overall_data[selectedYear].first_sem_rating.individs_rating,
                                overall_data[selectedYear].first_sem_rating.director_rating,
                                overall_data[selectedYear].first_sem_rating.students_rating
                            ]
                        },
                        {
                            name: 'Second Semester',
                            data: [
                                overall_data[selectedYear].second_sem_rating.acadhead_rating,
                                overall_data[selectedYear].second_sem_rating.individs_rating,
                                overall_data[selectedYear].second_sem_rating.director_rating,
                                overall_data[selectedYear].second_sem_rating.students_rating
                            ]
                        },
                    ];
        
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
        
                        stroke: {
                            width: [3, 3],
                            curve: "straight"
                        },
                        
                        series: semData,
        
                        xaxis: {
                            categories: ['Academic Head Rating', 'Self Rating', 'Director Rating', 'Student Rating'],
                            title: { text: "Categories" },
                        },
        
                        yaxis: {
                            title: {
                                text: "Rating"
                            }
                        },
                    }
                    if (ovc_chart) {
                        ovc_chart.destroy();
                        ovc_chart = new ApexCharts(document.querySelector("#faculty_overall"), options);
                        ovc_chart.render();
                    } else {
                        ovc_chart = new ApexCharts(document.querySelector("#faculty_overall"), options);
                        ovc_chart.render();
                    }
                }
            } FacultyOverall(response);

            function FacultyPerformance() {

                var faculty_dataa = response.faculty_mgmt;
                var isFirstSemesterAvailable  = faculty_dataa.Supervisor_First  && faculty_dataa.Student_First  && faculty_dataa.Director_First  && faculty_dataa.Self_First;
                var isSecondSemesterAvailable = faculty_dataa.Supervisor_Second && faculty_dataa.Student_Second && faculty_dataa.Director_Second && faculty_dataa.Self_Second;

                var semesterData = [];
                if (isFirstSemesterAvailable) {
                    semesterData.push({
                        name: 'First Semester',
                        data: [
                            faculty_dataa.Supervisor_First[0],
                            faculty_dataa.Student_First[0],
                            faculty_dataa.Director_First[0],
                            faculty_dataa.Self_First[0]
                        ]
                    });
                }
                if (isSecondSemesterAvailable) {
                    semesterData.push({
                        name: 'Second Semester',
                        data: [
                            faculty_dataa.Supervisor_Second[0],
                            faculty_dataa.Student_Second[0],
                            faculty_dataa.Director_Second[0],
                            faculty_dataa.Self_Second[0]
                        ]
                    });
                };

                var options = {
                    chart: {
                        type: 'bar',
                        height: 345,
                        zoom: { enabled: true },
                        toolbar: { show: false },
                    },

                    plotOptions: {
                        bar: {
                            horizontal: true,
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
                        categories: ['Supervisor', 'Student', 'Director', 'Self'],
                        title: {
                            text: 'Rating Based Percentage',
                        },
                    },

                    yaxis: {
                        title: {
                            text: 'Evaluations',
                        },
                        max: 100,
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
                var entr_year_sum = Object.keys(f_research_data);
                var counts = entr_year_sum.map(year => f_research_data[year].count);
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
                        categories: entr_year_sum,
                        title: { text: "Academic Year" },
                    },

                    yaxis: {
                        title: {
                            text: "Research Count"
                        },
                        max: 5
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

            $('#chart-loader').hide();
        },

        error: function(error) {
            console.error("Error fetching data:", error);
            $('#faculty-mgmt-chart').html('<p>An error occurred while fetching data. Please try again later.</p>');
            $('#faculty_overall').html('<p>An error occurred while fetching data. Please try again later.</p>');
            $('#rsrch_performance').html('<p>An error occurred while fetching data. Please try again later.</p>');

        }
    });
        
    $('#param_content .luh, #param_content2 .luh2, #param_content3 .luh3').empty();
    $('#faculty_mgmt_modal').on('hidden.bs.modal', function () {    
        if (faculty_chart) {
            faculty_chart.destroy();
        }

        if (rsrch_chart) {
            rsrch_chart.destroy();
        }

        if (ovc_chart) {
            ovc_chart.destroy();
        }
    });
    
});

$('#fac_dtble tbody').on('click', 'button.reports-btn', function() {
    var clickedFacultyName = $(this).data('faculty-name');
    $.ajax({
        url: "faculty_mgmt_reports",
        type: "POST",
        data: {
            csrfmiddlewaretoken: getCSRFToken(),
            faculty_name: clickedFacultyName
        },
        xhrFields: {
            responseType: 'blob'
        },
        success: function(response, status, xhr) {
            var filename = "";
            var disposition = xhr.getResponseHeader('Content-Disposition');
            if (disposition && disposition.indexOf('attachment') !== -1) {
                var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                var matches = filenameRegex.exec(disposition);
                if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, '');
            }
            var blob = new Blob([response], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = filename || 'testtest.xlsx';
            link.click();
        },
        error: function(error) {
            console.log("Oops, something went wrong.");
        }
    });
});
