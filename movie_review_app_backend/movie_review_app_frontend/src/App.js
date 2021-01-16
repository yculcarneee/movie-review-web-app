import './App.css';

import React from "react"

import MovieCard from './components/movie_card';
import {Grid, Typography, Box} from "@material-ui/core"
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
        setCurPageData(curPageDataObj.results);
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
      <div>
        <h1> Loading... </h1>
      </div>
    )
  }
  else {
    return (
      <div>
        <Grid container direction="row" align="center">
          <Grid item lg={12} xs={12}>
            <h1> Movie Review App </h1>
          </Grid>
          {
            curPageData.map(movie => (
              <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
                <MovieCard id={movie.id} page={page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster}/>
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
