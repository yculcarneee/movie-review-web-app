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
                title={props.title}
                subheader={props.release_date}
            />
            <CardMedia
                component="img"
                height="300px"
                image={props.poster}
                title={props.title}
            />
            <CardContent>
                <Typography variant="body2" color="textSecondary" component="p" align="justify">
                    {props.overview}
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