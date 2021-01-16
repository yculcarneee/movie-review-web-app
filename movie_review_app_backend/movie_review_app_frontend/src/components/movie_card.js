import React from 'react';
import {Card, CardHeader, CardMedia, CardContent, CardActions, Typography, IconButton} from '@material-ui/core'
import VisibilityIcon from '@material-ui/icons/Visibility';
import Rating from '@material-ui/lab/Rating';

export default function MovieCard(props) {

    const [watchedMovieButtonColor, setWatchedMovieButtonColor] = React.useState('grey')
    const [rating, setRating] = React.useState(2);

    const toggleWatchedMovieButtonColor = () => {
        if(watchedMovieButtonColor === 'grey') {
            setWatchedMovieButtonColor('#ffb400')
        }
        else {
            setWatchedMovieButtonColor('grey')
        }
    }

    return (
        <Card style={{maxWidth: '340px', maxHeight: '800px'}}>
            <CardHeader
                title="Movie Name"
                subheader="Release Date - September 14, 2016"
            />
            <CardMedia
                component="img"
                height="300px"
                image="https://placeimg.com/340/300/any"
                title="Movie Title"
            />
            <CardContent>
                <Typography variant="body2" color="textSecondary" component="p">
                    Card Number: {props.id} <br/>
                    Page Number: {props.page} <br/>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </Typography>
            </CardContent>
            <CardActions disableSpacing>
                <IconButton style={{color: watchedMovieButtonColor}} onClick={()=>{toggleWatchedMovieButtonColor()}}>
                    <VisibilityIcon />
                </IconButton>
                <Rating name={props.id} value={rating} onChange={(event, newRating) => {setRating(newRating);}}/>
            </CardActions>
        </Card>
    )
}