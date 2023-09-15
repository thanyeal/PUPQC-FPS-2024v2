function getChartColorsArray(e) {
    if (null !== document.getElementById(e)) {
        var a = document.getElementById(e).getAttribute("data-colors");
        if (a)
            return (a = JSON.parse(a)).map(function (e) {
                var a = e.replace(" ", "");
                return -1 === a.indexOf(",")
                    ? getComputedStyle(document.documentElement).getPropertyValue(a) || a
                    : 2 == (e = e.split(",")).length
                        ? "rgba(" +
                        getComputedStyle(document.documentElement).getPropertyValue(e[0]) +
                        "," +
                        e[1] +
                        ")"
                        : a;
            });
        console.warn("data-colors atributes not found on", e);
    }
}
var valrepTeacheval = {}

var linechartDashedColors = getChartColorsArray("line_chart_dashed"),
    chartDonutBasicColors =
        (linechartDashedColors &&
            ((options = {
                chart: {
                    height: 345,
                    type: "line",
                    zoom: { enabled: !1 },
                    toolbar: { show: !1 },
                },
                colors: linechartDashedColors,
                dataLabels: { enabled: !1 },
                stroke: { width: [3, 4, 3], curve: "straight", dashArray: [0, 3, 4] },
                series: [
                    {
                        name: "Peer Evaluation",
                        data: [79, 86, 74, 88, 82, 98, 84, 96, 94],
                    },
                    {
                        name: "Student Evaluation",
                        data: [45, 55, 58, 64, 53, 56, 61, 70, 76],
                    },
                    {
                        name: "Executive Evaluation",
                        data: [76, 42, 60, 42, 53, 58, 69, 77, 76],
                    },
                ],
                markers: { size: 0, hover: { sizeOffset: 6 } },
                xaxis: {
                    categories: [
                        "1st sem 2019",
                        "2nd sem 2019",
                        "1st sem 2020",
                        "2nd sem 2020",
                        "1st sem 2021",
                        "1st sem 2022",
                        "2nd sem 2023",
                        "1st sem 2024",
                        "2nd sem 2024",
                    ],
                },
                yaxis: {
                    labels: {
                        formatter: function (e) {
                            // Check if 'e' exists in the lookup table, if so, replace it
                            if (valrepTeacheval.hasOwnProperty(e)) {
                                e = valrepTeacheval[e];
                            }
                            // Format and return the modified 'e'
                            return e;
                        },
                    },
                    tickAmount: 5,
                    min: 0,
                    max: 100,
                },
                grid: { borderColor: "#f1f1f1" },
            }),
                (chart = new ApexCharts(
                    document.querySelector("#line_chart_dashed"),
                    options
                )).render()),
            getChartColorsArray("store-visits-source")),
    worldemapmarkers =
        (chartDonutBasicColors &&
            ((options = {
                series: [44, 55, 41, 17, 15],
                labels: ["Direct", "Social", "Email", "Other", "Referrals"],
                chart: { height: 333, type: "donut" },
                legend: { position: "bottom" },
                stroke: { show: !1 },
                dataLabels: { dropShadow: { enabled: !1 } },
                colors: chartDonutBasicColors,
            }),
                (chart = new ApexCharts(
                    document.querySelector("#store-visits-source"),
                    options
                )).render()),
            "");
