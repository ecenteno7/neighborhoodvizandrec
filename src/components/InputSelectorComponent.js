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

    // const activities = ["Biking", "Hiking", "Running", "Swimming", "Walking"];
    
    const activities = [
        "Wineries",
        "Transportation Services",
        "Taxis",
        "Food Markets",
        "Convenience Stores",
        "Grocery Stores",
        "Grocers Health Foods",
        "Seafood Markets",
        "Farm Markets",
        "Bakers Cake & Pie",
        "Doughnuts",
        "Miscellaneous Food Stores",
        "Electric Charging Station",
        "Children's Clothing",
        "Clothing Retail",
        "Sportswear",
        "Ice Cream Parlors",
        "Foods Carry Out",
        "(All) Restaurants",
        "Delicatessens",
        "Cafeterias",
        "Cafes",
        "Appetizers & Snacks Etc",
        "Subs & Sandwiches",
        "Theatres Dinner",
        "Coffee Shops",
        "Tea Rooms",
        "Juice Bars",
        "Restaurants Cyber Cafes",
        "Bars",
        "Discotheques",
        "Cocktail Lounges",
        "Pubs",
        "Comedy Clubs",
        "Karaoke Clubs",
        "Pharmacies",
        "Wines Retail",
        "Flea Markets",
        "Book Stores",
        "Toy Stores",
        "Gift Shops",
        "Art Galleries & Dealers",
        "Monuments",
        "Shopping Centers & Malls",
        "Hotels & Motels",
        "Cottages & Cabins",
        "Bed & Breakfasts",
        "Chalet & Cabin Rentals",
        "Skiing Centers & Resorts",
        "Resorts",
        "Villas",
        "Hostels",
        "Adventure Games & Activities",
        "Campgrounds",
        "Manicurists",
        "Barbers",
        "Movie Theatres",
        "Movie Theatres (drive-Ins)",
        "Theatres Live",
        "Concert Venues",
        "Entertainment Bureaus",
        "Bowling Centers",
        "Stadiums Arenas & Athletic Fields",
        "Race Tracks",
        "Horse Racing",
        "Health Clubs & Gyms",
        "Golf Courses-Public Or Private",
        "Casinos",
        "Arcades",
        "Amusement Places",
        "Water Parks",
        "Amusement Parks",
        "Recreation Centers",
        "Hockey Clubs",
        "Flying Clubs",
        "Beach & Cabana Clubs",
        "Sports Recreational",
        "Skating Rinks",
        "Bicycles Renting",
        "Baths Bath Houses Spas & Saunas",
        "Billiard Parlors",
        "Fairgrounds",
        "Historical Places",
        "Parks",
        "Picnic Grounds",
        "Horseback Riding",
        "Swimming Pools Public",
        "Tennis Courts Public",
        "Squash Courts Public",
        "Colleges & Universities",
        "Hiking Backpacking & Mountaineering Service",
        "Museums",
        "Planetariums",
        "Cultural Centres",
        "National Monuments",
        "Zoos",
        "Arboretums",
        "Aquariums Public",
        "Motoring Organisations",
        "Clubs",
        "Community Organizations",
        "(All) Places Of Worship",
        "Dance Clubs",
        "Beach",
        "Cave",
        "Forest",
        "Ridge",
        "Valley",
        "Bay",
        "Rapids",
        "Reservoir",
        "Swamp",
        "Bridge",
        "Building",
        "Dam",
        "Tower",
        "Tourist Attractions"
    ]

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
        // console.log(chicago_geojson);
        var regions = [];
        var regions = chicago_geojson.features.map((feature) => {
            return feature.properties.name;
        });
        // console.log(regions);
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
        console.log(process.env.REACT_APP_API_KEY)
        const req = {
            region: selectedRegion,
            activities: selectedActivities,
            startTime: timeBands[selectedTimeBand]['startTime'],
            endTime: timeBands[selectedTimeBand]['endTime'],
            places_of_interest: selectedActivities
        }

        setMode('map2')

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(req)
        };

        console.log(req)

        fetch('https://cors-everywhere.herokuapp.com/http://100.25.150.129:81/get-knn-result', requestOptions)
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
