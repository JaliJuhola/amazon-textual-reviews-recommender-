import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import './App.css';
import { withStyles } from '@material-ui/core/styles';
import ReviewViewer from './components/review-viewer';
import ReccomendationViewer from './components/reccomendation-viewer';
import { Box, Grid, AppBar, Badge, Fab } from '@material-ui/core';
import UserIdModal from './components/user-ids-modal';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import LocationSearchingIcon from '@material-ui/icons/LocationSearching';
import TrackChangesIcon from '@material-ui/icons/TrackChanges';
import PredictionViewer from './components/prediction-view'

interface AppState {
  reviewerId: string,
  currentView: number,

}
class App extends Component<{}, AppState> {
  constructor(props: any) {
    super(props);
    this.state = {
      reviewerId: "A35DQQH8W09HW",
      currentView: 0
    };
  }

  update_reviewer_id = (reviewerId: string) => {
    this.setState({
      reviewerId: reviewerId
    })
  }
  change_to_predicting_view = () => {
    this.setState({currentView: 1})
  }
  change_to_recommending_view = () => {
    this.setState({currentView: 0})
  }
  render(){
    let view: any = []
    if(this.state.currentView === 0) {
      view = (<Grid container spacing={3}>
      <Grid item xs={6}>
        <ReviewViewer updateReviewId={this.update_reviewer_id} />
      </Grid>
      <Grid item xs={6}>
        <ReccomendationViewer reviewerId={this.state.reviewerId}/>
      </Grid>
    </Grid>)
    } else if (this.state.currentView == 1) {
      view = (
        <Box style={{paddingTop: "50px"}}>
          <PredictionViewer/>
        </Box>
      )
    }
    return (
      <div className="App">
        <StyledPaper>
        
          <AppBar position="static"  style={{marginTop: "-50px", width: "calc(100% + 35px)", marginLeft: "-35px"}}>
          <Toolbar >
          <Typography style={{flexGrow: 1}}>
          </Typography>
          <UserIdModal/>
          <Fab size="small" aria-label="add" onClick={this.change_to_predicting_view} style={{marginLeft: "10px"}}>
            <LocationSearchingIcon />
          </Fab>

          <Fab size="small" aria-label="add" onClick={this.change_to_recommending_view} style={{marginLeft: "10px"}}>
            <TrackChangesIcon />
          </Fab>
          </Toolbar>
        </AppBar>
        {view}
      </StyledPaper>
      </div>
    );
  }
}

const StyledPaper = withStyles({
  root: {
    background: 'linear-gradient(45deg, #f8faf2 30%, #fefffc 90%)',
    borderRadius: 3,
    width: "94%",
    maxWidth: "1600px",
    border: 0,
    color: 'black',
    boxShadow: '0 3px 5px 2px #dbd7d7',
    margin: "auto",
    paddingTop: "50px",
    paddingLeft: "35px"
  },
  label: {
    textTransform: 'capitalize',
  },
})(Paper);
export default App;
