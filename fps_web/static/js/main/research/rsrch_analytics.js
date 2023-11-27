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
var options,
    charts,
    linechartrealtimeColors = getChartColorsArray("line_chart_realtime");
function generateDayWiseTimeSeriesline(e, t, a) {
    for (var r = 0, i = []; r < t;) {
        var n = e,
            o = Math.floor(Math.random() * (a.max - a.min + 1)) + a.min;
        i.push([n, o]), (e += 864e5), r++;
    }
    return i;
}
linechartrealtimeColors &&
    ((options = {
        series: [{ data: data.slice() }],
        chart: {
            id: "realtime",
            height: 350,
            type: "line",
            animations: {
                enabled: !0,
                easing: "linear",
                dynamicAnimation: { speed: 1e3 },
            },
            toolbar: { show: true },
            zoom: { enabled: true },
        },
        dataLabels: { enabled: !1 },
        stroke: { curve: "smooth" },
        title: {
            text: "Dynamic Updating Chart",
            align: "left",
            style: { fontWeight: 500 },
        },
        markers: { size: 0 },
        colors: linechartrealtimeColors,
        xaxis: { type: "datetime", range: XAXISRANGE },
        yaxis: { max: 100 },
        legend: { show: !1 },
    }),
        (charts = new ApexCharts(
            document.querySelector("#line_chart_realtime"),
            options
        )).render()),
    window.setInterval(function () {
        getNewSeries(lastDate, { min: 10, max: 90 }),
            charts.updateSeries([{ data: data }]);
    }, 1e3);

var optionsLine,
    chartLine,
    optionsLine2,
    chartLine2,
    optionsArea,
    chartArea,
    chartSyncingLine = getChartColorsArray("chart-syncing-line"),
    chartSyncingLine2 =
        (chartSyncingLine &&
            ((optionsLine = {
                series: [
                    {
                        data: generateDayWiseTimeSeriesline(
                            new Date("11 Feb 2017").getTime(),
                            20,
                            { min: 10, max: 60 }
                        ),
                    },
                ],
                chart: {
                    id: "fb",
                    group: "social",
                    type: "line",
                    height: 160,
                    toolbar: { show: true },
                    zoom: { enabled: true },
                },
                colors: chartSyncingLine,
                dataLabels: { enabled: !1 },
                stroke: { curve: "straight", width: 3 },
                toolbar: { tools: { selection: !1 } },
                markers: { size: 4, hover: { size: 6 } },
                tooltip: {
                    followCursor: !1,
                    x: { show: !1 },
                    marker: { show: !1 },
                    y: {
                        title: {
                            formatter: function () {
                                return "";
                            },
                        },
                    },
                },
                grid: { clipMarkers: !1 },
                yaxis: { tickAmount: 2 },
                xaxis: { type: "datetime" },
            }),
                (chartLine = new ApexCharts(
                    document.querySelector("#chart-syncing-line"),
                    optionsLine
                )).render()),
            getChartColorsArray("chart-syncing-line2")),
    chartSyncingArea =
        (chartSyncingLine2 &&
            ((optionsLine2 = {
                series: [
                    {
                        data: generateDayWiseTimeSeriesline(
                            new Date("11 Feb 2017").getTime(),
                            20,
                            { min: 10, max: 30 }
                        ),
                    },
                ],
                chart: {
                    id: "tw",
                    group: "social",
                    type: "line",
                    height: 160,
                    toolbar: { show: true },
                    zoom: { enabled: true },
                },
                colors: chartSyncingLine2,
                dataLabels: { enabled: !1 },
                stroke: { curve: "straight", width: 3 },
                toolbar: { tools: { selection: !1 } },
                markers: { size: 4, hover: { size: 6 } },
                tooltip: {
                    followCursor: !1,
                    x: { show: !1 },
                    marker: { show: !1 },
                    y: {
                        title: {
                            formatter: function () {
                                return "";
                            },
                        },
                    },
                },
                grid: { clipMarkers: !1 },
                yaxis: { tickAmount: 2 },
                xaxis: { type: "datetime" },
            }),
                (chartLine2 = new ApexCharts(
                    document.querySelector("#chart-syncing-line2"),
                    optionsLine2
                )).render()),
            getChartColorsArray("chart-syncing-area"));
chartSyncingArea &&
    ((optionsArea = {
        series: [
            {
                data: generateDayWiseTimeSeriesline(
                    new Date("11 Feb 2017").getTime(),
                    20,
                    { min: 10, max: 60 }
                ),
            },
        ],
        chart: {
            id: "yt",
            group: "social",
            type: "area",
            height: 160,
            toolbar: { show: true },
            zoom: { enabled: true },
        },
        colors: chartSyncingArea,
        dataLabels: { enabled: !1 },
        stroke: { curve: "straight", width: 3 },
        toolbar: { tools: { selection: !1 } },
        markers: { size: 4, hover: { size: 6 } },
        tooltip: {
            followCursor: !1,
            x: { show: !1 },
            marker: { show: !1 },
            y: {
                title: {
                    formatter: function () {
                        return "";
                    },
                },
            },
        },
        grid: { clipMarkers: !1 },
        yaxis: { tickAmount: 2 },
        xaxis: { type: "datetime" },
    }),
        (chartArea = new ApexCharts(
            document.querySelector("#chart-syncing-area"),
            optionsArea
        )).render());
