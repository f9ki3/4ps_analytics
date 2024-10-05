
    // Initialize the chart
    var options = {
        chart: {
            type: 'line',
            height: 400
        },
        series: [
            {
                name: 'Health',
                data: [20, 45, 60, 80, 100, 80]
            },
            {
                name: 'Education',
                data: [30, 50, 23, 90, 60, 40]
            },
            {
                name: 'Financial Stability',
                data: [10, 30, 12, 30, 90, 100]
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

    var chart = new ApexCharts(document.querySelector("#dashboard3"), options);
    chart.render();