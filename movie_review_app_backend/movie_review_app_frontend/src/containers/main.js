import '../App.css';

import React from "react"

import MovieCard from '../components/movie_card';
import {Grid, Typography, Box, CircularProgress} from "@material-ui/core"
import {Pagination} from "@material-ui/lab"
import Navbar from '../components/navbar';
import Loading from '../components/loading';

export default function Main() {

  const [page, setPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(1);
  const [isLoaded, setIsLoaded] = React.useState(false);
  const [curPageData, setCurPageData] = React.useState([]);

  const checkError = (response) => {
    if(response.status == 200) {
      return response.json()
    }
    else {
      throw Error("Error in retrieving movies list")
    }
  }

  const getCurPageData = async() => {

    // Load current page movie details from movies/ endpoint
    const endpoint = 'http://localhost:8000/movies/page' + page + '/';

    fetch(endpoint)
      .then(checkError).catch((error) => alert(error))
      .then((curPageDataObj) => {

        // Load all entries in the current page that are present in WatchedMoviesDatabase
        const endpoint = 'http://localhost:8000/database/checkPageInWatchedList/'

        fetch(endpoint, {
          method: 'POST',
          headers: {
              'Accept': 'application/json', 
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(curPageDataObj.results)
        })
        .then(checkError).catch((error) => alert(error))
        .then(watchedEntries => {

          // Load all entries in the current page that are present in MovieRatingDatabase
          const endpoint = 'http://localhost:8000/database/getCurrentPageMovieRatings/'

          fetch(endpoint, {
            method: 'POST',
            headers: {
                'Accept': 'application/json', 
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(curPageDataObj.results)
          })
          .then(checkError).catch((error) => alert(error))
          .then(movieRatingEntries => {

            // watchedEntries = JSON.parse(watchedEntries)
            // movieRatingEntries = JSON.parse(movieRatingEntries)
          
            // Set isWatched prop based on response from checkPageInWatchedList/ and rating prop based on response from getCurrentPageMovieRatings/
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
      <Loading/>
    )
  } 
  else {
    return (
      <div>
        <Navbar/>
        <Grid style={{marginTop: '8vh'}} container direction="row" align="center">
          {
            curPageData.map(movie => (
              <Grid key={movie.id} item xs={12} lg={3} style={{padding: '3vh'}}>
                <MovieCard key={movie.id} readOnlyRating={false} readOnlyWatchedIcon={false} id={movie.id} page={page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={true} showRating={true}/>
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

