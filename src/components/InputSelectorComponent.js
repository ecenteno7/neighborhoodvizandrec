import React from 'react'

import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import Chip from "@mui/material/Chip";
import Box from "@mui/material/Box";
import OutlinedInput from "@mui/material/OutlinedInput";
import atlanta_geojson from "../resources/atlanta.json";
import chicago_geojson from "../resources/chicago.json";

export default function InputSelectorComponent() {
    const [selectedRegion, setSelectedRegion] = React.useState("");
    const [selectedActivities, setSelectedActivities] = React.useState([]);

    const activities = ["Biking", "Hiking", "Running", "Swimming", "Walking"];

    function getRegions() {
        console.log(atlanta_geojson);
        var regions = [];
        var regions = atlanta_geojson.features.map((feature) => {
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

    const handleActivitySelection = (event) => {
        const {
            target: { value },
        } = event;
        setSelectedActivities(typeof value === "string" ? value.split(",") : value);
    };
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
        </>
    )
}
