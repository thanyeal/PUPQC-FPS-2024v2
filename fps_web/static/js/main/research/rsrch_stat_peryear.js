
if (base_response == 0) {
    document.querySelector("#multiple_radialbar").innerHTML = '<p class="text-center" style="margin: 19% 0% !important;">No data available.</p>';
}
else if (base_response == 1) {
    var yearsz = [];
    var percentagesz = [];
    for (const year in GroupPercent) {
        yearsz.push(year);
        percentagesz.push(GroupPercent[year].percentage);
    }
    var options = {
        series: percentagesz,
        chart: { 
            height: 350,
            type: "radialBar",
            animations: {
                enabled: true,
                easing: 'easeinout',
                speed: 3000,
                animateGradually: {
                    enabled: true,
                    delay: 250
                },
                dynamicAnimation: {
                    enabled: true,
                    speed: 350
                }
            },
        },
        plotOptions: {
            radialBar: {
                dataLabels: {
                    name: { fontSize: "22px" },
                    value: { fontSize: "16px" },
                    total: {
                        show: true,
                        label: "Total",
                        formatter: function (a) {
                            return TotalResearch;
                        },
                    },
                },
            },
        },
        labels: yearsz,
        colors: [
            getComputedStyle(document.documentElement).getPropertyValue('--vz-info'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-secondary'),
        ],
    };
    var rsrch_bound_chart = new ApexCharts(document.querySelector("#multiple_radialbar"), options);
    rsrch_bound_chart.render();
}