function loadCharts() {
    var e = getChartColorsArray("sales-by-locations");
    e &&
        ((document.getElementById("sales-by-locations").innerHTML = ""),
            (worldemapmarkers = ""),
            (worldemapmarkers = new jsVectorMap({
                map: "world_merc",
                selector: "#sales-by-locations",
                zoomOnScroll: !1,
                zoomButtons: !1,
                selectedMarkers: [0, 5],
                regionStyle: {
                    initial: {
                        stroke: "#9599ad",
                        strokeWidth: 0.25,
                        fill: e[0],
                        fillOpacity: 1,
                    },
                },
                markersSelectable: !0,
                markers: [
                    { name: "Palestine", coords: [31.9474, 35.2272] },
                    { name: "Russia", coords: [61.524, 105.3188] },
                    { name: "Canada", coords: [56.1304, -106.3468] },
                    { name: "Greenland", coords: [71.7069, -42.6043] },
                ],
                markerStyle: { initial: { fill: e[1] }, selected: { fill: e[2] } },
                labels: {
                    markers: {
                        render: function (e) {
                            return e.name;
                        },
                    },
                },
            })));
}
(window.onresize = function () {
    setTimeout(() => {
        loadCharts();
    }, 0);
}),
    loadCharts();
var jobListAll,
    searchResultList,
    chart,
    jobListAllData = [
        [
            "01",
            "Faculty Number One",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "02",
            "Faculty Number Two",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "03",
            "Faculty Number Three",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "04",
            "Faculty Number Four",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "05",
            "Faculty Number Five",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "06",
            "Faculty Number Six",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "07",
            "Faculty Number Seven",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "08",
            "Faculty Number Eight",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "09",
            "Faculty Number Nine",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "10",
            "Faculty Number Ten",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "11",
            "Faculty Number Eleven",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
        [
            "12",
            "Faculty Number Twelve",
            "26.30",
            "OUTSTANDING",
            "0",
            "POOR",
            "20.12",
            "OUTSTANDING",
            "30.00",
            "VERY OUTSTANDING",
        ],
    ],
    chartRadialbarBasicColors =
        (document.getElementById("recomended-jobs") &&
            ((jobListAll = new gridjs.Grid({
                columns: [
                    { name: "No.", width: "80px" },
                    { name: "Faculty Name", width: "200px" },
                    { name: "Rating", width: "100px" },
                    { name: "Supervisor Interpretation", width: "200px" },
                    { name: "Rating", width: "100px" },
                    { name: "Students Interpretation", width: "200px" },
                    { name: "Rating", width: "100px" },
                    { name: "Peer Interpretation", width: "200px" },
                    { name: "Rating", width: "100px" },
                    { name: "Self Interpretation", width: "200px" },
                ],
                sort: !0,
                pagination: { limit: 15 },
                data: jobListAllData,
            }).render(document.getElementById("recomended-jobs"))),
                (searchResultList =
                    document.getElementById("searchResultList")).addEventListener(
                        "keyup",
                        function () {
                            var e = searchResultList.value.toLowerCase();
                            a = e;
                            var a,
                                e = jobListAllData.filter(function (e) {
                                    return (
                                        -1 !== e[0].toLowerCase().indexOf(a.toLowerCase()) ||
                                        -1 !== e[1].toLowerCase().indexOf(a.toLowerCase())
                                    );
                                });
                            jobListAll.updateConfig({ data: e }).forceRender();
                        }
                    )),
            Array.from(document.querySelectorAll("#candidate-list li")).forEach(
                function (t) {
                    t.querySelector("a").addEventListener("click", function () {
                        var e = t.querySelector(".candidate-name").innerHTML,
                            a = t.querySelector(".candidate-position").innerHTML,
                            r = t.querySelector(".candidate-img").src;
                        (document.getElementById("candidate-name").innerHTML = e),
                            (document.getElementById("candidate-position").innerHTML = a),
                            (document.getElementById("candidate-img").src = r);
                    });
                }
            ),
            window.addEventListener("load", () => {
                var r = document.getElementById("searchList"),
                    t = document.querySelectorAll("#candidate-list li");
                r.onkeyup = () => {
                    var e,
                        a = r.value.toLowerCase();
                    for (e of t)
                        -1 ==
                            e.querySelector(".candidate-name").innerHTML.toLowerCase().indexOf(a)
                            ? e.classList.add("d-none")
                            : e.classList.remove("d-none");
                };
            }),
            getChartColorsArray("total_jobs"));
chartRadialbarBasicColors &&
    ((options = {
        series: [95],
        chart: { type: "radialBar", width: 105, sparkline: { enabled: !0 } },
        dataLabels: { enabled: !1 },
        plotOptions: {
            radialBar: {
                hollow: { margin: 0, size: "70%" },
                track: { margin: 1 },
                dataLabels: {
                    show: !0,
                    name: { show: !1 },
                    value: { show: !0, fontSize: "16px", fontWeight: 600, offsetY: 8 },
                },
            },
        },
        colors: chartRadialbarBasicColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#total_jobs"),
            options
        )).render()),
    (chartRadialbarBasicColors = getChartColorsArray("apply_jobs")) &&
    ((options = {
        series: [97],
        chart: { type: "radialBar", width: 105, sparkline: { enabled: !0 } },
        dataLabels: { enabled: !1 },
        plotOptions: {
            radialBar: {
                hollow: { margin: 0, size: "70%" },
                track: { margin: 1 },
                dataLabels: {
                    show: !0,
                    name: { show: !1 },
                    value: { show: !0, fontSize: "16px", fontWeight: 600, offsetY: 8 },
                },
            },
        },
        colors: chartRadialbarBasicColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#apply_jobs"),
            options
        )).render()),
    (chartRadialbarBasicColors = getChartColorsArray("interview_chart")) &&
    ((options = {
        series: [89],
        chart: { type: "radialBar", width: 105, sparkline: { enabled: !0 } },
        dataLabels: { enabled: !1 },
        plotOptions: {
            radialBar: {
                hollow: { margin: 0, size: "70%" },
                track: { margin: 1 },
                dataLabels: {
                    show: !0,
                    name: { show: !1 },
                    value: { show: !0, fontSize: "16px", fontWeight: 600, offsetY: 8 },
                },
            },
        },
        colors: chartRadialbarBasicColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#interview_chart"),
            options
        )).render()),
    (chartRadialbarBasicColors = getChartColorsArray("hired_chart")) &&
    ((options = {
        series: [64],
        chart: { type: "radialBar", width: 105, sparkline: { enabled: !0 } },
        dataLabels: { enabled: !1 },
        plotOptions: {
            radialBar: {
                hollow: { margin: 0, size: "70%" },
                track: { margin: 1 },
                dataLabels: {
                    show: !0,
                    name: { show: !1 },
                    value: { show: !0, fontSize: "16px", fontWeight: 600, offsetY: 8 },
                },
            },
        },
        colors: chartRadialbarBasicColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#hired_chart"),
            options
        )).render()),
    (chartRadialbarBasicColors = getChartColorsArray("rejected_chart")) &&
    ((options = {
        series: [20],
        chart: { type: "radialBar", width: 105, sparkline: { enabled: !0 } },
        dataLabels: { enabled: !1 },
        plotOptions: {
            radialBar: {
                hollow: { margin: 0, size: "70%" },
                track: { margin: 1 },
                dataLabels: {
                    show: !0,
                    name: { show: !1 },
                    value: { show: !0, fontSize: "16px", fontWeight: 600, offsetY: 8 },
                },
            },
        },
        colors: chartRadialbarBasicColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#rejected_chart"),
            options
        )).render()),
    (chartRadialbarBasicColors = getChartColorsArray("new_jobs_chart")) &&
    ((options = {
        series: [80],
        chart: { type: "radialBar", width: 105, sparkline: { enabled: !0 } },
        dataLabels: { enabled: !1 },
        plotOptions: {
            radialBar: {
                hollow: { margin: 0, size: "70%" },
                track: { margin: 1 },
                dataLabels: {
                    show: !0,
                    name: { show: !1 },
                    value: { show: !0, fontSize: "16px", fontWeight: 600, offsetY: 8 },
                },
            },
        },
        colors: chartRadialbarBasicColors,
    }),
        (chart = new ApexCharts(
            document.querySelector("#new_jobs_chart"),
            options
        )).render());
