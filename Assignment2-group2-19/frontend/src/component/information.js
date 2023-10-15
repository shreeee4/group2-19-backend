import * as React from 'react';
import { useState } from 'react';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box'; 

const CustomPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  textAlign: 'center',
  color: theme.palette.text.secondary,
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  backgroundColor: '#DCF0FD',
    ...theme.typography.body2,
  borderRadius: '16px',
  fontSize: '42px',
  boxShadow: theme.shadows[6],
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  minHeight: '100vh',
}));

const ButtonContainer = styled('div')({
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'flex-startf',
  fontSize: '32px',
  gap: '32px',
  marginTop: '32px', 
});

const TextContainer = styled('div')({
    fontSize: '32px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center', 
    justifyContent: 'flex-start',
    marginTop: '16px', 
  });
const Webpage = () => {
  const [displayedText, setDisplayedText] = useState({
    'Why Use Us?': false,
    'How We Audit': false,
    'Cost': false,
  });

  const handleButtonClick = (buttonName) => {
    // Toggle the display state for the clicked button
    setDisplayedText((prevState) => ({
      ...prevState,
      [buttonName]: !prevState[buttonName],
    }));
  };

  const BoxStyle = {
    border: '2px solid #000', 
    padding: '16px', 
    marginBottom: '16px',
    borderRadius: '10px',
    backgroundColor: 'white', 
  };

  return (
    <CustomPaper elevation={3}>
      <h1>Frequently Asked Questions</h1>
      <ButtonContainer>
        <Button
          variant="contained"
          color="primary"
          onClick={() => handleButtonClick('Why Use Us?')}
          style={{fontSize: '32px'}}
        >
          Why audit?
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => handleButtonClick('How We Audit')}
          style={{fontSize: '32px'}}
        >
          How We Audit
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => handleButtonClick('Cost')}
          style={{fontSize: '32px'}}
        >
          Cost
        </Button>
      </ButtonContainer>
      <TextContainer>
        {displayedText['Why Use Us?'] && <p><span style={{fontSize: '48px'}}><b><u>Why You Should Audit</u></b></span><br></br><Box sx={BoxStyle}>As blockchain technology continues to expand, smart contracts have become a crucial tool for automating and executing transactions or agreements without the need for intermediaries. While these self-executing contracts offer unprecedented efficiency and transparency, they are not immune to vulnerabilities, with attacks potentially leading to massive amounts of financial loss. To mitigate these risks and foster trust in blockchain applications, the adoption of a smart contract auditing system is a necessity.</Box>
<br></br>
<Box sx={BoxStyle}><b>Ensuring Security and Trust</b>
<br></br>
A smart contract auditing system plays a pivotal role in enhancing security and trust within the blockchain ecosystem. It employs a rigorous and systematic process of inspecting, analysing, and testing smart contracts to identify vulnerabilities, coding errors, and security weaknesses. By doing so, it safeguards the integrity of the blockchain network and instils confidence in users and stakeholders.
</Box><br></br>
<Box sx={BoxStyle}><b>Identifying Vulnerabilities</b>
<br></br>
Smart contracts are essentially lines of code that execute predefined actions when specific conditions are met. Unfortunately, even minor errors in code can lead to significant vulnerabilities. A dedicated auditing system employs a team of experts who meticulously review the codebase, searching for vulnerabilities such as reentrancy attacks, overflow/underflow errors, and unauthorised access. Identifying these issues before deployment prevents malicious actors from exploiting them.
</Box><br></br>
<Box sx={BoxStyle}><b>Compliance and Regulatory Assurance</b>
<br></br>

In an increasingly regulated environment, businesses utilising blockchain technology must adhere to legal and compliance requirements. Smart contract audits assist in ensuring that contracts comply with relevant laws and regulations. This reduces the risk of regulatory penalties and legal disputes while establishing a framework for responsible blockchain adoption.
</Box><br></br>
<Box sx={BoxStyle}><b>Protecting Investments</b>
<br></br>
For businesses and individuals alike, investments in blockchain projects represent substantial capital. Smart contract audits act as an insurance policy, safeguarding these investments from potential threats. By detecting and rectifying vulnerabilities, audits prevent financial losses resulting from exploits or hacks, ensuring the long-term viability of blockchain applications.
</Box><br></br>
<Box sx={BoxStyle}><b>Reputation Management</b>
<br></br>
Reputation is a priceless asset in the blockchain space. A single security breach can tarnish a project's reputation irreparably. Utilising a smart contract auditing system demonstrates a commitment to security and transparency. This commitment can be communicated to users, investors, and partners, bolstering the project's credibility and trustworthiness.
</Box><br></br>
<Box sx={BoxStyle}><b>Cost-Efficiency</b>
<br></br>
Auditing smart contracts before deployment is not just about risk mitigation; it's also a cost-effective approach. Addressing vulnerabilities in the development phase is significantly more economical than dealing with the aftermath of a security breach. The costs associated with a security incident, legal, regulatory, and public relations, are often far greater than those incurred during an audit.
</Box><br></br>
<Box sx={BoxStyle}><b>Accelerating Adoption</b>
<br></br>
Security concerns have been a significant barrier to blockchain adoption. A robust auditing system removes this barrier, encouraging more enterprises, governments, and individuals to embrace blockchain technology. As adoption increases, the entire ecosystem benefits from improved efficiency, reduced fraud, and expanded use cases.
</Box><br></br>
<Box sx={BoxStyle}><b>Customised Auditing Solutions</b>
<br></br>
Smart contract auditing systems offer customised solutions tailored to the unique needs of each project. Whether it's a decentralised finance (DeFi) platform, non-fungible token (NFT) marketplace, or supply chain solution, auditing processes can be adapted to address specific industry challenges and security requirements.</Box></p>}
        {displayedText['How We Audit'] && <p><span style={{fontSize: '48px'}}><b><u>How we Audit</u></b></span><br></br><Box sx={BoxStyle}><b>1. Code Review:</b> The auditing process starts with a thorough code review. Auditors examine the smart contract's source code line by line to understand its logic, functionality, and interactions with other contracts and external components.
</Box><br></br>
<Box sx={BoxStyle}><b>2. Automated Analysis:</b> Automated tools are often used to scan the code for common vulnerabilities and potential issues. These tools can detect issues like reentrancy vulnerabilities, arithmetic overflow/underflow, and other known security risks.
</Box><br></br>
<Box sx={BoxStyle}><b>3. Manual Testing:</b> In addition to automated tools, manual testing by experienced auditors is crucial. They analyse the code in-depth to identify complex vulnerabilities that automated tools might miss. Manual testing involves creating test cases to simulate various scenarios and interactions with the contract.
</Box><br></br>
<Box sx={BoxStyle}><b>4. Best Practices:</b> Auditors ensure that the smart contract follows best practices for security and efficiency. They check for proper error handling, gas optimisation, and adherence to coding standards.
</Box><br></br>
<Box sx={BoxStyle}><b>5. Risk Assessment:</b> Auditors assess the risks associated with the smart contract, considering potential threats and attack vectors. They classify vulnerabilities based on their severity and potential impact on the contract and the blockchain network.
</Box><br></br>
<Box sx={BoxStyle}><b>6. Recommendations:</b> Based on their findings, auditors provide recommendations for improving the smart contract's security and functionality. These recommendations may include code changes, optimisations, or additional security measures.
</Box><br></br>
<Box sx={BoxStyle}><b>7. Final Report:</b> After addressing all identified issues and making necessary improvements, a final audit report is generated. This report indicates that the smart contract is secure and ready for deployment.</Box></p>}
        {displayedText['Cost'] && <p><span style={{fontSize: '48px'}}><b><u>Costs of Smart Contract Audits</u></b></span><br></br><Box sx={BoxStyle}>Smart Contract Audits are varying in price depending on various factors, such as how complex a Smart Contract is, the size of the Codebase, scope of the audit, time constraints, frequency and/or type of audits. These are just a few factors that affect how much a Smart Contract may cost. 
            
            <br></br><br></br>Luckily our website gives a free comprehensive Smart Contract audit, however if you wish for a more in-depth audit please feel free to contact one of our team members directly. </Box></p>
            }
      </TextContainer>
    </CustomPaper>
  );
};

export default Webpage;