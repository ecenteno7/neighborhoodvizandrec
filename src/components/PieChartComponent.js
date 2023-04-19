import React, { useState, useEffect } from "react";
import { Chart } from "react-google-charts";

function getOptions(neighborhood) {
    return {
        title: neighborhood
    }
}

// function processData(data) {
//     let processedData = [];
//     processedData.push(['Activity', 'Trips']);
//     let activities = Object.keys(data);
//     console.log(data[activities[0]]);
//     let foo = Object.keys(data[activities[0]]);
//     console.log(activities);
//     console.log(foo[0]);
//     activities.forEach((activity) => {
//         processedData.push([activity, data[activity][foo[0]]]);
//     });
//     console.log(processData);
//     return processedData;
// }

export default function PieChartComponent({neighborhood, data}) {
    // const [data, setData] = useState([]);
    // const [isLoaded, setIsLoaded] = useState(false);

    // function getPieChartData(neighborhood) {
    //     console.log('neighborhood', neighborhood);
    //     fetch(`http://localhost:81/get-pie-chart-data?neighborhood=${neighborhood}`)
    //     .then(res => res.json())
    //     .then(
    //       (result) => {
    //           setIsLoaded(true);
    //           let processedData = processData(result);
    //           setData(processedData);
    //           console.log("data", processedData);
    //       },
    //       (error) => {
    //           setIsLoaded(true);
    //           // setError(error);
    //       }
    //     )
    // }

    // useEffect(() => {
    //     getPieChartData(neighborhood);
    //   }, [neighborhood])

    // if (!isLoaded) {
    //     return <div>Loading...</div>;
    // } else {
        return (
            <Chart
            chartType="PieChart"
            data={data}
            options={getOptions(neighborhood)}
            width={"100%"}
            height={"400px"}
            />
        );
    // }
}
