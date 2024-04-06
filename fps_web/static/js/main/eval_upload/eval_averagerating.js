
var chartData= Object.values(chartDataTwo);
var yearForEval = chartData.map(item => item.year);


var frstSemesterRatings = chartData.map(function (item) {
    return {
        'avgz_spvs_rating': item.frst_semester_avg.avgz_spvs_rating,
        'avgz_stud_rating': item.frst_semester_avg.avgz_stud_rating,
        'avgz_peer_rating': item.frst_semester_avg.avgz_peer_rating,
        'avgz_self_rating': item.frst_semester_avg.avgz_self_rating,
    };
});

var scndSemesterRatings = chartData.map(function (item) {
    return {
        'avgz_spvs_rating': item.scnd_semester_avg.avgz_spvs_rating,
        'avgz_stud_rating': item.scnd_semester_avg.avgz_stud_rating,
        'avgz_peer_rating': item.scnd_semester_avg.avgz_peer_rating,
        'avgz_self_rating': item.scnd_semester_avg.avgz_self_rating,
    };
});

var summmerSemesterRatings = chartData.map(function (item) {
    return {
        'avgz_spvs_rating': item.summer_semester_avg.avgz_spvs_rating,
        'avgz_stud_rating': item.summer_semester_avg.avgz_stud_rating,
        'avgz_peer_rating': item.summer_semester_avg.avgz_peer_rating,
        'avgz_self_rating': item.summer_semester_avg.avgz_self_rating,
    };
});

var series = [

    {
        name: '1st Sem Supervisor Rating',
        data: frstSemesterRatings.map(function (item) {
            return item.avgz_spvs_rating;
        }),
    },

    {
        name: '1st Sem Student Rating',
        data: frstSemesterRatings.map(function (item) {
            return item.avgz_stud_rating;
        }),
    },

    {
        name: '1st Sem Peer Rating',
        data: frstSemesterRatings.map(function (item) {
            return item.avgz_peer_rating;
        }),
    },

    {
        name: '1st Sem Self Rating',
        data: frstSemesterRatings.map(function (item) {
            return item.avgz_self_rating;
        }),
    },

    {
        name: '2nd Sem Supervisor Rating',
        data: scndSemesterRatings.map(function (item) {
            return item.avgz_spvs_rating;
        }),
    },

    {
        name: '2nd Sem Student Rating',
        data: scndSemesterRatings.map(function (item) {
            return item.avgz_stud_rating;
        }),
    },

    {
        name: '2nd Sem Peer Rating',
        data: scndSemesterRatings.map(function (item) {
            return item.avgz_peer_rating;
        }),
    },

    {
        name: '2nd Sem Self Rating',
        data: scndSemesterRatings.map(function (item) {
            return item.avgz_self_rating;
        }),
    },

    {
        name: 'Summer Semester Supervisor Rating',
        data: summmerSemesterRatings.map(function (item) {
            return item.avgz_spvs_rating;
        }),
    },

    {
        name: 'Summer Student Rating',
        data: summmerSemesterRatings.map(function (item) {
            return item.avgz_stud_rating;
        }),
    },

    {
        name: 'Summer Semester Peer Rating',
        data: summmerSemesterRatings.map(function (item) {
            return item.avgz_peer_rating;
        }),
    },

    {
        name: 'Summer Semester Self Rating',
        data: summmerSemesterRatings.map(function (item) {
            return item.avgz_self_rating;
        }),
    },
];

var options = {
    chart: {
        type: 'bar',
        height: 350,
        zoom: { enabled: false },
        toolbar: { show: false },
        animations: {
            enabled: true,
            easing: 'easeinout',
            speed: 1000,
            animateGradually: {
                enabled: true,
                delay: 150
            },
            dynamicAnimation: {
                enabled: true,
                speed: 350
            }
        },
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
        getComputedStyle(document.documentElement).getPropertyValue('--vz-dark'),
    ],
    xaxis: {
        categories: yearForEval,
        title: {
            text: 'Academic Year/s',
        },
    },
    yaxis: {
        title: {
            text: 'Average Rating',
        },
        max: 5
    },
    series: series,
};

