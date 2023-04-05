import React, {useState, useEffect} from 'react'
import rd3 from 'react-d3-library';
import * as d3 from 'd3';

export default function OverlayComponent() {
    const [d3Obj, setD3] = useState('');
    const RD3Component = rd3.Component;

    useEffect(() => {
        console.log('mount');

        // enter code to define margin and dimensions for svg
        const width = 960;
        const height = 600;
        const margin = 50;

        // enter code to define projection and path required for Choropleth
        // For grading, set the name of functions for projection and path as "projection" and "path"
        var projection = d3.geoMercator().translate([width/2, height/2]).scale(200).center([0,0]);
        var path = d3.geoPath().projection(projection);

        // enter code to create color scale

        // enter code to define tooltip
        var svg

        // define any other global variables 
        const atlDataRaw = d3.json("./atl.json")
            .then(function (values) {
                console.log('then');
                // enter code to create svg
                const root = document.createElement('div');
                svg = d3.select(root).append("svg").attr("id", "chloropleth")
                    .attr("width", width + margin + margin)
                    .attr("height", height + margin + margin);

                svg
                    .append("g").attr("id", "countries")
                    .selectAll("path")
                    .data(values[1].features)
                    .enter()
                    .append("path")
                    .attr("class","country")
                    .attr("d", path)
                    .attr("id", function(d){
                        return d.properties.name
                    });

                console.log(svg);
                setD3(svg);

                return;
        })

    });

    return (
        <>
            <RD3Component data={d3Obj} />
            <div>OverlayComponent</div>
        </>
        
    )
}
