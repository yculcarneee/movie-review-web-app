import {render, screen, waitForElementToBeRemoved} from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'

import Overview from '../containers/overview'

import { enableFetchMocks } from 'jest-fetch-mock'

enableFetchMocks()

describe('Overview Page', () => {

    beforeEach(() => {
        fetch.resetMocks()
    })

    const getAllWatchedMoviesListResponse = [
        {
            "movieId": 716703,
            "movieName": "Alpha Beta",
            "movieOverview": "Lorem Ipsum Dolor Sit Amet",
            "movieReleaseDate": "2020-12-17",
            "moviePoster": "https://image.tmdb.org/t/p/w500/zjGrlEuENSjRZGWc8N10zq3Jjkq1.jpg"
        },
        {
            "movieId": 716704,
            "movieName": "Gamma Theta",
            "movieOverview": "Lorem Ipsum Dolor Sit Amet Dos",
            "movieReleaseDate": "2021-12-17",
            "moviePoster": "https://image.tmdb.org/t/p/w500/zjGrlEuENSjRZGWc8N10zq3Jjkq2.jpg"
        }
    ]

    const getAllRatedMoviesListResponse = [
        {
            "movieId": 716705,
            "movieName": "Delta Epslion",
            "movieOverview": "Lorem Ipsum Dolor Sit Tres",
            "movieReleaseDate": "2022-12-17",
            "moviePoster": "https://image.tmdb.org/t/p/w500/zjGrlEuENSjRZGWc8N10zq3Jjkq3.jpg",
            "movieRating": 4
        },
        {
            "movieId": 716706,
            "movieName": "Zeta Iota",
            "movieOverview": "Lorem Ipsum Dolor Sit Amet Cuatro",
            "movieReleaseDate": "2023-12-17",
            "moviePoster": "https://image.tmdb.org/t/p/w500/zjGrlEuENSjRZGWc8N10zq3Jjkq4.jpg",
            "movieRating": 5

        }
    ]

    test('Renders Navbar component', async() => {

        fetch.mockResponseOnce(JSON.stringify(getAllWatchedMoviesListResponse))
            .mockResponseOnce(JSON.stringify(getAllRatedMoviesListResponse))

        render(
            <BrowserRouter>
                <Overview/>
            </BrowserRouter>
        )

        await waitForElementToBeRemoved(screen.getByText('Loading...'))

        expect(screen.getByRole('banner')).toBeInTheDocument()
        expect(screen.getByText('Movie Review App')).toBeInTheDocument()
        expect(screen.getByText('Overview')).toBeInTheDocument()
    })

    test('Renders Watched Movies List Section fully', async() => {

        fetch.mockResponseOnce(JSON.stringify(getAllWatchedMoviesListResponse))
            .mockResponseOnce(JSON.stringify(getAllRatedMoviesListResponse))

        render(
            <BrowserRouter>
                <Overview/>
            </BrowserRouter>
        )

        await waitForElementToBeRemoved(screen.getByText('Loading...'))

        expect(screen.getByText('Watched Movies List')).toBeInTheDocument()

        expect(screen.getByText(getAllWatchedMoviesListResponse[0].movieName)).toBeInTheDocument()
        expect(screen.getByText(getAllWatchedMoviesListResponse[1].movieName)).toBeInTheDocument()

        expect(screen.getByText(getAllWatchedMoviesListResponse[0].movieOverview)).toBeInTheDocument()
        expect(screen.getByText(getAllWatchedMoviesListResponse[1].movieOverview)).toBeInTheDocument()

        expect(screen.getByText(getAllWatchedMoviesListResponse[0].movieReleaseDate)).toBeInTheDocument()
        expect(screen.getByText(getAllWatchedMoviesListResponse[1].movieReleaseDate)).toBeInTheDocument()

        expect(screen.getByLabelText(getAllWatchedMoviesListResponse[0].movieName)).toBeInTheDocument()
        expect(screen.getByLabelText(getAllWatchedMoviesListResponse[1].movieName)).toBeInTheDocument()

        expect(screen.queryAllByRole('button')).not.toBeNull() 
    })

    test('Renders Rated Movies List Section fully', async() => {

        fetch.mockResponseOnce(JSON.stringify(getAllWatchedMoviesListResponse))
            .mockResponseOnce(JSON.stringify(getAllRatedMoviesListResponse))

        render(
            <BrowserRouter>
                <Overview/>
            </BrowserRouter>
        )

        await waitForElementToBeRemoved(screen.getByText('Loading...'))

        expect(screen.getByText('Watched Movies List')).toBeInTheDocument()

        expect(screen.getByText(getAllRatedMoviesListResponse[0].movieName)).toBeInTheDocument()
        expect(screen.getByText(getAllRatedMoviesListResponse[1].movieName)).toBeInTheDocument()

        expect(screen.getByText(getAllRatedMoviesListResponse[0].movieOverview)).toBeInTheDocument()
        expect(screen.getByText(getAllRatedMoviesListResponse[1].movieOverview)).toBeInTheDocument()

        expect(screen.getByText(getAllRatedMoviesListResponse[0].movieReleaseDate)).toBeInTheDocument()
        expect(screen.getByText(getAllRatedMoviesListResponse[1].movieReleaseDate)).toBeInTheDocument()

        expect(screen.getByLabelText(getAllRatedMoviesListResponse[0].movieName)).toBeInTheDocument()
        expect(screen.getByLabelText(getAllRatedMoviesListResponse[1].movieName)).toBeInTheDocument()

        expect(screen.queryAllByRole('radio')).not.toBeNull() 
    })
})