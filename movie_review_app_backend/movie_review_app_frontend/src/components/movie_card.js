import React from 'react';
import {Card, CardHeader, CardMedia, CardContent, CardActions, Typography, IconButton, Link} from '@material-ui/core'
import VisibilityIcon from '@material-ui/icons/Visibility';
import Rating from '@material-ui/lab/Rating';

export default function MovieCard(props) {

    const [needsExpansion, setNeedsExpansion] = React.useState(false);
    const [isExpanded, setIsExpanded] = React.useState(false);

    const [overviewText, setOverviewText] = React.useState('')
    const [expandedOverviewText, setExpandedOverviewText] = React.useState('')

    const [watchedMovieButtonColor, setWatchedMovieButtonColor] = React.useState('grey')
    const [rating, setRating] = React.useState(2);

    const toggleWatchedMovieButtonColor = async(id, title) => {
        if(watchedMovieButtonColor === 'grey') {
            setWatchedMovieButtonColor('#ffb400')

            const endpoint = 'http://localhost:8000/database/addToWatchedList/'

            const data = {
                movieId: id,
                movieName: title,
            }

            fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json', 
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }
        else {
            setWatchedMovieButtonColor('grey')

            const endpoint = 'http://localhost:8000/database/removeFromWatchedList/'

            const data = {
                movieId: id
            }

            fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json', 
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }
    }

    const handleRating = (rating) => {
        const endpoint = 'http://localhost:8000/database/updateMovieRating/'

        const data = {
            movieId: props.id,
            movieName: props.title,
            movieRating: rating
        }

        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Accept': 'application/json', 
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        setRating(rating);
    }

    const toggleOverviewText = () => {
        setIsExpanded(!isExpanded)
    }

    React.useEffect(() => {
        setRating(props.rating)
        if(props.isWatched) {
            setWatchedMovieButtonColor('#ffb400')
        }
        if(props.overview.length > 150) {
            setNeedsExpansion(true);
            setExpandedOverviewText(props.overview.substring(0, 150));
        }
        setOverviewText(props.overview)
    }, [overviewText])

    return (
        <Card style={{maxWidth: '340px', minHeight: '500px'}}>
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
                    {!isExpanded && needsExpansion ? expandedOverviewText : overviewText} 
                    {needsExpansion ? 
                        <Link onClick={()=>toggleOverviewText()}> 
                            {isExpanded ? " Read less..." : " Read more..." } 
                        </Link> : 
                        null}
                </Typography>
                
            </CardContent>
            <CardActions disableSpacing>
                <IconButton style={{color: watchedMovieButtonColor}} onClick={()=>{toggleWatchedMovieButtonColor(props.id, props.title)}}>
                    <VisibilityIcon />
                </IconButton>
                <Rating name={props.id} value={rating} onChange={(event, newRating) => {handleRating(newRating)}}/>
            </CardActions>
        </Card>
    )
}