function getChartColorsArray(e) {
    if (null !== document.getElementById(e)) {
        e = document.getElementById(e).getAttribute("data-colors");
        if (e)
            return (e = JSON.parse(e)).map(function (e) {
                var t = e.replace(" ", "");
                return -1 === t.indexOf(",")
                    ? getComputedStyle(document.documentElement).getPropertyValue(t) || t
                    : 2 == (e = e.split(",")).length
                        ? "rgba(" +
                        getComputedStyle(document.documentElement).getPropertyValue(e[0]) +
                        "," +
                        e[1] +
                        ")"
                        : t;
            });
    }
}
 // exporte to rsrch analytics.js


function generateDayWiseTimeSeries(e, t, a) {
    for (var r = 0, i = []; r < t;) {
        var n = e,
            o = Math.floor(Math.random() * (a.max - a.min + 1)) + a.min;
        i.push([n, o]), (e += 864e5), r++;
    }
    return i;
}
linechartannotationsColors &&
    ((options = {
        series: [{ data: series.monthDataSeries1.prices }],
        chart: {
            height: 350,
            type: "line",
            id: "areachart-2",
            toolbar: { show: !1 },
        },
        annotations: {
            yaxis: [
                {
                    y: 8200,
                    borderColor: "#038edc",
                    label: {
                        borderColor: "#038edc",
                        style: { color: "#fff", background: "#038edc" },
                        text: "Support",
                    },
                },
                {
                    y: 8600,
                    y2: 9e3,
                    borderColor: "#f7cc53",
                    fillColor: "#f7cc53",
                    opacity: 0.2,
                    label: {
                        borderColor: "#f7cc53",
                        style: { fontSize: "10px", color: "#000", background: "#f7cc53" },
                        text: "Y-axis range",
                    },
                },
            ],
            xaxis: [
                {
                    x: new Date("23 Nov 2017").getTime(),
                    strokeDashArray: 0,
                    borderColor: "#564ab1",
                    label: {
                        borderColor: "#564ab1",
                        style: { color: "#fff", background: "#564ab1" },
                        text: "Anno Test",
                    },
                },
                {
                    x: new Date("26 Nov 2017").getTime(),
                    x2: new Date("28 Nov 2017").getTime(),
                    fillColor: "#51d28c",
                    opacity: 0.4,
                    label: {
                        borderColor: "#000",
                        style: { fontSize: "10px", color: "#fff", background: "#000" },
                        offsetY: -10,
                        text: "X-axis range",
                    },
                },
            ],
            points: [
                {
                    x: new Date("01 Dec 2017").getTime(),
                    y: 8607.55,
                    marker: {
                        size: 8,
                        fillColor: "#fff",
                        strokeColor: "red",
                        radius: 2,
                        cssClass: "apexcharts-custom-class",
                    },
                    label: {
                        borderColor: "#f34e4e",
                        offsetY: 0,
                        style: { color: "#fff", background: "#f34e4e" },
                        text: "Point Annotation",
                    },
                },
                {
                    x: new Date("08 Dec 2017").getTime(),
                    y: 9340.85,
                    marker: { size: 0 },
                    image: { path: "./assets/images/logo-sm.png", width: 40, height: 40 },
                },
            ],
        },
        dataLabels: { enabled: !1 },
        stroke: { curve: "straight" },
        colors: linechartannotationsColors,
        grid: { padding: { right: 30, left: 20 } },
        title: {
            text: "Line with Annotations",
            align: "left",
            style: { fontWeight: 500 },
        },
        labels: series.monthDataSeries1.dates,
        xaxis: { type: "datetime" },
    }),
        (chart = new ApexCharts(
            document.querySelector("#line_chart_annotations"),
            options
        )).render());

