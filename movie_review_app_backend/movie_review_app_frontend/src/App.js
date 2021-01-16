import './App.css';

import React from "react"

import MovieCard from './components/movie_card';
import {Grid, Typography, Box} from "@material-ui/core"
import {Pagination} from "@material-ui/lab"

function App() {

  const [page, setPage] = React.useState(1);
  const handleChange = (event, value) => {
    setPage(value);
  };

  return (
    <div className="App">
      <Grid container direction="row" align="center">
        <Grid item lg={12}>
          <h1> Movie Review App </h1>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="1" page={page} />
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="2" page={page}/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="3" page={page}/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="4" page={page}/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="5" page={page}/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="6" page={page}/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="7" page={page}/>
        </Grid>
        <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
          <MovieCard id="8" page={page}/>
        </Grid>
      </Grid>
      <Box my={2} display="flex" justifyContent="center">
        <Typography>Page: {page}</Typography>
      </Box>
      <Box my={2} display="flex" justifyContent="center">
        <Pagination count={10} page={page} onChange={handleChange} />        
      </Box>
    </div>
  );
}

export default App;
