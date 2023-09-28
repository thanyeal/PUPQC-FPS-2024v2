
var chartData = JSON.parse('{{ chart_data|escapejs|safe }}');
function initializeChartOne() {
    var options = {
        chart: {
            type: 'line',
            height: 345,
            zoom: { enabled: true },
            toolbar: { show: true },
        },
        stroke: {
            width: [1, 1, 1, 1],
            curve: "straight",
            dashArray: [0, 1, 0, 0]
        },
        fill: {
            opacity: [1, 1, 1, 1]
        },
        markers: {
            size: [0, 4, 0, 0],
            strokeWidth: 2,
            hover: { size: 4 }
        },
        series: [
            {
                name: "Supervisor Evaluation",
                type: "bar",
                data: chartData.supervisor,
            },
            {
                name: "Student Evaluation",
                type: "line",
                data: chartData.student,
            },
            {
                name: "Peer Evaluation",
                type: "bar",
                data: chartData.peer,
            },
            {
                name: "Self Evaluation",
                type: "bar",
                data: chartData.self,
            }
        ],
        xaxis: {
            categories: chartData.faculty,
        },
        colors: [
            getComputedStyle(document.documentElement).getPropertyValue('--vz-success'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-secondary'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-danger'),
        ]
    }
    var chart = new ApexCharts(document.querySelector("#line-chart"), options);
    chart.render();
}
// Call the chart initialization function
initializeChartOne();