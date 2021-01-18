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

        const endpoint = 'http://localhost:8000/database/getAllWatchedMoviesList/';

        fetch(endpoint)
            .then(response => response.json())
            .then(watchedMoviesList => {
                // console.log(watchedMoviesList)
                setWatchedMovieList(watchedMoviesList)

                const endpoint = 'http://localhost:8000/database/getAllRatedMoviesList/';

                fetch(endpoint)
                    .then(response => response.json())
                    .then(ratedMoviesList => {
                        console.log(ratedMoviesList)
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
                    <Grid item lg={12} xs={12}>
                        <h1> Overview </h1>
                        
                        <h2> Watched Movies List </h2>
                    </Grid>
                    {
                        watchedMoviesList.map(movie => (
                            <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
                                <MovieCard key={movie.id} id={movie.movieId} title={movie.movieName} overview={""} poster={movie.poster}/>
                            </Grid>
                        ))
                    }
                    <Grid item lg={12} xs={12}>
                        <h2> Rated Movies List </h2>
                    </Grid>
                    {
                        ratedMoviesList.map(movie => (
                            <Grid item xs={12} lg={3} style={{padding: '3vh'}}>
                                <MovieCard key={movie.id} id={movie.movieId} title={movie.movieName} rating={movie.movieRating} overview={""} poster={movie.poster}/>
                            </Grid>
                        ))
                    }
                </Grid>
            </div>
        )
    }
}