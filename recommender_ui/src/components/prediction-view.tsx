import React, { Component } from 'react';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import { Container, Box, Grid, Button } from '@material-ui/core';
import TextFormatOutlinedIcon from '@material-ui/icons/TextFormatOutlined';
import Paper from '@material-ui/core/Paper';
import 'typeface-roboto';
import LinearProgress from '@material-ui/core/LinearProgress';
import TextField from '@material-ui/core/TextField';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

const axios = require('axios');

interface ReviewViewerProps {
}
interface ReviewViewerState {
  loading: boolean,
  predictions: number[],
  reviews: string[],
  textFieldValue: string,
}
  
class PredictionViewer extends Component<ReviewViewerProps, ReviewViewerState> {
    constructor(props: ReviewViewerProps) {
        super(props);
        this.state = {
          predictions: [],
          reviews: [],
          loading: false,
          textFieldValue: "Amazon claim to be the most customer centric company. I guess that was the ethos in the early days but now Bezos has managed to dominate the market they can treat their customers like trash. They have gone seriously downhill and their contact centre is a joke. Poorly trained staff who can only read from a script. I will not be dealing with them again."
        };
    }

  predictionTextFieldOnChange = (event: any) => {
    this.setState({textFieldValue: event.target.value})
  }; 
  predictButtonOnClick = () => {
    this.setState({loading: true});
    let review_list = this.state.textFieldValue.split(":::");
    this.setState({reviews: review_list});
    this.getPredictionResults(review_list);;
  }

  getPredictionResults = (review_list: string[]) => {
    this.setState({loading: true})
    let self = this;
    console.log(review_list)
    axios.post('http://127.0.0.1:8080/predict/', {
        reviews: review_list
    })
    .then(function (response: any) {
      let predictions = response['data']['predictions'] as number[];
      self.setState({predictions: predictions})
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
  }

  render() {

    return (
        <Box style={{marginTop: "20px", fontFamily: "Roboto", paddingBottom: "100px"}}>
        <Grid container spacing={3} style={{width: "100%"}}>
            <Grid item xs={6}>
                    <StyledPaperHeading>
                        <Typography variant="h5" style={{fontFamily: "Roboto", verticalAlign: "middle", lineHeight: "60px", color: "#3c3f45" }}>
                            Predict positivity of written review
                        </Typography>
                    </StyledPaperHeading>
                    {this.state.loading ? <LinearProgress /> : [] }
                    <StyledPaper>
                    <TextField
                        id="review viewer"
                        label="comma-separated reviews"
                        multiline
                        rows="20"
                        defaultValue={this.state.textFieldValue}
                        style={{width: "500px", borderTop: '1px solid lightgray', borderLeft: '1px solid lightgray', borderRight: '1px solid lightgray', borderBottom: '1px solid lightgray', boxShadow: ""}}
                        onChange={this.predictionTextFieldOnChange}
                    />
                    <br/>
                    <Button
                    variant="contained"
                    color="primary"
                    size="medium"
                    style={{marginTop: "15px", marginLeft: "15px"}}
                    startIcon={<TextFormatOutlinedIcon/>}
                    onClick={this.predictButtonOnClick}
                    > 
                    Predict
                    </Button>
                </StyledPaper>
            </Grid>
            <Grid item xs={6}>
                <TableContainer component={Paper}>
                    <Table style={{minWidth: "350px"}} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell>Review text</TableCell>
                            <TableCell align="right">Review length</TableCell>
                            <TableCell align="right">Review score</TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                        {this.state.predictions.map((score: number, index: number) => {
                            return <TableRow key={index}>
                            <TableCell component="th" scope="row">
                                {this.state.reviews[index]}
                            </TableCell>
                            <TableCell align="right">{this.state.reviews[index].length}</TableCell>
                            <TableCell align="right">{score === 0 ? "Negative" : "Positive"}</TableCell>
                            </TableRow>
                        })
                        }
                        </TableBody>
                    </Table>
                </TableContainer>
            </Grid>
        </Grid>
      </Box>
    )
  }
}

const StyledPaper = withStyles({
  root: {
    backgroundColor: "FDFDFD", 
    boxShadow: '0 3px 5px 2px #dbd7d7',
    margin: "auto",
    color: "#3c3f45",
    paddingTop: "30px"
  },
  label: {
    textTransform: 'capitalize',
  },
})(Paper);
const StyledPaperHeading = withStyles({
  root: {
    backgroundColor: "transparent",
    boxShadow: '0 3px 5px 2px #dbd7d7',
    color: "#3c3f45",
    margin: "auto",
    height: "60px"
  },
  label: {
    textTransform: 'capitalize',
  },
})(Paper);

export default PredictionViewer;