import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';

import Navbar from '../components/navbar';

describe('Navbar Component', () => {
    test('Renders Title', () => {
        render(
            <BrowserRouter>
                <Navbar/>
            </BrowserRouter>
        )

        expect(screen.getByText('Movie Review App')).toBeInTheDocument()
    })

    test('Title redirects to main page', () => {
        render(
            <BrowserRouter>
                <Navbar/>
            </BrowserRouter>
        )

        expect(screen.getByText('Movie Review App').closest('a').href).toBe('http://localhost/')
    })

    test('Renders Overview', () => {
        render(
            <BrowserRouter>
                <Navbar/>
            </BrowserRouter>
        )
        
        expect(screen.getByText('Overview')).toBeInTheDocument()
    })

    test('Overview redirects to /overview', () => {
        render(
            <BrowserRouter>
                <Navbar/>
            </BrowserRouter>
        )

        expect(screen.getByText('Overview').closest('a').href).toBe('http://localhost/overview')
    })
})