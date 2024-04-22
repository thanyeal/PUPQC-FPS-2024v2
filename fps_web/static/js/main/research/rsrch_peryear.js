
if (base_response == 0) {
    document.querySelector("#rsrch_counts").innerHTML = '<p class="text-center" style="margin: 5% 0% !important;">No data available.</p>';
}
else if (base_response == 1) {
    var years = Object.keys(groupedCountedData);

    var counts = years.map(year => groupedCountedData[year].count);
    var options = {
        chart: {
            height: 380,
            type: "line",
            zoom: { enabled: false },
            toolbar: { show: false },
        },
        colors: [
            getComputedStyle(document.documentElement).getPropertyValue('--vz-info'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-primary'),
            getComputedStyle(document.documentElement).getPropertyValue('--vz-secondary'),
        ],
        
        stroke: { width: [3, 3], curve: "smooth" },
        markers: { style: "inverted", size: 6 },
        series: [
            { name: 'No. of Research Published', data: counts },
        ],
        grid: {
            row: { colors: ["transparent", "transparent"], opacity: 0.2 },
            borderColor: "#f1f1f1",
        },
        markers: { style: "inverted", size: 6 },
        xaxis: {
            categories: years,
            title: { text: "Academic Year" },
        },
        yaxis: { title: { text: "Research Count" }, min: 0, max: 50 },
        legend: {
            position: "top",
            horizontalAlign: "right",
            floating: !0,
            offsetY: -25,
            offsetX: -5,
        },
        responsive: [
            {
                breakpoint: 600,
                options: { chart: { toolbar: { show: !1 } }, legend: { show: !1 } },
            },
        ],
    }
    var rsrch_chart = new ApexCharts(document.querySelector('#rsrch_counts'), options);
    rsrch_chart.render();

    
    // Create and populate the dropdown
    var yearFilterDropdown = document.getElementById('rsrch_year_filter');

    // Add 'All' option to show all data
    var rsrch_allOption = document.createElement('option');
        rsrch_allOption.value = 'all';
        rsrch_allOption.text = 'Display All';
    yearFilterDropdown.add(rsrch_allOption);

    years.forEach(year => {
        var option = document.createElement('option');
        option.value = year;
        option.text = year;
        yearFilterDropdown.appendChild(option);
    });

    function rsrch_updateChart(event) {
        if (event) {
            event.preventDefault();
        }
        var selectedYear = yearFilterDropdown.value;
        var filteredData = {};

        if (selectedYear === 'all') {
            filteredData = groupedCountedData; // Show all data
        }
        
        else {
            // Filter by year
            filteredData[selectedYear] = groupedCountedData[selectedYear];
        }

        var filteredYears = Object.keys(filteredData);
        var filteredCounts = filteredYears.map(year => filteredData[year].count);
        
        // Update the chart options with filtered data
        rsrch_chart.updateOptions({ xaxis: { categories: filteredYears } });
        rsrch_chart.updateSeries([{ data: filteredCounts }]);
    }

    yearFilterDropdown.addEventListener('change', rsrch_updateChart);
}