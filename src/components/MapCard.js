import React from 'react'

import MapComponent from "./MapComponent";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import Paper from "@mui/material/Paper";
import washingtondc_geojson from "../resources/washingtondc.json";
import chicago_geojson from "../resources/chicago.json";
import Grid from "@mui/material/Grid";

export default function MapCard({ mode, setMode, res }) {

    const handleMapSelection = (event, newSelectedMap) => {
        console.log(newSelectedMap)
        setMode(newSelectedMap);
    };

    return (
        <>
            <Grid item>
                <Paper
                    elevation={24}
                    style={{ margin: 20, width: 700, height: 700 }}
                >
                    {/* <ToggleButtonGroup
                        value={mode}
                        exclusive
                        onChange={handleMapSelection}
                        style={{ width: 500, height: 25, margin: "auto", padding: 20 }}
                    >
                        <ToggleButton value="map1" aria-label="left aligned">
                            <p>Map 1</p>
                        </ToggleButton>
                        <ToggleButton value="map2" aria-label="centered">
                            <p>Map 2</p>
                        </ToggleButton>
                    </ToggleButtonGroup> */}
                    {res == null && (
                        <MapComponent
                            geojson={chicago_geojson}
                            initialViewState={{
                                longitude: -87.63238,
                                latitude: 41.84372,
                                zoom: 9,
                            }}
                            res={res}
                        ></MapComponent>
                    )}
                    {res != null && (
                        <MapComponent
                            geojson={washingtondc_geojson}
                            initialViewState={{
                                longitude: -77.036600,
                                latitude: 38.907018, 
                                zoom: 10,
                            }}
                            res={res}
                        ></MapComponent>
                    )}
                </Paper>
            </Grid>
        </>
    )
}
