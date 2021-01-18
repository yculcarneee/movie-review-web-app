import {Link} from 'react-router-dom'
import {AppBar, Toolbar, Button, Typography} from "@material-ui/core"

export default function Navbar(props) {    
    return (
        <AppBar>
            <Toolbar>
                <div style={{flexGrow: 1}}>
                    <Button component={Link} to="/" color="inherit" style={{textTransform: 'none'}}>
                        <Typography variant="h5">
                            Movie Review App 
                        </Typography>  
                    </Button>
                </div>
                <Button component={Link} to="/overview" color="inherit" style={{textTransform: 'none'}}>
                    Overview
                </Button>
            </Toolbar>
        </AppBar>
    )
}