import React from 'react'
import Paper from "@mui/material/Paper";
import PreferencesComponent from "./PreferencesComponent";
import Grid from "@mui/material/Grid";
import InputSelectorComponent from "./InputSelectorComponent";

export default function LeftContextCard({ mode }) {

    return (
        <>
            <Grid item>
                <Paper
                    elevation={24}
                    style={{
                        margin: 20,
                        width: 400,
                        height: 700,
                        maxHeight: 700,
                        overflow: "auto",
                    }}
                >
                    {(mode == "map1" ? 
                        <InputSelectorComponent></InputSelectorComponent>
                        : <PreferencesComponent></PreferencesComponent>)}
                </Paper>
            </Grid>
        </>
    )
}
