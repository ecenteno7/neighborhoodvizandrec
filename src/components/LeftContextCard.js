import React from 'react'
import Paper from "@mui/material/Paper";
import PreferencesComponent from "./PreferencesComponent";
import Grid from "@mui/material/Grid";
import InputSelectorComponent from "./InputSelectorComponent";

export default function LeftContextCard({ mode, setMode, res, setResult }) {

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
                        <InputSelectorComponent setMode={setMode} setResult={setResult}></InputSelectorComponent>
                        : <PreferencesComponent res={res}></PreferencesComponent>)}
                </Paper>
            </Grid>
        </>
    )
}
