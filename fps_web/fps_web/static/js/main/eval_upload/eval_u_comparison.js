var chartDataTwo = JSON.parse('{{ chart_data_two|escapejs|safe }}');

function initializeChartTwo() {
    var semesterData = [
        {
            name: 'Institutional Average Rating',
            data: [4.9, 4.9, 4.9, 4.9],
        },
        {
            name: 'First Sem',
            data: [
                chartDataTwo.spvs_first[0],
                chartDataTwo.stud_first[0],
                chartDataTwo.peerr_first[0],
                chartDataTwo.selff_first[0]
            ]
        },
        {
            name: 'Second Sem',
            data: [
                chartDataTwo.spvs_second[0],
                chartDataTwo.stud_second[0],
                chartDataTwo.peerr_second[0],
                chartDataTwo.selff_second[0]
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
            getComputedStyle(document.documentElement).getPropertyValue('--vz-warning'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-success')
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

    var chart = new ApexCharts(document.querySelector("#eval_perf_inst"), options);
    chart.render();
}

initializeChartTwo();