var chart,
    data = generateDayWiseTimeSeries(new Date("11 Feb 2017").getTime(), 185, {
        min: 30,
        max: 90,
    }),
    brushchartLine2Colors = getChartColorsArray("brushchart_line2"),
    brushchartLineColors =
        (brushchartLine2Colors &&
            ((options = {
                series: [{ data: data }],
                chart: {
                    id: "chart2",
                    type: "line",
                    height: 220,
                    toolbar: { autoSelected: "pan", show: !1 },
                },
                colors: brushchartLine2Colors,
                stroke: { width: 3 },
                dataLabels: { enabled: !1 },
                fill: { opacity: 1 },
                markers: { size: 0 },
                xaxis: { type: "datetime" },
            }),
                (chart = new ApexCharts(
                    document.querySelector("#brushchart_line2"),
                    options
                )).render()),
            getChartColorsArray("brushchart_line")),
    steplineChartColors =
        (brushchartLineColors &&
            ((optionsLine = {
                series: [{ data: data }],
                chart: {
                    id: "chart1",
                    height: 130,
                    type: "area",
                    brush: { target: "chart2", enabled: !0 },
                    selection: {
                        enabled: !0,
                        xaxis: {
                            min: new Date("19 Jun 2017").getTime(),
                            max: new Date("14 Aug 2017").getTime(),
                        },
                    },
                },
                colors: brushchartLineColors,
                fill: {
                    type: "gradient",
                    gradient: { opacityFrom: 0.91, opacityTo: 0.1 },
                },
                xaxis: { type: "datetime", tooltip: { enabled: !1 } },
                yaxis: { tickAmount: 2 },
            }),
                (chartLine = new ApexCharts(
                    document.querySelector("#brushchart_line"),
                    optionsLine
                )).render()),
            getChartColorsArray("line_chart_stepline")),
    lineChartGradientColors =
        (steplineChartColors &&
            ((options = {
                series: [{ data: [34, 44, 54, 21, 12, 43, 33, 23, 66, 66, 58] }],
                chart: { type: "line", height: 350, toolbar: { show: !1 } },
                stroke: { curve: "stepline" },
                dataLabels: { enabled: !1 },
                title: {
                    text: "Stepline Chart",
                    align: "left",
                    style: { fontWeight: 500 },
                },
                markers: { hover: { sizeOffset: 4 } },
                colors: steplineChartColors,
            }),
                (chart = new ApexCharts(
                    document.querySelector("#line_chart_stepline"),
                    options
                )).render()),
            getChartColorsArray("line_chart_gradient")),
    linechartMissingDataColors =
        (lineChartGradientColors &&
            ((options = {
                series: [
                    {
                        name: "Likes",
                        data: [
                            4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5,
                        ],
                    },
                ],
                chart: { height: 350, type: "line", toolbar: { show: !1 } },
                stroke: { width: 7, curve: "smooth" },
                xaxis: {
                    type: "datetime",
                    categories: [
                        "1/11/2001",
                        "2/11/2001",
                        "3/11/2001",
                        "4/11/2001",
                        "5/11/2001",
                        "6/11/2001",
                        "7/11/2001",
                        "8/11/2001",
                        "9/11/2001",
                        "10/11/2001",
                        "11/11/2001",
                        "12/11/2001",
                        "1/11/2002",
                        "2/11/2002",
                        "3/11/2002",
                        "4/11/2002",
                        "5/11/2002",
                        "6/11/2002",
                    ],
                    tickAmount: 10,
                },
                title: {
                    text: "Social Media",
                    align: "left",
                    style: { fontWeight: 500 },
                },
                fill: {
                    type: "gradient",
                    gradient: {
                        shade: "dark",
                        gradientToColors: lineChartGradientColors,
                        shadeIntensity: 1,
                        type: "horizontal",
                        opacityFrom: 1,
                        opacityTo: 1,
                        stops: [0, 100, 100, 100],
                    },
                },
                markers: {
                    size: 4,
                    colors: ["#038edc"],
                    strokeColors: "#fff",
                    strokeWidth: 2,
                    hover: { size: 7 },
                },
                yaxis: { min: -10, max: 40, title: { text: "Engagement" } },
            }),
                (chart = new ApexCharts(
                    document.querySelector("#line_chart_gradient"),
                    options
                )).render()),
            getChartColorsArray("line_chart_missing_data")),
    lastDate =
        (linechartMissingDataColors &&
            ((options = {
                series: [
                    {
                        name: "Peter",
                        data: [5, 5, 10, 8, 7, 5, 4, null, null, null, 10, 10, 7, 8, 6, 9],
                    },
                    {
                        name: "Johnny",
                        data: [
                            10,
                            15,
                            null,
                            12,
                            null,
                            10,
                            12,
                            15,
                            null,
                            null,
                            12,
                            null,
                            14,
                            null,
                            null,
                            null,
                        ],
                    },
                    {
                        name: "David",
                        data: [
                            null,
                            null,
                            null,
                            null,
                            3,
                            4,
                            1,
                            3,
                            4,
                            6,
                            7,
                            9,
                            5,
                            null,
                            null,
                            null,
                        ],
                    },
                ],
                chart: {
                    height: 350,
                    type: "line",
                    zoom: { enabled: !1 },
                    animations: { enabled: !1 },
                },
                stroke: { width: [5, 5, 4], curve: "straight" },
                labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                title: {
                    text: "Missing data (null values)",
                    style: { fontWeight: 500 },
                },
                xaxis: {},
                colors: linechartMissingDataColors,
            }),
                (chart = new ApexCharts(
                    document.querySelector("#line_chart_missing_data"),
                    options
                )).render()),
            0),
    data = [],
    TICKINTERVAL = 864e5,
    XAXISRANGE = 7776e5;


function getDayWiseTimeSeries(e, t, a) {
    for (var r = 0; r < t;) {
        var i = e,
            n = Math.floor(Math.random() * (a.max - a.min + 1)) + a.min;
        data.push({ x: i, y: n }), (lastDate = e), (e += TICKINTERVAL), r++;
    }
}
function getNewSeries(e, t) {
    var a = e + TICKINTERVAL;
    lastDate = a;
    for (var r = 0; r < data.length - 10; r++)
        (data[r].x = a - XAXISRANGE - TICKINTERVAL), (data[r].y = 0);
    data.push({
        x: a,
        y: Math.floor(Math.random() * (t.max - t.min + 1)) + t.min,
    });
}
function resetData() {
    data = data.slice(data.length - 10, data.length);
}
getDayWiseTimeSeries(new Date("11 Feb 2017 GMT").getTime(), 10, {
    min: 10,
    max: 90,
});

