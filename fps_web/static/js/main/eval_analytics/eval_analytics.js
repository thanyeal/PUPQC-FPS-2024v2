// Faculty Performance vs. Institutional Requirement Percentage
document.addEventListener("DOMContentLoaded", function () {

    //const json_data = JSON.parse('{{ overall_avg_data|escapejs }}');
    const valueToSet = json_data.overall_avg_first;
    const valueToSetTwo = json_data.overall_avg_second;

    const frfs = document.getElementById('frfs');
    frfs.textContent = valueToSet;

    const frss = document.getElementById('frss');
    frss.textContent = valueToSetTwo;
});


// Faculty Performance vs. Institutional Requirement
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
            zoom: { enabled: false },
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
            categories: [
                'Supervisor Evaluation',
                'Student Evaluation',
                'Peer Evaluation', 
                'Self Evaluation'
            ],
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

    var chartz = new ApexCharts(document.querySelector("#line-chart-two"), options);
    chartz.render();
}
initializeChartTwo();


// Trends in Teaching Effectiveness Over Time
var chartData = Object.values(combinedData);
var years = chartData.map(function (item) {
    return item.year;
});

var firstSemesterRatings = chartData.map(function (item) {
    return {
        'avg_stud_rating': item.first_semester_avg.avg_stud_rating,
    };
});

var secondSemesterRatings = chartData.map(function (item) {
    return {
        'avg_stud_rating': item.second_semester_avg.avg_stud_rating,
    };
});

var series = [
    {
        name: '1st Sem Students Rating',
        data: firstSemesterRatings.map(function (item) {
            return item.avg_stud_rating;
        }),
    },
    {
        name: '2nd Sem Students Rating',
        data: secondSemesterRatings.map(function (item) {
            return item.avg_stud_rating;
        }),
    },
];

var options = {
    chart: {
        type: 'bar',
        height: 350,
        zoom: { enabled: false },
        toolbar: { show: false },
    },
    plotOptions: {
        bar: {
            horizontal: false,
        },
    },
    colors: [
        getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
        getComputedStyle(document.documentElement).getPropertyValue('--vz-secondary'),
    ],
    xaxis: {
        categories: years,
        title: {
            text: 'Academic Year/s',
        },
    },
    yaxis: {
        title: {
            text: 'Average Rating',
        },
    },
    series: series, 
};

var chart = new ApexCharts(document.querySelector("#chartz"), options);
chart.render();


// Average Student Scores for Each Faculty 
var percentage_above_3 = percentage_data.pctg_ra3;
var percentage_below_3 = percentage_data.pctg_rb3;

var options = {
    series: [percentage_above_3, percentage_below_3],
    chart: {
        type: 'pie',
        height: '400px',
        width: '400px', 
    },
    labels: ['Above 4.0', 'Less/Equal  3.99'],
    colors: [
        getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
        getComputedStyle(document.documentElement).getPropertyValue('--vz-warning'),
    ],
};
var chart = new ApexCharts(document.querySelector("#prjects-status-1"), options);
chart.render();


// Average Student Scores for Each Faculty: Count
document.addEventListener("DOMContentLoaded", function () {

    const valueToSetThree = percentaging.count_ra3;
    const valueToSetFour  = percentaging.count_rb3;

    const ra3 = document.getElementById('ra3');
    ra3.textContent = valueToSetThree;

    const rb3 = document.getElementById('rb3');
    rb3.textContent = valueToSetFour;
});