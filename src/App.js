import * as React from "react";
import MapComponent from "./components/MapComponent";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import atlanta_geojson from "./resources/atlanta.json";
import chicago_geojson from "./resources/chicago.json";
import PreferencesComponent from "./components/PreferencesComponent";

function App() {
  const [selectedMap, setSelectedMap] = React.useState("map1");

  const handleMapSelection = (event, newSelectedMap) => {
    setSelectedMap(newSelectedMap);
  };

  return (
    <div>
      <ToggleButtonGroup
        value={selectedMap}
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
      {selectedMap == "map1" && (
        <MapComponent
          geojson={atlanta_geojson}
          initialViewState={{
            longitude: -84.376656,
            latitude: 33.749542,
            zoom: 10,
          }}
        ></MapComponent>
      )}
      {selectedMap == "map2" && (
        <>
          <MapComponent
            geojson={chicago_geojson}
            initialViewState={{
              longitude: -87.63238,
              latitude: 41.84372,
              zoom: 9,
            }}
          ></MapComponent>
          <PreferencesComponent></PreferencesComponent>
        </>
      )}
    </div>
  );
}

export default App;
