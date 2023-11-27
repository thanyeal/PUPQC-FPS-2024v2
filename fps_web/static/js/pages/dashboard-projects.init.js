function getChartColorsArray(e) {
    if (null !== document.getElementById(e)) {
        var t = document.getElementById(e).getAttribute("data-colors");
        if (t)
            return (t = JSON.parse(t)).map(function (e) {
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
        console.warn("data-colors Attribute not found on:", e);
    }
}
var options,
    chart,
    linechartcustomerColors = getChartColorsArray("projects-overview-chart"),
    isApexSeriesData =
        (linechartcustomerColors &&
            ((options = {
                series: [
                    {
                        name: "1st Semestral Year Awardees",
                        type: "bar",
                        data: [12, 10, 16, 18, 10, 11, 12, 14, 18],
                    },
                    {
                        name: "No. of Performing Faculties in Academic Year",
                        type: "area",
                        data: [15, 20, 19, 14, 12, 15, 16, 12, 11],
                    },
                    {
                        name: "2nd Semestral Year Awardees",
                        type: "bar",
                        data: [10, 18, 18, 11, 9, 10, 2, 4, 10],
                    },
                ],
                chart: { height: 374, type: "line", toolbar: { show: !1 } },
                stroke: { curve: "smooth", dashArray: [0, 3, 0], width: [0, 1, 0] },
                fill: { opacity: [1, 0.1, 1] },
                markers: { size: [0, 4, 0], strokeWidth: 2, hover: { size: 4 } },
                xaxis: {
                    categories: [
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021",
                        "2022",
                        "2023",
                    ],
                    axisTicks: { show: !1 },
                    axisBorder: { show: !1 },
                },
                grid: {
                    show: !0,
                    xaxis: { lines: { show: !0 } },
                    yaxis: { lines: { show: !1 } },
                    padding: { top: 0, right: -2, bottom: 15, left: 10 },
                },
                legend: {
                    show: !0,
                    horizontalAlign: "center",
                    offsetX: 0,
                    offsetY: -5,
                    markers: { width: 9, height: 9, radius: 6 },
                    itemMargin: { horizontal: 10, vertical: 0 },
                },
                plotOptions: { bar: { columnWidth: "30%", barHeight: "70%" } },
                colors: linechartcustomerColors,
                tooltip: {
                    shared: !0,
                    y: [
                        {
                            formatter: function (e) {
                                return void 0 !== e ? e.toFixed(0) : e;
                            },
                        },
                        //{
                        //    formatter: function (e) {
                        //        return void 0 !== e ? "$" + e.toFixed(2) : e;
                        //    },
                        //},
                        {
                            formatter: function (e) {
                                return void 0 !== e ? e.toFixed(0) : e;
                            },
                        },
                    ],
                },
            }),
                (chart = new ApexCharts(
                    document.querySelector("#projects-overview-chart"),
                    options
                )).render()),
            {}),
    isApexSeries = document.querySelectorAll("[data-chart-series]"),
    donutchartProjectsStatusColors =
        (isApexSeries &&
            Array.from(isApexSeries).forEach(function (e) {
                var t,
                    e = e.attributes;
                e["data-chart-series"] &&
                    ((isApexSeriesData.series = e["data-chart-series"].value.toString()),
                        (t = getChartColorsArray(e.id.value.toString())),
                        (t = {
                            series: [isApexSeriesData.series],
                            chart: {
                                type: "radialBar",
                                width: 36,
                                height: 36,
                                sparkline: { enabled: !0 },
                            },
                            dataLabels: { enabled: !1 },
                            plotOptions: {
                                radialBar: {
                                    hollow: { margin: 0, size: "50%" },
                                    track: { margin: 1 },
                                    dataLabels: { show: !1 },
                                },
                            },
                            colors: t,
                        }),
                        new ApexCharts(
                            document.querySelector("#" + e.id.value.toString()),
                            t
                        ).render());
            }),
            getChartColorsArray("prjects-status")),
    currentChatId =
        (donutchartProjectsStatusColors &&
            ((options = {
                series: [125, 42, 58, 89],
                labels: ["Completed", "In Progress", "Yet to Start", "Cancelled"],
                chart: { type: "donut", height: 230 },
                plotOptions: {
                    pie: {
                        size: 100,
                        offsetX: 0,
                        offsetY: 0,
                        donut: { size: "60%", labels: { show: !1 } },
                    },
                },
                dataLabels: { enabled: !1 },
                legend: { show: !1 },
                stroke: { lineCap: "round", width: 0 },
                colors: donutchartProjectsStatusColors,
            }),
                (chart = new ApexCharts(
                    document.querySelector("#prjects-status"),
                    options
                )).render()),
            "users-chat");
function scrollToBottom(e) {
    setTimeout(() => {
        new SimpleBar(
            document.getElementById("chat-conversation")
        ).getScrollElement().scrollTop =
            document.getElementById("users-conversation").scrollHeight;
    }, 100);
}
scrollToBottom(currentChatId);
