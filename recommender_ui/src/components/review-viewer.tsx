import React, { Component } from 'react';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { withStyles } from '@material-ui/core/styles';
import { Container, Box, Grid, Button } from '@material-ui/core';
import Chip from '@material-ui/core/Chip';
import TextField from '@material-ui/core/TextField';
import SearchIcon from '@material-ui/icons/Search';
import Paper from '@material-ui/core/Paper';
import 'typeface-roboto';
import LinearProgress from '@material-ui/core/LinearProgress';


const axios = require('axios');

interface ReviewViewerProps {
  updateReviewId(reviewerId:string): any
}
interface ReviewViewerState {
  review_items: ReviewItem[],
  reviewerId: string,
  loading: boolean,
}


interface ReviewItem {
  reviewerID: string,
  asin: string,
  reviewText: string,
  overall: number,
  summary: string,
  category: string[],
  title: string,
  image: string[],
  brand: string[],
  description: string[],
}


  
class ReviewViewer extends Component<ReviewViewerProps, ReviewViewerState> {
    constructor(props: ReviewViewerProps) {
        super(props);
        this.state = {
          review_items: [],
          reviewerId: "A35DQQH8W09HW",
          loading: false
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

  reviewIDTextFieldOnChange = (event: any) => {
    this.setState({reviewerId: event.target.value})
  };

  getReviewsButtonOnClick = () => {
    this.props.updateReviewId(this.state.reviewerId);
    this.getReviewData()
  }

  getReviewData = () => {
    this.setState({loading: true})
    let self = this;
    let reviewer_id = this.state.reviewerId
    axios.get('http://127.0.0.1:8080/reviews?reviewerID=' + reviewer_id)
    .then(function (response: any) {
      // handle success
      console.log(response)
      let review_data = response['data'] as ReviewItem[];
      self.setState({review_items: review_data})
    })
    .catch(function (error: any) {
      
    })
    .finally(function () {
      self.setState({loading: false})
    });
  }


  componentDidUpdate() {

  }
  componentDidMount() {
    this.getReviewData()
  }

  render() {

    return (
        <Box style={{marginTop: "20px", maxWidth: "700px", fontFamily: "Roboto", paddingBottom: "100px"}}>
            <StyledPaperHeading>
              <Typography variant="h5" style={{fontFamily: "Roboto", verticalAlign: "middle", lineHeight: "60px", color: "#3c3f45" }}>
                Selected users reviews
              </Typography>
          </StyledPaperHeading>
            {this.state.review_items.map((review: ReviewItem) => {     
            return <ExpansionPanel
                      style={{maxWidth: "700px", borderBottom: '1px solid lightgray'}}
                    >
                      <ExpansionPanelSummary
                          expandIcon={<ExpandMoreIcon />}
                          aria-controls="panel1a-content"
                          id="panel1a-header"
                          >
                            <Grid container xs={12} spacing={3}>
                              <Grid xs={4} >
                                <Box display="flex" justifyItems="flex-start">
                                  <Chip
                                    label={review.overall}
                                    color={review.overall < 3 ? 'secondary' : 'primary'}
                                    /> 
                                  <Chip
                                    label={review.asin}
                                    color={review.overall < 3 ? 'secondary' : 'primary'}
                                    /> 
                                </Box>
                              </Grid>
                              <Grid xs={8}>
                              <Box display="flex" justifyItems="center">
                                <StyledTypography>{review.title}</StyledTypography>
                              </Box>
                              </Grid>
                          </Grid>
                      </ExpansionPanelSummary>
                    <ExpansionPanelDetails style={{display: "block", minHeight: "250px", borderTop: '1px solid lightgray', backgroundColor: "#fafafa"}}>
                      <Box style={{borderBottom: '1px solid lightgray', paddingBottom: "15px"}}>
                      <Grid container spacing={3}>
                        { review.image ? (
                        <Grid item xs={4} style={{ borderRight: '1px solid lightgray', marginTop: '2px'}}>
                            <img style={{margin: "auto",height: "100%", maxHeight: "200px", overflow: "hidden", maxWidth: "150px"}} alt="videogame" src={review.image[0]} />
                        </Grid>
                        ) : (
                          <Grid item xs={4} style={{ borderRight: '1px solid lightgray', marginTop: '2px'}}>
                            <img style={{marginLeft: "auto", marginTop: "auto",width: "100%", height: "100%", maxHeight: "200px", overflow: "hidden"}} alt="videogame" src={"https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"} />
                          </Grid>
                        )
                        }
                        <Grid item xs={8}>
                          <Typography style={{height: "100%", width: "100%", textAlign: "center"}}>
                            {review.description && review.description[0].length <= 641 ? (
                                review.description[0]
                            ) :
                                (review.description[0].slice(0, 637) + "...")
                            }
                          </Typography>
                        </Grid>

                      </Grid>
                      </Box>
                      <Box style={{display: "block", paddingTop: "15px"}}>
                        {review.category.map((category: string) => {
                          if(category.length < 25 && category.length > 2) {
                            return <Chip
                              label={category}
                              style={{fontSize: "12px"}}
                              color={'secondary'}
                              /> 
                          }
                          })}
                        </Box>
                </ExpansionPanelDetails>
              </ExpansionPanel> })}
        {this.state.loading ? <LinearProgress /> : [] }
        <StyledPaper>
          <TextField
            id="reviewerID_field"
            label="Reviewer id"
            defaultValue="A35DQQH8W09HW"
            helperText="Amazon reviewer id from data"
            variant="filled"
            onChange={this.reviewIDTextFieldOnChange}
            style={{marginTop: "15px"}}
          />
        <Button
          variant="contained"
          color="primary"
          size="medium"
          style={{marginTop: "25px", marginLeft: "15px"}}
          startIcon={<SearchIcon/>}
          onClick={this.getReviewsButtonOnClick}
        > 
        Search
      </Button>
      </StyledPaper>
      </Box>
    )
  }
}

const StyledTypography= withStyles({
  root: {
    fontSize: 17,
    fontWeight: "inherit",
  },
  label: {

  },
})(Container);

const StyledPaper = withStyles({
  root: {
    backgroundColor: '#f7f5f5',
    boxShadow: '0 3px 5px 2px #dbd7d7',
    margin: "auto",
    height: "100px",
    color: "#3c3f45"
  },
  label: {
    textTransform: 'capitalize',
  },
})(Paper);
const StyledPaperHeading = withStyles({
  root: {
    backgroundColor: '#f7f5f5',
    boxShadow: '0 3px 5px 2px #dbd7d7',
    color: "#3c3f45",
    margin: "auto",
    height: "60px"
  },
  label: {
    textTransform: 'capitalize',
  },
})(Paper);

export default ReviewViewer;