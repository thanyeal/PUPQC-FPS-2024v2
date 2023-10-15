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
// THIS IS FOR FPS
var valrepResearch = {
    // for research published
    36: 50,    
    27: 30,  
    18: 20,  
    9: 10,  
    0: 0,
    
}

var valrepCommittee = {
    // for committee and service contributions
    260: 100,
    208: 80,
    156: 60,
    104: 40,
    52: 20,
    0: 0,
};
// for research and productivity
var options,
    chart,
    areachartSalesColors = getChartColorsArray("sales-forecast-chart"),
    dealTypeChartsColors =
        (areachartSalesColors &&
            ((options = {
                series: [
                    { name: "2021", data: [37] },
                    { name: "2022", data: [12] },
                    { name: "2023", data: [18] },
                ],
                chart: { type: "bar", height: 341, toolbar: { show: !1 } },
                plotOptions: { bar: { horizontal: !1, columnWidth: "65%" } },
                stroke: { show: !0, width: 5, colors: ["transparent"] },
                xaxis: {
                    categories: [""],
                    axisTicks: {
                        show: !1,
                        borderType: "solid",
                        color: "#78909C",
                        height: 6,
                        offsetX: 0,
                        offsetY: 0,
                    },
                    title: {
                        text: "Total Forecasted Value",
                        offsetX: 0,
                        offsetY: -30,
                        style: { color: "#78909C", fontSize: "12px", fontWeight: 400 },
                    },
                },
                yaxis: {       
                    labels: {
                        formatter: function (e) {
                            // Check if 'e' exists in the lookup table, if so, replace it
                            if (valrepResearch.hasOwnProperty(e)) {
                                e = valrepResearch[e];
                            }
                            // Format and return the modified 'e'
                            return e;
                        },
                    },
                    max: 50,
                },
                fill: { opacity: 1 },
                legend: {
                    show: !0,
                    position: "bottom",
                    horizontalAlign: "center",
                    fontWeight: 500,
                    offsetX: 0,
                    offsetY: -14,
                    itemMargin: { horizontal: 8, vertical: 0 },
                    markers: { width: 10, height: 10 },
                },
                colors: areachartSalesColors,
            }),
            (chart = new ApexCharts(
                document.querySelector("#sales-forecast-chart"),
                options
            )).render()),

// for performance evaluation
            getChartColorsArray("deal-type-charts")),
    revenueExpensesChartsColors =
        (dealTypeChartsColors &&
            ((options = {
                series: [
                    { name: "Overall", data: [80, 50, 30, 40, 100, 20] },
                    { name: "Peer", data: [20, 30, 40, 80, 20, 80] },
                    { name: "Students", data: [44, 76, 78, 13, 43, 10] },
                ],
                chart: {
                    height: 341,
                    type: "radar",
                    dropShadow: { enabled: !0, blur: 1, left: 1, top: 1 },
                    toolbar: { show: !1 },
                },
                stroke: { width: 2 },
                fill: { opacity: 0.2 },
                legend: {
                    show: !0,
                    fontWeight: 500,
                    offsetX: 0,
                    offsetY: -8,
                    markers: { width: 8, height: 8, radius: 6 },
                    itemMargin: { horizontal: 10, vertical: 0 },
                },
                markers: { size: 0 },
                colors: dealTypeChartsColors,
                xaxis: { categories: ["2016", "2017", "2018", "2019", "2020", "2021"] },
            }),
            (chart = new ApexCharts(
                document.querySelector("#deal-type-charts"),
                options
            )).render()),

// for committee and service contributions
            getChartColorsArray("revenue-expenses-charts"));
    revenueExpensesChartsColors &&
    ((options = {
        series: [
            {
                name: "2021",
                data: [20, 25, 30, 35, 40, 55, 70, 80, 90, 92, 95, 100],
            },
            {
                name: "2022",
                data: [12, 17, 15, 23, 24, 35, 30, 40, 56, 34, 60, 65],
            },
            {
                name: "2023",
                data: [2, 12, 16, 18, 26, 36, 46, 55, 65, 77, 88, 95],
            },
        ],
        chart: { height: 290, type: "area", toolbar: "false" },
        dataLabels: { enabled: !1 },
        stroke: { curve: "smooth", width: 2 },
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
        },
        yaxis: {
            labels: {
                formatter: function (e) {
                    // Check if 'e' exists in the lookup table, if so, replace it
                    if (valrepCommittee.hasOwnProperty(e)) {
                        e = valrepCommittee[e];
                    }
                    // Format and return the modified 'e'
                    return e;
                },
            },
            tickAmount: 5,
            min: 0,
            max: 100,
        },
        colors: revenueExpensesChartsColors,
        fill: { opacity: 0.06, colors: revenueExpensesChartsColors, type: "solid" },
    }),
        (chart = new ApexCharts(
            document.querySelector("#revenue-expenses-charts"),
            options
        )).render());

