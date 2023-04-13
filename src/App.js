import * as React from "react";
import Grid from "@mui/material/Grid";
import InputSelectorCard from "./components/LeftContextCard";
import MapCard from "./components/MapCard";
import PreferencesComponent from "./components/PreferencesComponent";
import LeftContextCard from "./components/LeftContextCard";

function App() {

  const [selectedMap, setSelectedMap] = React.useState("map1");

  return (
    <>
      <div
        style={{
          display: "flex",
          margin: "auto",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Grid
          container
          spacing={0}
          marginLeft={3}
          style={{
            display: "flex",
            margin: "auto",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Grid item>
            <h1>Header</h1>
          </Grid>
          <Grid
            container
            item
            spacing={0}
            marginLeft={3}
            style={{
              display: "flex",
              margin: "auto",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
              <LeftContextCard mode={selectedMap} />
              <MapCard mode={selectedMap} setMode={setSelectedMap}/>
          </Grid>
        </Grid >
      </div>
    </>
  );
}

export default App;
