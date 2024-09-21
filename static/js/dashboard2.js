// Initialize the chart
var options = {
    chart: {
        type: 'line',
        height: 400
    },
    series: [
        {
            name: 'Emergency Needs',
            data: [30, 70, 40, 80, 90, 100] // Example data for Emergency Needs
        },
        {
            name: 'Livelihood Support',
            data: [20, 50, 60, 70, 80, 90] // Example data for Livelihood Support
        }
    ],
    xaxis: {
        categories: ['January', 'February', 'March', 'April', 'May', 'June']
    },
    title: {
        text: 'Monthly Data Representation',
        align: 'center',
        style: {
            fontSize: '20px',
            fontWeight: 'bold'
        }
    },
    stroke: {
        width: 2,
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        title: {
            text: 'Values',
            style: {
                fontSize: '12px',
                fontWeight: 'bold'
            }
        },
        min: 0,
        max: 100,
        tickAmount: 5,
        labels: {
            formatter: function (val) {
                return val + '%';
            }
        }
    },
    legend: {
        position: 'top',
        horizontalAlign: 'center'
    }
};

var chart = new ApexCharts(document.querySelector("#dashboard2"), options);
chart.render();
