import {Grid, CircularProgress} from "@material-ui/core"

export default function Loading() {
    return (
        <div>
            <Grid container direction="row" justify="center">
                <Grid item>
                    <h1> Loading... </h1>
                    <CircularProgress size="7vw"/>
                </Grid>
            </Grid>
        </div>
    )
}