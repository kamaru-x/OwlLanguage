(function($) {
    "use strict";

    /*************************
          Chart Column
    *************************/
    var chartcolumn = jQuery('#chart-column')
    if (chartcolumn.length > 0) {
        var options = {
            series: [{
                data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
            }],
            chart: {
                type: 'bar',
                height: 440,
                toolbar: {
                    show: false
                },
            },
            plotOptions: {
                bar: {
                    horizontal: true,
                }
            },
            colors: ['#f85a14'],
            dataLabels: {
                enabled: false
            },
            xaxis: {
                categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan',
                    'United States', 'China', 'Germany'
                ],
            }
        };

        var chart = new ApexCharts(document.querySelector("#chart-column"), options);
        chart.render();
    }

    /*************************
          Chart Wave
    *************************/

    var chartwave = jQuery('#chart-wave')
    if (chartwave.length > 0) {
        var options = {
            series: [{
                name: 'TEAM A',
                type: 'column',
                data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30]
            }, {
                name: 'TEAM B',
                type: 'area',
                data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43]
            }],
            chart: {
                height: 370,
                type: 'line',
                stacked: false,
                toolbar: {
                    show: false
                },
            },
            stroke: {
                width: [0, 2, 5],
                curve: 'smooth'
            },
            plotOptions: {
                bar: {
                    columnWidth: '50%'
                }
            },
            colors: ['#f85a14', '#f85a14'],
            fill: {
                opacity: [0.85, 0.25, 1],
                gradient: {
                    inverseColors: false,
                    shade: 'light',
                    type: "vertical",
                    opacityFrom: 0.85,
                    opacityTo: 0.55,
                    stops: [0, 100, 100, 100]
                }
            },
            labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003',
                '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'
            ],
            markers: {
                size: 0
            },
            xaxis: {
                type: 'datetime'
            },
            yaxis: {
                min: 0
            },
            tooltip: {
                shared: true,
                intersect: false,
                y: {
                    formatter: function(y) {
                        if (typeof y !== "undefined") {
                            return y.toFixed(0) + " points";
                        }
                        return y;

                    }
                }
            }
        };

        var chart = new ApexCharts(document.querySelector("#chart-wave"), options);
        chart.render();

    }

    /*************************
          Chart Round
    *************************/
    var chartround = jQuery('#chart-round')
    if (chartround.length > 0) {

        var options = {
            series: [{
                    name: 'Bob',
                    data: [{
                            x: 'Design',
                            y: [
                                new Date('2019-03-05').getTime(),
                                new Date('2019-03-08').getTime()
                            ]
                        },
                        {
                            x: 'Code',
                            y: [
                                new Date('2019-03-02').getTime(),
                                new Date('2019-03-05').getTime()
                            ]
                        },
                        {
                            x: 'Code',
                            y: [
                                new Date('2019-03-05').getTime(),
                                new Date('2019-03-07').getTime()
                            ]
                        },
                        {
                            x: 'Test',
                            y: [
                                new Date('2019-03-03').getTime(),
                                new Date('2019-03-09').getTime()
                            ]
                        },
                        {
                            x: 'Test',
                            y: [
                                new Date('2019-03-08').getTime(),
                                new Date('2019-03-11').getTime()
                            ]
                        },
                        {
                            x: 'Validation',
                            y: [
                                new Date('2019-03-11').getTime(),
                                new Date('2019-03-16').getTime()
                            ]
                        },
                        {
                            x: 'Design',
                            y: [
                                new Date('2019-03-01').getTime(),
                                new Date('2019-03-03').getTime()
                            ]
                        }
                    ]
                },
                {
                    name: 'Joe',
                    data: [{
                            x: 'Design',
                            y: [
                                new Date('2019-03-02').getTime(),
                                new Date('2019-03-05').getTime()
                            ]
                        },
                        {
                            x: 'Test',
                            y: [
                                new Date('2019-03-06').getTime(),
                                new Date('2019-03-16').getTime()
                            ]
                        },
                        {
                            x: 'Code',
                            y: [
                                new Date('2019-03-03').getTime(),
                                new Date('2019-03-07').getTime()
                            ]
                        },
                        {
                            x: 'Deployment',
                            y: [
                                new Date('2019-03-20').getTime(),
                                new Date('2019-03-22').getTime()
                            ]
                        },
                        {
                            x: 'Design',
                            y: [
                                new Date('2019-03-10').getTime(),
                                new Date('2019-03-16').getTime()
                            ]
                        }
                    ]
                },
                {
                    name: 'Dan',
                    data: [{
                            x: 'Code',
                            y: [
                                new Date('2019-03-10').getTime(),
                                new Date('2019-03-17').getTime()
                            ]
                        },
                        {
                            x: 'Validation',
                            y: [
                                new Date('2019-03-05').getTime(),
                                new Date('2019-03-09').getTime()
                            ]
                        },
                    ]
                }
            ],
            chart: {
                height: 300,
                type: 'rangeBar',
                toolbar: {
                    show: false,
                },
            },
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: '100%'
                }
            },
            colors: ['#f85a14', '#212c6b', '#28a745'],
            xaxis: {
                type: 'datetime'
            },
            yaxis: {
                labels: {
                    show: false,
                },
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'light',
                    type: 'vertical',
                    shadeIntensity: 1,
                    gradientToColors: undefined,
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [50, 0, 100, 100]
                }
            },
            legend: {
                show: false,
                position: 'top',
                horizontalAlign: 'left'
            }
        };

        var chart = new ApexCharts(document.querySelector("#chart-round"), options);
        chart.render();
    }

})(jQuery);