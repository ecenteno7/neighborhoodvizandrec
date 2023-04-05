import React, { useState } from "react";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";

export default function PreferencesComponent() {
  const res = {
    neighborhoods: [
      {
        key: "West Midtown",
        description:
          "West Midtown, also known as Westside,[1] is a colloquial area, comprising many historical neighborhoods located in Atlanta, Georgia. Once largely industrial, West Midtown is now the location of urban lofts, art galleries, live music venues, retail and restaurants.",
        pointsOfInterest: [
          "Ormsby's",
          "Puttshack",
          "Fire Maker Brewing Company",
        ],
      },
      {
        key: "East Atlanta",
        description:
          "East Atlanta is a neighborhood on the east side of Atlanta, Georgia, United States. The name East Atlanta Village primarily refers to the neighborhood's commercial district.",
        pointsOfInterest: ["Ramen Place", "Coffee Shop", "Brewery"],
      },
      {
        key: "Candler Park",
        description:
          "Leafy Candler Park is a quiet, largely residential neighborhood, with late-19th- and early-20th-century homes. Community events are often held at landscaped Candler Park, which has a golf course, playground and swimming pool. Trails wind past outdoor art installations in adjacent Freedom Park. McLendon Avenue is home to laid-back cafes and restaurants that serve Southern food.",
        pointsOfInterest: ["Coffee", "Bar", "Movie Theater"],
      },
    ],
  };

  const [preferences, setPreferences] = useState(res);

  const renderResults = () => {
    return res.neighborhoods.map((pointOfInterest) => {
      return (
        <Grid item xs={10}>
          <Paper elevation={3}>
            <div
              style={{
                paddingLeft: 10,
                paddingRight: 10,
                paddingTop: 0,
                paddingBottom: 10,
              }}
            >
              <h2>{pointOfInterest.key}</h2>
              <em>Description</em>
              <p>{pointOfInterest.description}</p>
              <em>Areas you may enjoy:</em>
              {pointOfInterest.pointsOfInterest.map((feature) => {
                return <li>{feature}</li>;
              })}
            </div>
          </Paper>
        </Grid>
      );
    });
  };

  return (
    <>
      <Grid container spacing={0} marginLeft={3}>
        {renderResults()}
      </Grid>
    </>
  );
}
