//Shreeya Shrestha - 103831863
import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import SearchBar from './component/SearchBar.js';
import './index.css';
import Typography from '@mui/material/Typography';
import UploadFile from './component/UploadFile.js';
import Footer from './component/footer.js';

//styled components Item
const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
}));

export default function Home() {
    return (
        <Box spacing={2} sx={{ flexGrow: 1}}>
                <Box className= "bg-image" sx={{ flexGrow: 1}}>
                    {/* display a title of the page  */}
                    <Grid container spacing={5} justifyContent="center" alignItems="center" padding={5}></Grid>
                    <Grid item xs={12} sm={12} md={12}>
                            <Typography variant="h1" sx={{ color: 'white', textAlign: 'center', fontWeight: '800', textShadow: '4px 2px 4px rgba(0, 0, 0, 0.9)'}}>
                                    VERIFY YOUR SMART CONTRACTS WITH US
                            </Typography>
                    </Grid>
                            {/* grid layout for other component  */}
                            <Grid container spacing={5} justifyContent="center" alignItems="center" padding={5}>
                            {/* searchbar grid component  */}
                            <Grid item xs={12} sm={12} md={8}>
                                    <Item>
                                        <SearchBar />
                                    </Item>
                                </Grid>
                            {/* upload button grid component  */}
                            <Grid item xs={12} sm={12} md={8}>
                                    <Item>
                                        <UploadFile />
                                    </Item>
                                </Grid>             
                            </Grid>
                            
                </Box>
                
      {/* Sample Text */}
      
      <Grid container spacing={5}  padding={3} alignItems="center" style={{ backgroundColor: '#DCF0FD' }}>
      <Grid item xs={12}>
        <Typography variant="h4" sx={{ color: '#525264', fontWeight: '200'}}>What are Smart Contracts?</Typography>
      </Grid>
      <Grid item xs={12} md={6}>
        <Typography variant="body1">
        A smart contract operates as an independent program, automating tasks outlined in a contract or agreement. After execution, these transactions are both traceable and irreversible.
        <br></br><br></br>
        These smart contracts enable secure transactions and agreements among different, anonymous parties, removing the necessity for a central authority, legal structure, or external enforcement mechanism.
        <br></br><br></br>
        Smart contracts function by adhering to straightforward "if/when...then..." statements, scripted into blockchain code. A network of computers initiates actions when predetermined conditions are met and verified. 
        These actions can involve disbursing funds, recording vehicle data, sending alerts, or generating tickets.
        Once executed, the blockchain registers the transaction as immutable, visible only to authorized parties.
        <br></br><br></br>
        In 1994, Nick Szabo, an American computer scientist known for creating the virtual currency "Bit Gold" in 1998, introduced the concept of smart contracts. This groundbreaking idea predates the emergence of Bitcoin by a decade.
        </Typography>
      </Grid>

      {/* Image */}
      <Grid item xs={12} md={6}>
        <img
          src="SmartContract.png"
          alt="SmartContract"
          style={{ maxWidth: '100%', height: 'auto',  border: '2px solid #3498DB',  boxShadow: '8px 10px 10px rgba(0, 0, 0, 0.2)' }}
        />
        <Typography variant="caption">What are Smart Contracts?</Typography>
      </Grid>      
      </Grid>
                {/* Footer grid component  */}
                <Grid item xs={12} sm={12} md={12}>
                    <Item> 
                        <Footer />
                    </Item>
                </Grid>
            
        </Box>
    )}