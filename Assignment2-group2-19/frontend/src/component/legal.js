//Scott LEE 103994562
import * as React from 'react';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box'; 

const CustomPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  textAlign: 'center',
  color: theme.palette.text.primary,
  backgroundColor: '#DCF0FD',
  borderRadius: '16px',
  boxShadow: theme.shadows[6],
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  minHeight: '100vh',
}));

const doubleFontSize = {
  fontSize: '1.5em', 
};

const BoxStyle = {
  border: '2px solid #000', 
  padding: '16px', 
  marginBottom: '16px',
  borderRadius: '10px',
  backgroundColor: 'white', 
};


const Legal = () => {
  return (
    <CustomPaper elevation={3}>
      <h1><span style={{fontSize: '50px'}}>Legal Information</span></h1>

      <div style={doubleFontSize}>
      <Box sx={BoxStyle}><h2>Terms and Conditions</h2>
        <p>These are the terms and conditions...</p></Box>
      </div>

      <div style={doubleFontSize}>
      <Box sx={BoxStyle}>
        <h2>Privacy Policy</h2>
        <p>This is the privacy policy...</p></Box>
      </div>

      <div style={doubleFontSize}>
      <Box sx={BoxStyle}>
        <h2>Disclaimer</h2>
        <p>This is the disclaimer...</p></Box>
      </div>

      <div style={doubleFontSize}>
      <Box sx={BoxStyle}>
        <h2>Cookie Policy</h2>
        <p>This is the cookie policy...</p></Box>
      </div>

      <div style={doubleFontSize}>
      <Box sx={BoxStyle}>
        <h2>Security</h2>
        <p>This is the security information...</p></Box>
      </div>
    </CustomPaper>
  );
};

export default Legal;