function getChartColorsArray(a) {
    if (null !== document.getElementById(a))
        return (
            (a = document.getElementById(a).getAttribute("data-colors")),
            (a = JSON.parse(a)).map(function (a) {
                var r = a.replace(" ", "");
                return -1 === r.indexOf(",")
                    ? getComputedStyle(document.documentElement).getPropertyValue(r) || r
                    : 2 == (a = a.split(",")).length
                        ? "rgba(" +
                        getComputedStyle(document.documentElement).getPropertyValue(a[0]) +
                        "," +
                        a[1] +
                        ")"
                        : r;
            })
        );
}

            // This is for Research Bar Graphs : imported in rsrch.html

chartStorkeRadialbarColors &&
    ((options = {
        series: [67],
        chart: { height: 326, type: "radialBar", offsetY: -10 },
        plotOptions: {
            radialBar: {
                startAngle: -135,
                endAngle: 135,
                dataLabels: {
                    name: { fontSize: "16px", color: void 0, offsetY: 120 },
                    value: {
                        offsetY: 76,
                        fontSize: "22px",
                        color: void 0,
                        formatter: function (a) {
                            return a + "%";
                        },
                    },
                },
            },
        },
        fill: {
            type: "gradient",
            gradient: {
                shade: "dark",
                shadeIntensity: 0.15,
                inverseColors: !1,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 50, 65, 91],
            },
        },
        stroke: { dashArray: 4 },
        labels: ["Median Ratio"],
        colors: chartStorkeRadialbarColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#stroked_radialbar"),
            options
        )).render());
(chartStorkeRadialbarColors = getChartColorsArray("stroked_radialbar")) &&
    ((options = {
        series: [67],
        chart: { height: 315, type: "radialBar" },
        plotOptions: {
            radialBar: {
                hollow: {
                    margin: 15,
                    size: "65%",
                    image: "./assets/images/comingsoon.png",
                    imageWidth: 56,
                    imageHeight: 56,
                    imageClipped: !1,
                },
                dataLabels: {
                    name: { show: !1, color: "#fff" },
                    value: { show: !0, color: "#333", offsetY: 65, fontSize: "22px" },
                },
            },
        },
        fill: {
            type: "image",
            image: { src: ["./assets/images/small/img-4.jpg"] },
        },
        stroke: { lineCap: "round" },
        labels: ["Volatility"],
    }),
        (chart = new ApexCharts(
            document.querySelector("#radialbar_with_img"),
            options
        )).render());

var options,
    chart,
    chartSemiRadialbarColors = getChartColorsArray("semi_radialbar");
chartSemiRadialbarColors &&
    ((options = {
        series: [76],
        chart: {
            type: "radialBar",
            height: 350,
            offsetY: -20,
            sparkline: { enabled: !0 },
        },
        plotOptions: {
            radialBar: {
                startAngle: -90,
                endAngle: 90,
                track: {
                    background: "#e7e7e7",
                    strokeWidth: "97%",
                    margin: 5,
                    dropShadow: {
                        enabled: !0,
                        top: 2,
                        left: 0,
                        color: "#999",
                        opacity: 1,
                        blur: 2,
                    },
                },
                dataLabels: {
                    name: { show: !1 },
                    value: { offsetY: -2, fontSize: "22px" },
                },
            },
        },
        grid: { padding: { top: -10 } },
        fill: {
            type: "gradient",
            gradient: {
                shade: "light",
                shadeIntensity: 0.4,
                inverseColors: !1,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 50, 53, 91],
            },
        },
        labels: ["Average Results"],
        colors: chartSemiRadialbarColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#semi_radialbar"),
            options
        )).render());
