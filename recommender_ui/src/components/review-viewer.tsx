import React, { Component } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { withStyles } from '@material-ui/core/styles';
import { Container } from '@material-ui/core';
import { useTheme } from '@material-ui/core/styles';

interface ReviewViewerProps {

}
interface ReviewViewerState {

}

  
class ReviewViewer extends Component<ReviewViewerProps, ReviewViewerState> {
    constructor(props: ReviewViewerProps) {
        super(props);
        this.state = {
        };
    }
  //basicBusMarkerOnClick = () => {
   // this.props.setWayPoints((this.props.vehicleNumber.toString()), this.props.nextStops);
   // if (!this.state.infoIsVisible) {
    //  this.props.focusToBus({ lng: this.props.lng, lat: this.props.lat }, 16, this.props.vehicleNumber);
    //} else {
    //  this.props.clearFocusToBus();
    //}
    //this.setState({ infoIsVisible: !this.state.infoIsVisible, isTracking: this.props.isTracking })
  //}

  componentDidUpdate() {
  }

  render() {

    return (
        <StyledDiv>
        <ExpansionPanel>
          <ExpansionPanelSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
            id="panel1a-header"
          >
            <StyledTypography>Expansion Panel 1</StyledTypography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
              sit amet blandit leo lobortis eget.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <ExpansionPanel>
          <ExpansionPanelSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel2a-content"
            id="panel2a-header"
          >
            <StyledTypography>Expansion Panel 2</StyledTypography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
              sit amet blandit leo lobortis eget.
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <ExpansionPanel disabled>
          <ExpansionPanelSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel3a-content"
            id="panel3a-header"
          >
            <StyledTypography>Disabled Expansion Panel</StyledTypography>
          </ExpansionPanelSummary>
        </ExpansionPanel>
      </StyledDiv>
    )
  }
}
const theme = useTheme()
const StyledDiv= withStyles({
  root: {
    width: '100%',
  },
  label: {

  },
})(Container);

const StyledTypography= withStyles({
  root: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
  label: {

  },
})(Container);

export default ReviewViewer;