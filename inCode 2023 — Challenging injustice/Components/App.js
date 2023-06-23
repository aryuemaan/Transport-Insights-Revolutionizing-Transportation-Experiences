import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/Home';
import Feedback from './components/Feedback';
import Analytics from './components/Analytics';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/feedback" component={Feedback} />
        <Route path="/analytics" component={Analytics} />
      </Switch>
    </Router>
  );
};

export default App;
