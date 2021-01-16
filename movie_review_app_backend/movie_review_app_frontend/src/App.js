import './App.css';
import MovieCard from './components/movie_card';
import {Grid} from "@material-ui/core"

function App() {

  return (
    <div>
      <Grid container direction="row" align="center">
        <Grid item lg={12}>
          <h1> Movie Review App </h1>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="1" />
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="2"/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="3"/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="4"/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="5"/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="6"/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="7"/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="8"/>
        </Grid>
      </Grid>

    </div>
  );
}

export default App;
