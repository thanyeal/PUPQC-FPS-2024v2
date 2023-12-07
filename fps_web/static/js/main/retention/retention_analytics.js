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
        console.warn("data-colors atributes not found on", e);
    }
}

var barchartCountriesColors = getChartColorsArray("countries_charts");
function generateData(e, t) {
    for (var a = 0, o = []; a < e;) {
        var r = (a + 1).toString() + "h",
            n = Math.floor(Math.random() * (t.max - t.min + 1)) + t.min;
        o.push({ x: r, y: n }), a++;
    }
    return o;
}
barchartCountriesColors &&
    ((options = {
        series: [
            {
                data: [1010, 1640, 490, 1255, 1050, 689, 800, 420, 1085, 589],
                name: "Sessions",
            },
        ],
        chart: { type: "bar", height: 436, toolbar: { show: !1 } },
        plotOptions: {
            bar: {
                borderRadius: 4,
                horizontal: !0,
                distributed: !0,
                dataLabels: { position: "top" },
            },
        },
        colors: barchartCountriesColors,
        dataLabels: {
            enabled: !0,
            offsetX: 32,
            style: { fontSize: "12px", fontWeight: 400, colors: ["#adb5bd"] },
        },
        legend: { show: !1 },
        grid: { show: !1 },
        xaxis: {
            categories: [
                "High Very Good Feedbacks",
                "Medium Very Good Feedbacks",
                "Low Very Good Feedbacks",
                "High Good Feedbacks",
                "Medium Good Feedbacks",
                "Low Good Feedbacks",
                "High Good Feedbacks",
                "Medium Good Feedbacks",
                "Low Good Feedbacks",
                "High Good Feedbacks",
            ],
        },
    }),
        (chart = new ApexCharts(
            document.querySelector("#countries_charts"),
            options
        )).render());


var columnoptions,
options,
chart,
chartHeatMapBasicColors = getChartColorsArray(
    "audiences-sessions-country-charts"
),
chartAudienceColumnChartsColors =
    (chartHeatMapBasicColors &&
        ((options = {
            series: [
                { name: "Sat", data: generateData(18, { min: 0, max: 90 }) },
                { name: "Fri", data: generateData(18, { min: 0, max: 90 }) },
                { name: "Thu", data: generateData(18, { min: 0, max: 90 }) },
                { name: "Wed", data: generateData(18, { min: 0, max: 90 }) },
                { name: "Tue", data: generateData(18, { min: 0, max: 90 }) },
                { name: "Mon", data: generateData(18, { min: 0, max: 90 }) },
                { name: "Sun", data: generateData(18, { min: 0, max: 90 }) },
            ],
            chart: {
                height: 400,
                type: "heatmap",
                offsetX: 0,
                offsetY: -8,
                toolbar: { show: !1 },
            },
            plotOptions: {
                heatmap: {
                    colorScale: {
                        ranges: [
                            { from: 0, to: 50, color: chartHeatMapBasicColors[0] },
                            { from: 51, to: 100, color: chartHeatMapBasicColors[1] },
                        ],
                    },
                },
            },
            dataLabels: { enabled: !1 },
            legend: {
                show: !0,
                horizontalAlign: "center",
                offsetX: 0,
                offsetY: 20,
                markers: { width: 20, height: 6, radius: 2 },
                itemMargin: { horizontal: 12, vertical: 0 },
            },
            colors: chartHeatMapBasicColors,
            tooltip: {
                y: [
                    {
                        formatter: function (e) {
                            return void 0 !== e ? e.toFixed(0) + "k" : e;
                        },
                    },
                ],
            },
        }),
            (chart = new ApexCharts(
                document.querySelector("#audiences-sessions-country-charts"),
                options
            )).render()),
        getChartColorsArray("audiences_metrics_charts")),
dountchartUserDeviceColors =
    (chartAudienceColumnChartsColors &&
        ((columnoptions = {
            series: [
                {
                    name: "Good Feedback",
                    data: [
                        25.3, 12.5, 20.2, 18.5, 40.4,
                    ],
                },
                {
                    name: "Bad Feedback",
                    data: [
                        36.2, 22.4, 38.2, 30.5, 26.4,
                    ],
                },
            ],
            chart: { type: "bar", height: 309, stacked: !0, toolbar: { show: !1 } },
            plotOptions: {
                bar: { horizontal: !1, columnWidth: "20%", borderRadius: 6 },
            },
            dataLabels: { enabled: !1 },
            legend: {
                show: !0,
                position: "bottom",
                horizontalAlign: "center",
                fontWeight: 400,
                fontSize: "8px",
                offsetX: 0,
                offsetY: 0,
                markers: { width: 9, height: 9, radius: 4 },
            },
            stroke: { show: !0, width: 2, colors: ["transparent"] },
            grid: { show: !1 },
            colors: chartAudienceColumnChartsColors,
            xaxis: {
                categories: [
                    "2019",
                    "2020",
                    "2021",
                    "2022",
                    "2023",
                ],
                axisTicks: { show: !1 },
                axisBorder: {
                    show: !0,
                    strokeDashArray: 1,
                    height: 1,
                    width: "100%",
                    offsetX: 0,
                    offsetY: 0,
                },
            },
            yaxis: { show: !1 },
            fill: { opacity: 1 },
        }),
            (chart = new ApexCharts(
                document.querySelector("#audiences_metrics_charts"),
                columnoptions
            )).render()),
        getChartColorsArray("user_device_pie_charts"));


        var options,
        chart,
        linechartcustomerColors = getChartColorsArray("customer_impression_charts"),
        chartDonutBasicColors =
            (linechartcustomerColors &&
                ((options = {
                    series: [
                        {
                            name: "Orders",
                            type: "area",
                            data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67],
                        },
                        {
                            name: "Earnings",
                            type: "bar",
                            data: [
                                89.25, 98.58, 68.74, 108.87, 77.54, 84.03, 51.24, 28.57, 92.57,
                                42.36, 88.51, 36.57,
                            ],
                        },
                        {
                            name: "Refunds",
                            type: "line",
                            data: [8, 12, 7, 17, 21, 11, 5, 9, 7, 29, 12, 35],
                        },
                    ],
                    chart: { height: 370, type: "line", toolbar: { show: !1 } },
                    stroke: { curve: "straight", dashArray: [0, 0, 8], width: [2, 0, 2.2] },
                    fill: { opacity: [0.1, 0.9, 1] },
                    markers: { size: [0, 0, 0], strokeWidth: 2, hover: { size: 4 } },
                    xaxis: {
                        categories: [
                            "Jan",
                            "Feb",
                            "Mar",
                            "Apr",
                            "May",
                            "Jun",
                            "Jul",
                            "Aug",
                            "Sep",
                            "Oct",
                            "Nov",
                            "Dec",
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
                            {
                                formatter: function (e) {
                                    return void 0 !== e ? "$" + e.toFixed(2) + "k" : e;
                                },
                            },
                            {
                                formatter: function (e) {
                                    return void 0 !== e ? e.toFixed(0) + " Sales" : e;
                                },
                            },
                        ],
                    },
                }),
                    (chart = new ApexCharts(
                        document.querySelector("#customer_impression_charts"),
                        options
                    )).render()),
                getChartColorsArray("store-visits-source"));