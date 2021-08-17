import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import './App.css';
import FindResources from './components/FindResources';

function App() {
  return (
    <BrowserRouter>
      <Switch>
      <Route exact path='/' component={FindResources} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;