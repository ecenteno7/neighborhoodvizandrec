import React from 'react'

import MapComponent from "./MapComponent";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import Paper from "@mui/material/Paper";
import atlanta_geojson from "../resources/atlanta.json";
import chicago_geojson from "../resources/chicago.json";
import Grid from "@mui/material/Grid";

export default function MapCard({ mode, setMode }) {

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
                    <ToggleButtonGroup
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
                    </ToggleButtonGroup>
                    {mode == "map1" && (
                        <MapComponent
                            geojson={chicago_geojson}
                            initialViewState={{
                                longitude: -87.63238,
                                latitude: 41.84372,
                                zoom: 9,
                            }}
                        ></MapComponent>
                    )}
                    {mode == "map2" && (
                        <MapComponent
                            geojson={atlanta_geojson}
                            initialViewState={{
                                longitude: -84.376656,
                                latitude: 33.749542,
                                zoom: 10,
                            }}
                        ></MapComponent>
                    )}
                </Paper>
            </Grid>
        </>
    )
}
