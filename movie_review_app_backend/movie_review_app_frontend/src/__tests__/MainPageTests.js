import {render, screen, waitForElementToBeRemoved} from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Main from '../containers/main'

import { enableFetchMocks } from 'jest-fetch-mock'

enableFetchMocks()

describe('Main Page', () => {

    beforeEach(() => {
        fetch.resetMocks()
    })

    const moviesInCurPageResponse = {
        "page": 1,
        "total_pages": 500,
        "total_results": 10000,
        "results": [
            {
                "id": 716703,
                "title": "Alpha Beta",
                "overview": "Lorem Ipsum Dolor Sit Amet",
                "release_date": "2020-12-17",
                "poster": "https://image.tmdb.org/t/p/w500/zjGrlEuENSjRZGWc8N10zq3Jjkq1.jpg"
            },
            {
                "id": 716704,
                "title": "Gamma Theta",
                "overview": "Lorem Ipsum Dolor Sit Amet Dos",
                "release_date": "2021-12-17",
                "poster": "https://image.tmdb.org/t/p/w500/zjGrlEuENSjRZGWc8N10zq3Jjkq2.jpg"
            },
        ]
    }

    const checkPageInWatchedListResponse = {
        '716703': true,
        '716704': false
    }

    const getCurrentPageMovieRatingsResponse = {
        '716703': 4,
        '716704': 5
    }

    test('Renders Navbar component', async() => {

        fetch.mockResponseOnce(JSON.stringify(moviesInCurPageResponse))
            .mockResponseOnce(JSON.stringify(checkPageInWatchedListResponse))
            .mockResponseOnce(JSON.stringify(getCurrentPageMovieRatingsResponse))

        render(
            <BrowserRouter>
                <Main/>
            </BrowserRouter>
        )

        await waitForElementToBeRemoved(screen.getByText('Loading...'))

        expect(screen.getByRole('banner')).toBeInTheDocument()
        expect(screen.getByText('Movie Review App')).toBeInTheDocument()
        expect(screen.getByText('Overview')).toBeInTheDocument()
    })

    test('Renders Movie Cards fully', async() => {

        fetch.mockResponseOnce(JSON.stringify(moviesInCurPageResponse))
            .mockResponseOnce(JSON.stringify(checkPageInWatchedListResponse))
            .mockResponseOnce(JSON.stringify(getCurrentPageMovieRatingsResponse))

        render(
            <BrowserRouter>
                <Main/>
            </BrowserRouter>
        )

        await waitForElementToBeRemoved(screen.getByText('Loading...'))

        expect(screen.getByText(moviesInCurPageResponse.results[0].title)).toBeInTheDocument()
        expect(screen.getByText(moviesInCurPageResponse.results[1].title)).toBeInTheDocument()

        expect(screen.getByText(moviesInCurPageResponse.results[0].overview)).toBeInTheDocument()
        expect(screen.getByText(moviesInCurPageResponse.results[1].overview)).toBeInTheDocument()

        expect(screen.getByText(moviesInCurPageResponse.results[0].release_date)).toBeInTheDocument()
        expect(screen.getByText(moviesInCurPageResponse.results[1].release_date)).toBeInTheDocument()

        expect(screen.getByLabelText(moviesInCurPageResponse.results[0].title)).toBeInTheDocument()
        expect(screen.getByLabelText(moviesInCurPageResponse.results[1].title)).toBeInTheDocument()

        expect(screen.queryAllByRole('radio')).not.toBeNull() 
    })

    test('Renders Pagniation component', async() => {

        fetch.mockResponseOnce(JSON.stringify(moviesInCurPageResponse))
            .mockResponseOnce(JSON.stringify(checkPageInWatchedListResponse))
            .mockResponseOnce(JSON.stringify(getCurrentPageMovieRatingsResponse))

        render(
            <BrowserRouter>
                <Main/>
            </BrowserRouter>
        )

        await waitForElementToBeRemoved(screen.getByText('Loading...'))

        expect(screen.getByRole('navigation')).toBeInTheDocument()
    })
})