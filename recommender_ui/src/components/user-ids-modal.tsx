import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import { Fab } from '@material-ui/core';
import LaunchSharpIcon from '@material-ui/icons/LaunchSharp';
function rand() {
  return Math.round(Math.random() * 20) - 10;
}

function getModalStyle() {
  const top = 50 + rand();
  const left = 50 + rand();

  return {
    top: `${top}%`,
    left: `${left}%`,
    transform: `translate(-${top}%, -${left}%)`,
  };
}

const useStyles = makeStyles(theme => ({
  paper: {
    position: 'absolute',
    width: 400,
    backgroundColor: theme.palette.background.paper,
    border: '2px solid #000',
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));

export default function UserIdModal() {
  const classes = useStyles();
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);
  const [open, setOpen] = React.useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Fab size="small" aria-label="add" onClick={handleOpen}>
        <LaunchSharpIcon />
      </Fab>
      <Modal
        aria-labelledby="simple-modal-title"
        aria-describedby="simple-modal-description"
        onClose={handleClose}
        open={open}
      >
        <div style={modalStyle} className={classes.paper}>
          <h2 id="simple-modal-title">ReviewerID:s</h2>
          <p id="simple-modal-description">
          A2AAO8ECJZJGBR  A37T0C2H6PB2K4  AM39FGA2VCIDA  A27A2OSB01YOBB  A27KJVLKRIPJHJ A1N0WDO1C81HAR  
          A2AOEN40IYMAXP A247P51OUO683W A2H8UCVKM5YFF8 A11GKJRT1DYD9Q A3KYOJLZSQ4X8O
          A2M65WRANHYCO7  A3UCJD17GS387I A1C5NG2AZ8LB4P  A2IVC9YDV10VKQ  A1Q27GB6HL0ZZN  A2TI5NH88XAX3V
          AC37RZA1ZX04W A27RFBMPCWGZSZ A11S9LBCLTOE7S  A35Y53UVU3095N  A33B5M5CE7ZX7C  A6ORJ504BQZ9R  AK5UVZZARQWL0  
          A23KDYA7YGPEWW  A3NLIRZB0K479C  A1QFVYXAASFZHA  ACK92GHVVETOB  A3MNGI81TEAJFQ  A17A9U1O7R55XA  ALQPUQXMC1TT  A103JSUL9TCTGV  
          A2UXT6ADHPPJ81  AMHS35L463U87   A11440YU3U1WXZ  AYKEN16NIUW9M  A31HUJI3KGSPR4  A30OFYAGEFMA1L  A3RIIMSG5HB0J8  A1KDGSZEJXSE9S
          AZZ1KF8RAO1BR  A3VDRHSYXZ06YX  AFBZN55SV4GZQ  AEZK0ORBUJRSI  A29Z8XYDD5UZF8  AE3PQYXY49FJB  A1XHRU4HUHVE5Y  A2GNDQS5VHNID8  
          A2429XNXJU585Q  ANF6VHCR0JT1E   AWT53A209LVQ0   A1UPPS3SCS1J7O   AGUQ1KM7F9JDD   A3PQB10P4O38TS', 'A2W8WA99B1D7LX', 'A1EQ0W58BZO9A0 
          A1HJ2ADX8TH5F6   A2PK5OYQ3F5J8U   A1AC0P3B8C5NND   A1DMJHAM09Z8GU   A1PX8HKIMRGCVE   ALZW8UVZ0D5K0', 'A19WF87V967LPZ', 'A3O5K12S4996HM', 'A23HBDRWFTD5Y2', 'AL6KFPOR2WNXH', 'A16Z41LQ0PEQFY', 'A1QY2STLNNTC5Y', 'A3F2MQJY23H3DP', 'APBMY19Z31940', 'A1NBRF4297UMJ9']
          </p>

        </div>
      </Modal>
    </div>
  );
}