//Shreeya Shrestha - 103831863
import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button'; 
import MenuItem from '@mui/material/MenuItem';
import {Link} from 'react-router-dom';

//array of navigation pages to link to them later
const pages = ['Home', 'Reports', 'About Us'];

function ResponsiveAppBar() {
    const [anchorElNav, setAnchorElNav] = React.useState(null);

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };

    return (
        //top app bar set up
        <AppBar position="static" sx={{ backgroundColor: '3498DB'}}>
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                {/* Add the logo and configure size   */}
                <img
                    src="bcimg.jpg"
                    alt="Logo"
                    style={{ display: { xs: 'none', md: 'flex'}, mr: 1, maxWidth: '100%', height: '40px'}} 
                />
                    {/* main link to the homepage by clicking the name on the navbar */}
                    <Typography
                        variant="h6"
                        noWrap
                        component="a"
                        href="/"
                        sx={{
                            mr: 2,
                            display: { xs: 'none', md: 'flex' },
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.3rem',
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                           |Veridity
                    </Typography>

                    <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
                        <IconButton
                            size="large"
                            aria-label="account of current user"
                            aria-controls="menu-appbar"
                            aria-haspopup="true"
                            onClick={handleOpenNavMenu}
                            color="inherit"
                        >
                            <MenuIcon />
                        </IconButton>

                        {/* drop down menu to adjust to small screen */}
                        <Menu
                            id="menu-appbar"
                            anchorEl={anchorElNav}
                            anchorOrigin={{
                                vertical: 'bottom',
                                horizontal: 'left',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'left',
                            }}
                            open={Boolean(anchorElNav)}
                            onClose={handleCloseNavMenu}
                            sx={{
                                display: { xs: 'block', md: 'none' },
                            }}
                        >
                            {pages.map((page) => (
                                //link pages to respective clicks
                                <MenuItem key={page} onClick={handleCloseNavMenu}
                                component={Link} 
                                to={page === 'Home' ? '/' : `/${page}`}
                                >
                                    <Typography textAlign="center">{page}</Typography>
                                </MenuItem>
                            ))}

                            
                        </Menu>
                    </Box>
                    <Typography
                        variant="h5"
                        noWrap
                        component="a"
                        href="/"
                        sx={{
                            mr: 2,
                            display: { xs: 'flex', md: 'none' },
                            flexGrow: 1,
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.3rem',
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        Veridity
                    </Typography>
                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } , justifyContent: 'flex-end' }}>
                    {pages.map((page) => (
                        //create buttons for pages in big screen
                        <Button
                            key={page}
                            //link buttons to their pages
                            component={Link}
                            to={page === 'Home' ? '/' : `/${page}`}
                            sx={{
                                my: 1,
                                color: 'white',
                                display: 'block',
                                borderRadius: '8px',
                                padding: '4px 8px',
                                backgroundColor: 'rgba(0, 0, 0, 0.2)',
                                marginRight: '8px',
                            }}
                        >
                            {page}
                        </Button>
                    ))
                    }
                    </Box>
                </Toolbar>
            </Container>
        </AppBar>
    );
}
export default ResponsiveAppBar;