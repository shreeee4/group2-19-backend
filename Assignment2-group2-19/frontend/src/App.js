// Shreeya Shrestha - 103831863
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './component/header';
import Home from './home.js';
import Reports from './Reports.js';
import AboutUs from './AboutUs.js';
import FAQ from './FAQ.js';
import Legal from './Legal.js';

function App() {
    return (
            <div>
              {/* insert header */}
              <Header />
              {/* determine route to each page  */}
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/Reports" element={<Reports />} />
                <Route path="/About Us" element={<AboutUs />}/>
                <Route path="/FAQ" element={<FAQ />}/>
                <Route path="/Legal" element={<Legal />}/>

              </Routes>
            </div>
          

    );
  }

export default App;