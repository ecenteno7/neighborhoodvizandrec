import React from "react";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import PieChartComponent from "./PieChartComponent";

export default function PreferencesComponent({res}) {

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
              {/* <em>Locations to try out:</em>
              {pointOfInterest.pointsOfInterest.map((feature) => {
                return <li>{feature}</li>;
              })} */}
              <em>Places of Interest Breakdown</em>
              <PieChartComponent 
                style={{
                  paddingLeft: 10,
                  paddingRight: 10,
                  paddingTop: 0,
                  paddingBottom: 10,
                }}
                neighborhood={pointOfInterest.key}
                data={pointOfInterest.chartData}
              >
              </PieChartComponent>
              <p>Shown above is the breakdown of counts of locations that you prefer based off of your activity selections. "Other" denotes activities that you did not select.</p>
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
