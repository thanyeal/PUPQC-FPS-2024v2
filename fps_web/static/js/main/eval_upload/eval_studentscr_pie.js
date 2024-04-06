
var percentage_above_3 = percentage_data.pctg_ra3;
var percentage_below_3 = percentage_data.pctg_rb3;

var options = {
    series: [percentage_above_3, percentage_below_3],
    chart: {
        type: 'pie',
        height: '400px',
        width: '400px', 
        animations: {
            enabled: true,
            speed: 1000,
        },
    },
    labels: ['Above 4.0', 'Less/Equal  3.99'],
    colors: [
        getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
        getComputedStyle(document.documentElement).getPropertyValue('--vz-warning'),
    ],
    dataLabels: {
        enabled: true,
        offsetX: -10,
        offsetY: 50,
    },
};
var chart = new ApexCharts(document.querySelector("#prjects-status-1"), options);

if (chart == null) {
    document.querySelector("#prjects-status-1").innerHTML = '<p class="text-center">No data available.</p>';
}
else {
    chart.render();
}