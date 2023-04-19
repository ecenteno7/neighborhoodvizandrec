import React, {useEffect} from "react";
import Grid from "@mui/material/Grid";
import { CircularProgress, Box } from "@mui/material";
import InputSelectorCard from "./components/LeftContextCard";
import MapCard from "./components/MapCard";
import PreferencesComponent from "./components/PreferencesComponent";
import LeftContextCard from "./components/LeftContextCard";

function App() {

  const [selectedMap, setSelectedMap] = React.useState("map1");
  const [res, setResult] = React.useState(null);

  const [fact, setFact] = React.useState("Loading...");

  const sleep = (time) => {
    return new Promise((resolve) => setTimeout(resolve, time));
}

  useEffect(() => {
    const intervalId = setInterval(() => {
      fetch("https://uselessfacts.jsph.pl/random.json?language=en")
        .then((res) => res.json())
        .then((data) => {
          setFact(data.text);
        });
    }, 10000)
  return () => clearInterval(intervalId);
  }, []);

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
            <h1>Travel Recommendation System</h1>
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
            {res == null &&
              <>
                <p style={{"width": "50%", "text-align": "center"}}>Please select a neighborhood in <em><strong>Chicago</strong></em> that you enjoy hanging out in, some types of activities in that neighborhood that you enjoy, and the time you like to hangout there.</p>
                <Box width="100%"/>
              </>
              
            }
            {res != null && res != 'pending' &&
              <>
                <p style={{"width": "50%", "text-align": "center"}}>Based off of your selections, here are some recommendations for your trip to <em><strong>Washington D.C.</strong></em></p>
                <Box width="100%"/>
              </>
              
            }
            {res == 'pending' ?
              (<>
                  
                  <Grid item>
                    <h4>Loading your Washington D.C. recommendations...</h4>
                  </Grid>

                  <Box width="100%"/>
                  
                  <Grid item>
                    <p>Hang tight, and enjoy some fun facts in the meantime.</p>
                  </Grid>

                  <Box width="100%"/>
                  <Grid item style={{"width": "50%", "alignItems": "center"}}>
                    <p style={{"textAlign": "center"}}><em>{fact}</em></p>
                  </Grid>

                  <Box width="100%" height="33%"/>
                  <Grid item>
                    <CircularProgress />
                  </Grid>
                </>
              ) :
              <>
                <LeftContextCard mode={selectedMap} setMode={setSelectedMap} res={res} setResult={setResult} />
                <MapCard mode={selectedMap} setMode={setSelectedMap} res={res} />
              </>}
          </Grid>
        </Grid >
      </div>
    </>
  );
}

export default App;
