import React from "react";

import Navbar from '../components/navbar';
import MovieCard from '../components/movie_card';

import {Grid, CircularProgress} from "@material-ui/core"
import Loading from "../components/loading";

export default function Overview() {

    const [isLoaded, setIsLoaded] = React.useState(false);
    const [watchedMoviesList, setWatchedMovieList] = React.useState([]);
    const [ratedMoviesList, setRatedMovieList] = React.useState([]);

    const getCurPageData = async() => {

        // Load all entries present in WatchedMoviesDatabase from getAllWatchedMoviesList/ endpoint
        const endpoint = 'http://localhost:8000/database/getAllWatchedMoviesList/';

        fetch(endpoint)
            .then(response => response.json())
            .then(watchedMoviesList => {
                // console.log(watchedMoviesList)
                setWatchedMovieList(watchedMoviesList)

                // Load all entries present in MovieRatingDatabase from getAllRatedMoviesList/ endpoint
                const endpoint = 'http://localhost:8000/database/getAllRatedMoviesList/';

                fetch(endpoint)
                    .then(response => response.json())
                    .then(ratedMoviesList => {
                        // console.log(ratedMoviesList)
                        setRatedMovieList(ratedMoviesList)
                        setIsLoaded(true);
                    })
            })
    }

    React.useEffect(() => {
        setIsLoaded(false);
        getCurPageData();
    }, [])

    if(!isLoaded) {
        return(
            <Loading/>
        )
    }
    else {
        return (
            <div>
                <Navbar/>
                <Grid style={{marginTop: '8vh'}} container direction="row" align="center">
                    <Grid key="Watched Movies List Heading" item lg={12} xs={12}>
                        <h1> Watched Movies List </h1>
                    </Grid>
                    {
                        watchedMoviesList.map(movie => (
                            <Grid item key={"watchedMovies-"+movie.movieId} xs={12} lg={3} style={{padding: '3vh'}}>
                                <MovieCard key={movie.movieId} readOnlyWatchedIcon={true} id={movie.movieId} title={movie.movieName} overview={movie.movieOverview} release_date={movie.movieReleaseDate} poster={movie.moviePoster} isWatched={true} showWatchedIcon={true} showRating={false}/>
                            </Grid>
                        ))
                    }
                    <Grid key="Rated Movies List Heading" item lg={12} xs={12}>
                        <h1> Rated Movies List </h1>
                    </Grid>
                    {
                        ratedMoviesList.map(movie => (
                            <Grid item key={"ratedMovies-"+movie.movieId} xs={12} lg={3} style={{padding: '3vh'}}>
                                <MovieCard key={movie.movieId} readOnlyRating={true} id={movie.movieId} title={movie.movieName} overview={movie.movieOverview} release_date={movie.movieReleaseDate} poster={movie.moviePoster} rating={movie.movieRating} showWatchedIcon={false} showRating={true}/>
                            </Grid>
                        ))
                    }
                </Grid>
            </div>
        )
    }
}