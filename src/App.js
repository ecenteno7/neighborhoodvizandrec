import * as React from 'react';
import MapComponent from './components/MapComponent';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import Paper from '@mui/material/Paper';
import Chip from '@mui/material/Chip';
import Box from '@mui/material/Box';
import OutlinedInput from '@mui/material/OutlinedInput';
import atlanta_geojson from './resources/atlanta.json';
import chicago_geojson from './resources/chicago.geojson';

function App() {
  const [selectedMap, setSelectedMap] = React.useState('map1');
  const [selectedRegion, setSelectedRegion] = React.useState('');
  const [selectedActivities, setSelectedActivities] = React.useState([]);
  
  const activities = ['Biking', 'Hiking', 'Running', 'Swimming', 'Walking'];

  function getRegions() {
    console.log(atlanta_geojson);
    var regions = [];
    var regions = atlanta_geojson.features.map((feature) => {
      return feature.properties.name;
    });
    console.log(regions);
    return regions;
  };

  const getMenuItems = () => {
    var regions = getRegions();
    var menuItems = [];
    regions.forEach(region => {
      menuItems.push(<MenuItem value={region}>{region}</MenuItem>);
    });
    return menuItems;
  };

  const handleMapSelection = (event, newSelectedMap) => {
    setSelectedMap(newSelectedMap);
  };

  const handleRegionSelection = (event) => {
    setSelectedRegion(event.target.value);
  };

  const handleActivitySelection = (event) => {
    const {
      target: { value },
    } = event;
    setSelectedActivities(
      typeof value === 'string' ? value.split(',') : value,
    );
  };
  
  return (
    <div style={{display: 'flex', margin: 'auto'}}>
      <Paper elevation={24} style={{margin: 20, width: 400, height: 700}}>
        <FormControl fullWidth style={{margin: 20, width: 360}}>
          <InputLabel id="demo-simple-select-label">Region</InputLabel>
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
        <FormControl fullWidth style={{margin: 20, width: 360}}>
          <InputLabel id="activity-select-label">Activity</InputLabel>
          <Select
            style={{marginTop: 20}}
            labelId="activity-select-label"
            id="activity-select"
            multiple
            value={selectedActivities}
            onChange={handleActivitySelection}
            input={<OutlinedInput id="select-multiple-chip" label="activity-select-label" />}
            renderValue={(selected) => (
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                {selected.map((value) => (
                  <Chip key={value} label={value} />
                ))}
              </Box>
            )}
          >
            {activities.map((activity) => (
              <MenuItem
                key={activity}
                value={activity}
              >
                {activity}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Paper>
      <Paper elevation={24} style={{margin: 20, width: 700, height: 700}}>
        <ToggleButtonGroup
          value={selectedMap}
          exclusive
          onChange={handleMapSelection}
          style={{width: 500, height: 25, margin: 'auto', padding: 20}}
        >
          <ToggleButton value="map1" aria-label="left aligned">
            <p>Map 1</p>
          </ToggleButton>
          <ToggleButton value="map2" aria-label="centered">
            <p>Map 2</p>
          </ToggleButton>
        </ToggleButtonGroup>
        {
          selectedMap == 'map1' &&
          <MapComponent
            geojson={atlanta_geojson}
            initialViewState={{
              longitude: -84.376656,
              latitude: 33.749542,
              zoom: 10
            }}>
          </MapComponent>
        }
        {
          selectedMap == 'map2' &&
          <MapComponent
            geojson={chicago_geojson}
            initialViewState={{
              longitude: -87.63238,
              latitude: 41.84372,
              zoom: 9
            }}>
          </MapComponent>
        }
      </Paper>
    </div>
  );
}

export default App;