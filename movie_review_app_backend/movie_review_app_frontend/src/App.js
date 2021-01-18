import './App.css';

import React from "react"

import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Overview from "./containers/overview"
import Main from "./containers/main"

function App() {
  return(
    <Router>
      <Switch>
        <Route exact path="/overview" exact component={Overview}></Route>
        <Route exact path="/" component={Main}/>
      </Switch>
    </Router>
  )
}

export default App;
