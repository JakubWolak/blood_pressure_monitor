
    var systolic_pressure_options = {};

    systolic_pressure_options = {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'mm Hg',
                    data: systolic_pressure,
                }]
            },
            options: {
              scales: {
                yAxes: [{
                  ticks: {
                    beginAtZero: true,
                    suggestedMax: 200,
                  }
                }]
              }
            }
          };
