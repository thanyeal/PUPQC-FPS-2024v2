
if (base_response == 0) {
    document.querySelector("#basic_radialbar").innerHTML = '<p class="text-center" style="margin: 19% 0% !important;">No data available.</p>';
}
else if (base_response == 1) {
    var percentage = specificYearData.percentage;

    var options = {
        series: [percentage],

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
        colors: [
            getComputedStyle(document.documentElement).getPropertyValue('--vz-info')
        ],
        plotOptions: { 
            radialBar: { hollow: { size: "80%" } } 
        },
        labels: ["Research Publications"],
    }
    var chart = new ApexCharts(document.querySelector("#basic_radialbar"), options);
    chart.render();
}