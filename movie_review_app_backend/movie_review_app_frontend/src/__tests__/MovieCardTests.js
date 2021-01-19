import { render, screen } from '@testing-library/react';
import MovieCard from '../components/movie_card';


describe('MovieCard Component', () => {
  const movie = {
    'page': 1,
    'id': 1,
    'title': 'Dummy Movie Name',
    'overview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam',
    'release_date': '2020-12-16',
    'poster': 'https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg',
    'rating': 4,
    'isWatched': true,
    'showWatchedIcon': true,
    'showRating': true,
    'readOnlyRating': false,
    'readOnlyWatchedIcon': false
  }
  
  test('Renders Movie Title', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.getByText(movie.title)).toBeInTheDocument()
  });

  test('Renders Movie Release Date', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.getByText(movie.release_date)).toBeInTheDocument()
  });

  test('Renders Movie Poster', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);

    expect(screen.getByRole('img')).toBeInTheDocument()
    expect(screen.getByRole('img').src).toBe(movie.poster)
  });

  test('Movie Poster content matches passed one', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);

    expect(screen.getByRole('img').src).toBe(movie.poster)
  });
  
  test('Renders Movie Overview', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.getByText(movie.overview)).toBeInTheDocument()
  });

  test('Renders Watched Button', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.getByRole('button')).toBeInTheDocument()
  });

  test('Watched Button is disabled when readOnlyWatchedIcon is set to True', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={true} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.getByRole('button')).toBeDisabled()
  });

  test('Watched Button has #ffb400 color when isWatched prop is set to true', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyRating} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.getByRole('button')).toHaveStyle('color: #ffb400')
  });

  test('Watched Button does not render when showWatchedIcon is set to False', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyRating} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={false} showRating={movie.showRating} />);
    
    expect(screen.queryByRole('button')).toBeNull()
  });

  test('Renders Rating component', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.queryAllByRole('radio')).not.toBeNull()
  });

  test('Rating component is disabled when readOnlyRating prop is set to True', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={true} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={movie.showRating} />);
    
    expect(screen.queryByRole('radio')).toBeNull()
    expect(screen.getByLabelText(movie.rating + ' Stars')).toBeInTheDocument()
  });

  test('Rating component is does not render when showRating prop is set to False', async() => {
    render(<MovieCard key={movie.id} readOnlyRating={movie.readOnlyRating} readOnlyWatchedIcon={movie.readOnlyWatchedIcon} id={movie.id} page={movie.page} title={movie.title} overview={movie.overview} release_date={movie.release_date} poster={movie.poster} rating={movie.rating} isWatched={movie.isWatched} showWatchedIcon={movie.showWatchedIcon} showRating={false} />);
    
    expect(screen.queryByRole('radio')).toBeNull()
    expect(screen.queryByLabelText(movie.rating + ' Stars')).toBeNull()
  });
})
