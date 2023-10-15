// Scott Lee (103994562)
import React from "react";
import { Link } from "react-router-dom";
import './footer.css';
//import fblogo from '../assets/facebook.webp'

// Defines the FooterFinal component to be used and imported into the main site
const FooterFinal = () => {
    return(
    <div className="footer">
        <div className="sl__footer section__padding"> 
            <div className="sl__footer-links">
                <div className="sl__footer-links_div"> 
                <h4>About Us</h4>
                {/*Lets users know why use our site, how we audit and potential costs.*/}
<a href="/FAQ"> <p>Why audit/validate</p>
</a>
<a href="/FAQ"> <p>How we audit/validate</p>
</a>
<a href="/FAQ">
<p>Cost</p>
</a>
</div>
<div className="sl__footer-links_div">
<h4>Resources</h4>
{/*Lets users learn all relevant information needed about Smart Contracts should they wish to*/}
<a href="https://www.ibm.com/topics/smart-contracts#:~:text=Smart%20contracts%20are%20simply%20programs,intermediary's%20involvement%20or%20time%20loss."target ="_blank">
<p>What are "Smart Contracts"?</p>
</a>
<a href="https://www.britannica.com/money/how-smart-contracts-work" target="_blank">
<p>How do "Smart Contracts" work?</p>
</a>
<a href="https://hedera.com/learning/smart-contracts/smart-contract-audit#:~:text=A%20smart%20contract%20audit%20involves,and%20reliability%20of%20blockchain%20applications."target ="_blank">
<p>Why are audits so important?</p>
</a>
            </div>
            <div className="sl__footer-links_div">
                <h4>Support</h4>
                <a href="/FAQ">
                    <p>Frequently Asked Questions (FAQ)</p>
                </a>
                <a href="mailto: 103994562@student.swin.edu.au;102570136@student.swin.edu.au;103831863@student.swin.edu.au">
                    <p>Submit a Support Ticket</p>
                </a>
                <a href="mailto: 103994562@student.swin.edu.au;102570136@student.swin.edu.au;103831863@student.swin.edu.au">
                    <p>Contact Us</p>
                </a>
            </div>
            
            <div className="sl__footer-links_div">
                <h4>Our Team</h4>
                <div className="socialmedias"> {/*Intended to use to add social media icons, not being used atm*/}
                <a href="mailto: 102570136@student.swin.edu.au">
                    <p>Simon Holt</p>
                    </a>
                    <a href="mailto: 103831863@student.swin.edu.au">
                    <p>Shreeya Shrestha</p>
                    </a>
                    <a href="mailto: 103994562@student.swin.edu.au">
                    <p>Scott Lee</p>
                    </a>
                    </div>
            </div>
        </div>

    <hr></hr> {/*Horizontal line separating the main links with the misc/legal stuff*/}

    <div className="sl__footer-below"> {/*Container for the footer below section*/}
        <div className="sl__footer-copyright"> {/*Container for copyright information*/}
            <p>
                @{new Date().getFullYear()} COS30049 S2 Group 2-19 @ Swinburne. All rights reserved. {/*Gets the current year as a date to ensure always displays the present year as copyright*/}
            </p>
        </div>
        <div className="sl__footer-below-links">{/*Container for additional links primarily used for legal/whatnot stuff*/}
            <a href="/Legal"><div><p>Terms & Conditions</p></div></a>
            <a href="/Legal"><div><p>Privacy</p></div></a>
            <a href="/Legal"><div><p>Security</p></div></a>
            <a href="/Legal"><div><p>Disclaimer</p></div></a>
            <a href="/Legal"><div><p>Cookie Policy</p></div></a>
            <a href="#top"><div><p>Back to the Top</p></div></a>  {/*Lets users conveniently go back to the top of the current page*/}
            
            </div>

    </div>
    
    </div>
    </div>
    )
};

export default FooterFinal; //Exports the FooterFinal component