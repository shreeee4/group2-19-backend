//Scott Lee 103994562
import * as React from 'react';
import { useState } from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button'
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';


// Define a styled component for the outer paper
const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  backgroundColor: '#DCF0FD',
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

// Define a styled component for the team title
const TeamTitle = styled(Item)(({ theme }) => ({
    fontSize: '48px',
    fontWeight: 'bold', 
  }));



export default function TeamMembers() {
  // Create an array of showDetails states, one for each team member
  const [showDetails, setShowDetails] = useState([false, false, false]);

  const toggleDetails = (index) => {
    // Create a copy of the showDetails array and toggle the state for the specified index
    const newShowDetails = [...showDetails];
    newShowDetails[index] = !newShowDetails[index];
    setShowDetails(newShowDetails);
  };
// Function to open the default email client with a specified email address
  const sendEmail = (emailAddress) => {
    window.location.href = `mailto:${emailAddress}`;
  };

  return (
    <Box sx={{ flexGrow: 1, marginBottom: '50px', marginLeft: '20px', marginRight: '20px', marginTop: '10px'}}>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={12} md={12}>
          <TeamTitle>The Veridity Team</TeamTitle>
        </Grid>

        {/* Team Member 1 */}
        <Grid item xs={12} sm={6} md={4}>
          <Item>
          <ImageList variant="masonry" cols={4} gap={0}> 
            <img
              src="https://cdn-icons-png.flaticon.com/256/1077/1077114.png"
              alt="User Icon"
              width="100"
              height="100"
            />
             
             <ImageListItem sx={{width: 75, height: 75}}>
            <img
              src="https://www.iconpacks.net/icons/2/free-send-mail-icon-2574-thumb.png"
              alt="Send Email"
              onClick={() => sendEmail('102570136@student.swin.edu.au')}
              style={{ cursor: 'pointer' }}
              title="Send an Email"
            />
            </ImageListItem>
            <ImageListItem sx={{marginLeft: '-0px', width: 60, height: 60}}>
            <img
            src="https://cdn-icons-png.flaticon.com/512/174/174857.png"
            alt="LinkedIn"
            onClick={() => window.open('https://www.linkedin.com/in/scott-lee-0a15a028b', '_blank')}
            style={{ cursor: 'pointer' }}
            title="LinkedIn"
            />
            </ImageListItem>
            <ImageListItem sx={{marginLeft: '-10px', width: 70, height: 70}}>

            <img
            src="https://cyclr.com/wp-content/uploads/2022/03/ext-627.png"
            alt="Twitter"
            onClick={() => window.open('https://twitter.com/Panglosic', '_blank')}
            style={{ cursor: 'pointer' }}
            title="Twitter"
            />


            </ImageListItem>
            </ImageList>
            <h2>Simon Holt</h2>
            <Button variant="text" onClick={() => toggleDetails(0)}
            >
              {showDetails[0] ? 'Hide Details' : 'About Simon Holt'}
            </Button>
            {showDetails[0] && (
              <div>
                <p>
                  Hello! I'm Simon Holt, a passionate student with a diverse range of interests looking to get into the cybersecurity workforce.
                  {/* Rest of the detailed text here */}
                  <br></br><br></br>
                  <b>Email: 102570136@student.swin.edu.au</b>
                </p>
              </div>
            )}
          </Item>
        </Grid>

        {/* Team Member 2 */}
        <Grid item xs={12} sm={6} md={4}>
          <Item>
          <ImageList variant="masonry" cols={4} gap={0}> 
            <img
              src="https://cdn-icons-png.flaticon.com/256/1077/1077114.png"
              alt="User Icon"
              width="100"
              height="100"
            />
             
             <ImageListItem sx={{width: 75, height: 75}}>
            <img
              src="https://www.iconpacks.net/icons/2/free-send-mail-icon-2574-thumb.png"
              alt="Send Email"
              onClick={() => sendEmail('103831863@student.swin.edu.au')}
              style={{ cursor: 'pointer' }}
              title="Send an Email"
            />
            </ImageListItem>
            <ImageListItem sx={{marginLeft: '-0px', width: 60, height: 60}}>
            <img
            src="https://cdn-icons-png.flaticon.com/512/174/174857.png"
            alt="LinkedIn"
            onClick={() => window.open('https://www.linkedin.com/in/shreeyastha04', '_blank')}
            style={{ cursor: 'pointer' }}
            title="LinkedIn"
            />
            </ImageListItem>
            <ImageListItem sx={{marginLeft: '-10px', width: 70, height: 70}}>

            <img
            src="https://cyclr.com/wp-content/uploads/2022/03/ext-627.png"
            alt="Twitter"
            onClick={() => window.open('https://twitter.com/shre_wd', '_blank')}
            style={{ cursor: 'pointer' }}
            title="Twitter"
            />


            </ImageListItem>
            </ImageList>
            <h2>Shreeya Shrestha</h2>
            <Button variant="text" onClick={() => toggleDetails(1)}
            >
              {showDetails[1] ? 'Hide Details' : 'About Shreeya Shrestha'}
            </Button>
            {showDetails[1] && (
              <div>
                <p>
                Hello! I'm Shreeya Shrestha, a student in my second year of University.
                  Besides my interest in keeping digital information safe, I also really enjoy reading books.

                  {/* Rest of the detailed text here */}
                  <br></br>
                  <br></br>
                  When I'm not learning about online security, you'll often find me lost in a good book. I find that my love for understanding computer security is a bit like my love for exploring exciting stories in books.
                  <br></br>
                  <br></br>
                  <b>Email: 103831863@student.swin.edu.au</b>
                </p>
              </div>
            )}
          </Item>
        </Grid>

        {/* Team Member 3 */}
        <Grid item xs={12} sm={6} md={4}>
          <Item>
          <ImageList variant="masonry" cols={4} gap={0}> 
            <img
              src="https://cdn-icons-png.flaticon.com/256/1077/1077114.png"
              alt="User Icon"
              width="100"
              height="100"
            />
             
             <ImageListItem sx={{width: 75, height: 75}}>
            <img
              src="https://www.iconpacks.net/icons/2/free-send-mail-icon-2574-thumb.png"
              alt="Send Email"
              onClick={() => sendEmail('103994562@student.swin.edu.au')}
              style={{ cursor: 'pointer' }}
              title="Send an Email"
            />
            </ImageListItem>
            <ImageListItem sx={{marginLeft: '-0px', width: 60, height: 60}}>
            <img
            src="https://cdn-icons-png.flaticon.com/512/174/174857.png"
            alt="LinkedIn"
            onClick={() => window.open('https://www.linkedin.com/in/scott-lee-0a15a028b', '_blank')}
            style={{ cursor: 'pointer' }}
            title="LinkedIn"
            />
            </ImageListItem>
            <ImageListItem sx={{marginLeft: '-10px', width: 70, height: 70}}>

            <img
            src="https://cyclr.com/wp-content/uploads/2022/03/ext-627.png"
            alt="Twitter"
            onClick={() => window.open('https://twitter.com/Panglosic', '_blank')}
            style={{ cursor: 'pointer' }}
            title="Twitter"
            />


            </ImageListItem>
            </ImageList>
            <h2>Scott Lee</h2>
            <Button variant = "text" onClick={() => toggleDetails(2)}
            >
              {showDetails[2] ? 'Hide Details' : 'About Scott Lee'}
            </Button>
            {showDetails[2] && (
              <div>
                <p>
                  Hello! I'm Scott Lee, a passionate student with a diverse range of interests looking to get into the cybersecurity workforce.
                  <br></br><br></br>
                  On the court, you'll often find me dribbling and shooting hoops as basketball is not just a sport for me, but a way of life. Off the court, I'm a fitness enthusiast who enjoys hitting the gym to stay physically fit and mentally sharp.

When I'm not working up a sweat, I'm immersed in the world of music. Whether it's playing a musical instrument or curating playlists, music is my constant companion, providing inspiration and relaxation.
<br></br><br></br>
My fascination with technology led me down the path of cybersecurity and computer science. I thrive on the challenges of securing digital landscapes and exploring the limitless possibilities of computer science. It's an ever-evolving field that keeps me engaged and eager to learn more.
<br></br><br></br>
In a nutshell, I'm a well-rounded individual with a love for sports, fitness, creativity through music, and a strong commitment to the ever-evolving realms of cybersecurity and computer science.
<br></br><br></br>
<b>Email: 103994562@student.swin.edu.au</b>
<br></br>
<b>YEAR0001</b>
                </p>
              </div>
            )}
          </Item>
        </Grid>
      </Grid>
      <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
    </Box>
    
  );
}