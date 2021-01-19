import { ExpansionPanelActions } from '@material-ui/core';
import { render, screen } from '@testing-library/react';

import Loading from '../components/loading'

describe('Loading component', () => {
    test('Renders Loading Text', () => {
        render(<Loading/>)

        expect(screen.getByText('Loading...')).toBeInTheDocument()
    })

    test('Renders Progress Bar', () => {
        render(<Loading/>)

        expect(screen.getByRole('progressbar')).toBeInTheDocument()
    })
})