    // Fetch data from the Flask endpoint
    fetch('/monthly-survey-statistics')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Initialize the chart with dynamic data
        var options = {
            chart: {
                type: 'bar',
                height: 400
            },
            series: [
                {
                    name: 'Livelihood Support',
                    data: data.emergency_percent  // Use the emergency_percent data from the response
                },
                {
                    name: 'Emergency Needs',
                    data: data.livelihood_percent  // Use the livelihood_percent data from the response
                }
            ],
            xaxis: {
                categories: data.month // Use the month data from the response
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
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });

    $.ajax({
        type: "GET",
        url: "/response-percentage",
        dataType: "json",
        success: function (response) {
            const emergency_percentage = Math.round(response.emergency_percentage);
            const livelihood_percentage = Math.round(response.livelihood_percentage);

            console.log(livelihood_percentage)
            $('#emergency-needs-percentage').text(emergency_percentage+"%")
            $('#livelihood-support-percentage').text(livelihood_percentage+"%")
        }
    });
