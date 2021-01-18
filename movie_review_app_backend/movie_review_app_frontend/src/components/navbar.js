import {AppBar, Toolbar, Button, Typography} from "@material-ui/core"

export default function Navbar(props) {    
    return (
        <AppBar>
            <Toolbar>
                <Typography variant="h6" style={{flexGrow: 1}}>
                Movie Review App 
                </Typography>
                <Button color="inherit">
                Overview
                </Button>
            </Toolbar>
        </AppBar>
    )
}