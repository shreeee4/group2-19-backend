import React from 'react';
//import './App.css';
//import BodyPlaceholder from './body/body';
import FooterFinal from './component/footer';
import TeamMembers from './component/aboutus';
//import Information from './components/information';
//import LegalInfo from './legal/legal'
function AboutUs() {
  return (
    <div className="AboutUs">
      <TeamMembers/>
      <FooterFinal/>
    </div>
  );
}

export default AboutUs;