var chartz = new ApexCharts(document.querySelector("#line-chart-two"), options);

if (chartz == null) {
    document.querySelector("#line-chart-two").innerHTML = '<p class="text-center" style="margin-top: 5% !important;">No data available.</p>';
}
else {
    chartz.render();

    var yearDropdownForEval = document.getElementById('yearDropdownForEval');
        
    var allOptionForEval = document.createElement('option');
        allOptionForEval.value = "all";
        allOptionForEval.text = "Display All";
    yearDropdownForEval.add(allOptionForEval);

    yearForEval.forEach( yearForEval => {
        var optionForEval = document.createElement('option');
            optionForEval.value = yearForEval;
            optionForEval.text = yearForEval;
        yearDropdownForEval.appendChild(optionForEval);
    });

    function updateEvaluationz(event) {
        if (event) {
            event.preventDefault();
        }
        var selectedYearForEval = yearDropdownForEval.value;
        var filteredYearDataForEval = chartData.filter(item => item.year == selectedYearForEval);
        
        if (selectedYearForEval == "all") {
            var filteredYearDataForEval = chartData;
        }
        
        if (filteredYearDataForEval.length > 0) {
            var filteredSeriesForEval = [
                //++++++++
                {
                    name: '1st Sem Supervisor Rating',
                    data: filteredYearDataForEval.map(item => item.frst_semester_avg.avgz_spvs_rating)
                },
                
                {
                    name: '1st Sem Student Rating',
                    data: filteredYearDataForEval.map(item => item.frst_semester_avg.avgz_stud_rating)
                },
                {
                    name: '1st Sem Peer Rating',
                    data: filteredYearDataForEval.map(item => item.frst_semester_avg.avgz_peer_rating)
                },
                
                {
                    name: '1st Sem Self Rating',
                    data: filteredYearDataForEval.map(item => item.frst_semester_avg.avgz_self_rating)
                },
                //++++++++
                {
                    name: '2nd Sem Supervisor Rating',
                    data: filteredYearDataForEval.map(item => item.scnd_semester_avg.avgz_spvs_rating)
                },
                
                {
                    name: '2nd Sem Student Rating',
                    data: filteredYearDataForEval.map(item => item.scnd_semester_avg.avgz_stud_rating)
                },
                {
                    name: '2nd Sem Peer Rating',
                    data: filteredYearDataForEval.map(item => item.scnd_semester_avg.avgz_peer_rating)
                },
                
                {
                    name: '2nd Sem Self Rating',
                    data: filteredYearDataForEval.map(item => item.scnd_semester_avg.avgz_self_rating)
                },
                //+++++++++
                {
                    name: 'Summer Sem Supervisor Rating',
                    data: filteredYearDataForEval.map(item => item.summer_semester_avg.avgz_spvs_rating)
                },
                
                {
                    name: 'Summer Sem Student Rating',
                    data: filteredYearDataForEval.map(item => item.summer_semester_avg.avgz_stud_rating)
                },
                {
                    name: 'Summer Sem Peer Rating',
                    data: filteredYearDataForEval.map(item => item.summer_semester_avg.avgz_peer_rating)
                },
                
                {
                    name: 'Summer Sem Self Rating',
                    data: filteredYearDataForEval.map(item => item.summer_semester_avg.avgz_self_rating)
                },

            ];
            
            chartz.updateOptions({
                xaxis: {
                    categories: filteredYearDataForEval.map(item => item.year)
                }
                
            });
            chartz.updateSeries(filteredSeriesForEval);
        }
        else {
            console.error('No data found for the selected year.');
        }
    }
    
    var yearDropdownForEval = document.getElementById('yearDropdownForEval');
    yearDropdownForEval.addEventListener('change', updateEvaluationz);

}
