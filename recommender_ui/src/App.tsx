import React from 'react';
import Paper from '@material-ui/core/Paper';
import './App.css';
import { withStyles } from '@material-ui/core/styles';
import ReviewViewer from './components/review-viewer';

const App: React.FC = () => {
  return (
    <div className="App">
        <StyledPaper>
        <ReviewViewer/>
        </StyledPaper>
    </div>
  );
}

const StyledPaper = withStyles({
  root: {
    background: 'linear-gradient(45deg, #f8faf2 30%, #fefffc 90%)',
    borderRadius: 3,
    height: "96%",
    width: "94%",
    border: 0,
    color: 'black',
    boxShadow: '0 3px 5px 2px #dbd7d7',
    margin: "auto",
  },
  label: {
    textTransform: 'capitalize',
  },
})(Paper);
export default App;
