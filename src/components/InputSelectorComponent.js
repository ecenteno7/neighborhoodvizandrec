import React from 'react'

import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import Chip from "@mui/material/Chip";
import Box from "@mui/material/Box";
import OutlinedInput from "@mui/material/OutlinedInput";
import chicago_geojson from "../resources/chicago.json";

import { Button } from '@mui/material';

export default function InputSelectorComponent({setMode, setResult}) {
    const [selectedRegion, setSelectedRegion] = React.useState("");
    const [selectedActivities, setSelectedActivities] = React.useState([]);
    const [selectedTimeBand, setSelectedTimeBand] = React.useState("");

    const activities = ["Biking", "Hiking", "Running", "Swimming", "Walking"];

    const timeBands = {
        'Early Morning': {
            'startTime': '00:00',
            'endTime': '06:00'
        },
        'Morning': {
            'startTime': '05:59',
            'endTime': '11:59'
        },
        'Afternoon': {
            'startTime': '12:00',
            'endTime': '18:00'
        },
        'Night': {
            'startTime': '18:00',
            'endTime': '23:59'
        }
    }

    function getRegions() {
        console.log(chicago_geojson);
        var regions = [];
        var regions = chicago_geojson.features.map((feature) => {
            return feature.properties.name;
        });
        console.log(regions);
        return regions;
    }

    const getMenuItems = () => {
        var regions = getRegions();
        var menuItems = [];
        regions.forEach((region) => {
            menuItems.push(<MenuItem value={region}>{region}</MenuItem>);
        });
        return menuItems;
    };


    const handleRegionSelection = (event) => {
        setSelectedRegion(event.target.value);
    };

    const getTimeBands = () => {
        var menuItems = [];
        
        Object.keys(timeBands).forEach((time, index) => {
            menuItems.push(<MenuItem value={time}>{time}</MenuItem>);
        });

        return menuItems;
    };


    const handleSelectedTimeBand = (event) => {
        setSelectedTimeBand(event.target.value);
    };

    const handleActivitySelection = (event) => {
        const {
            target: { value },
        } = event;
        setSelectedActivities(typeof value === "string" ? value.split(",") : value);
    };

    const handleSubmit = (event) => {
        setResult('pending')
        const req = {
            region: selectedRegion,
            activities: selectedActivities,
            startTime: timeBands[selectedTimeBand]['startTime'],
            endTime: timeBands[selectedTimeBand]['endTime']
        }

        setMode('map2')

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(req)
        };

        console.log(req)

        fetch('http://localhost:81/get-knn-result', requestOptions)
            .then(response => response.json())
            .then(data => {console.log(data); setResult(data.body)});

    }

    return (
        <>
            <FormControl fullWidth style={{ margin: 20, width: 360 }}>
                <InputLabel id="demo-simple-select-label">
                    Region
                </InputLabel>
                <Select
                    labelId="region-select-label"
                    id="region-select"
                    value={selectedRegion}
                    label="Age"
                    onChange={handleRegionSelection}
                >
                    {getMenuItems()}
                </Select>
            </FormControl>
            <FormControl fullWidth style={{ margin: 20, width: 360 }}>
                <InputLabel id="activity-select-label">Activity</InputLabel>
                <Select
                    labelId="activity-select-label"
                    id="activity-select"
                    multiple
                    value={selectedActivities}
                    onChange={handleActivitySelection}
                    input={
                        <OutlinedInput
                            id="select-multiple-chip"
                            label="activity-select-label"
                        />
                    }
                    renderValue={(selected) => (
                        <Box
                            sx={{ display: "flex", flexWrap: "wrap", gap: 0.5 }}
                        >
                            {selected.map((value) => (
                                <Chip key={value} label={value} />
                            ))}
                        </Box>
                    )}
                >
                    {activities.map((activity) => (
                        <MenuItem key={activity} value={activity}>
                            {activity}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
            <FormControl fullWidth style={{ margin: 20, width: 360 }}>
                <InputLabel id="timeBand-select-label">Time</InputLabel>
                <Select
                    labelId="timeBand-select-label"
                    id="timeBand-select"
                    value={selectedTimeBand}
                    label="Age"
                    onChange={handleSelectedTimeBand}
                >
                    {getTimeBands()}
                </Select>
            </FormControl>

            <Button variant="contained" onClick={handleSubmit}>SUBMIT</Button>
        </>
    )
}
