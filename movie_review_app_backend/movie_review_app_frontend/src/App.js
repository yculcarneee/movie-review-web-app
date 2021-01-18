import './App.css';

import React from "react"

import MovieCard from './components/movie_card';
import {Grid, Typography, Box, CircularProgress, AppBar, Toolbar} from "@material-ui/core"
import {Pagination} from "@material-ui/lab"

function App() {

  const [page, setPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(1);
  const [isLoaded, setIsLoaded] = React.useState(false);
  const [curPageData, setCurPageData] = React.useState([]);

  const getCurPageData = async() => {

    const endpoint = 'http://localhost:8000/movies/page' + page;

    fetch(endpoint)
      .then(response => response.json())
      .then((curPageDataObj) => {

        const endpoint = 'http://localhost:8000/database/checkPageInWatchedList/'

        fetch(endpoint, {
          method: 'POST',
          headers: {
              'Accept': 'application/json', 
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(curPageDataObj.results)
        })
        .then(response => response.json())
        .then(watchedEntries => {

          const endpoint = 'http://localhost:8000/database/getCurrentPageMovieRatings/'

          fetch(endpoint, {
            method: 'POST',
            headers: {
                'Accept': 'application/json', 
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(curPageDataObj.results)
          })
          .then(response => response.json())
          .then(movieRatingEntries => {

            watchedEntries = JSON.parse(watchedEntries)
            movieRatingEntries = JSON.parse(movieRatingEntries)
          
            curPageDataObj.results.forEach(entry => {
              if(entry['id'] in watchedEntries && watchedEntries[entry['id']]) {
                entry['isWatched'] = true;
              }
              else {
                entry['isWatched'] = false;
              }
              entry['rating'] = movieRatingEntries[entry['id']]
            })
            setCurPageData(curPageDataObj.results)
          })
        })
      
        setTotalPages(curPageDataObj.total_pages);
        setIsLoaded(true);
      })
  }

  const handleChange = (event, value) => {
    setPage(value);
  };

  React.useEffect(() => {
    setIsLoaded(false);
    getCurPageData();
  }, [page])

  if(!isLoaded) {
    return (
      <Grid container direction="row" justify="center">
        <Grid item>
          <h1> Loading... </h1>
          <CircularProgress size="7vw"/>
        </Grid>
      </Grid>
    )
  } 
  else {
    return (
      <div>
        <AppBar>
          <Toolbar>
              Movie Review App 
          </Toolbar>
        </AppBar>
        <Grid style={{marginTop: '10vh'}} container direction="row" align="center">
          <Grid item lg={12} xs={12}>
            
          </Grid>
          {
            curPageData.map(movie => (
              <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
                <MovieCard key={movie.id} id={movie.id} page={page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched}/>
              </Grid>
            ))
          }
        </Grid>
        <Box my={2} display="flex" justifyContent="center">
          <Typography>Page: {page}</Typography>
        </Box>
        <Box my={2} display="flex" justifyContent="center">
          <Pagination count={totalPages} page={page} onChange={handleChange} />        
        </Box>
      </div>
    );
  }
}

export default App;
