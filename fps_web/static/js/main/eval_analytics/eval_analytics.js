// Trends in Teaching Effectiveness Over Time
var chartStudRating = Object.values(combinedData);
var years = chartStudRating.map(item => item.year);

var firstSemesterRatings = chartStudRating.map(function (item) {
    return {
        'avg_stud_rating': item.first_semester_avg.avg_stud_rating,
    };
});

var secondSemesterRatings = chartStudRating.map(function (item) {
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
        getComputedStyle(document.documentElement).getPropertyValue('--vz-info'),
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

    // Populate the year dropdown
    var yearDropdown = document.getElementById('yearDropdown');
    
    // Add "Display All" option as the first option
    var allOption = document.createElement('option');
        allOption.value = "all";
        allOption.text = "Display All";
    yearDropdown.add(allOption);

    // Read the Json data for "Years"
    years.forEach( year => {
        var option = document.createElement('option');
            option.value = year;
            option.text = year
        yearDropdown.appendChild(option);
    });
        
    // Function to update the chart based on the selected year
    function updateChart() {
        var selectedYear = yearDropdown.value; 
        var filteredYearData = chartStudRating.filter(item => item.year == selectedYear);

        if (selectedYear === "all") {
            var filteredYearData = chartStudRating;
        }
        
        if (filteredYearData.length > 0) {
            var filteredSeries = [
                {
                    name: '1st Sem Students Rating',
                    data: filteredYearData.map(item => item.first_semester_avg.avg_stud_rating)
                },
                
                {
                    name: '2nd Sem Students Rating',
                    data: filteredYearData.map(item => item.second_semester_avg.avg_stud_rating)
                }
            ];
            chart.updateOptions({
                xaxis: {
                    categories: filteredYearData.map(item => item.year)
                }
            });
            chart.updateSeries(filteredSeries);
        }
        else {
            console.error('No data found for the selected year.');
        }
    } updateChart();
    
    yearDropdown.addEventListener('change', updateChart);



// Faculty Performance vs. Institutional Requirement Percentage
function initializeOverallAverageData () {
    document.addEventListener("DOMContentLoaded", function () {

        //const json_data = JSON.parse('{{ overall_avg_data|escapejs }}');
        const valueToSet = json_data.overall_avg_first;
        const valueToSetTwo = json_data.overall_avg_second;

        const frfs = document.getElementById('frfs');
        frfs.textContent = valueToSet;

        const frss = document.getElementById('frss');
        frss.textContent = valueToSetTwo;
    });
} initializeOverallAverageData ()

// Average Student Scores for Each Faculty
function initializePercentage () {
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
} initializePercentage ();

// Average Student Scores for Each Faculty: Count
function initializePercentCount () {
    document.addEventListener("DOMContentLoaded", function () {

        const valueToSetThree = percentaging.count_ra3;
        const valueToSetFour  = percentaging.count_rb3;

        const ra3 = document.getElementById('ra3');
        ra3.textContent = valueToSetThree;

        const rb3 = document.getElementById('rb3');
        rb3.textContent = valueToSetFour;
    });
}  initializePercentCount ()
