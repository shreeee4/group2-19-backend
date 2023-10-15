//Simon Holt
import React, { Component } from "react";
import axios from 'axios';

class ReportPage extends Component {
    state = {
        reportId: null, // Will be updated once data is fetched
        vulnerabilities: [], // To store fetched vulnerabilities
        error: null // To store any potential error message
    };

    async componentDidMount() {
        //const {reportId} = this.props.match.params; // Get reportId from the URL
        //this.setState({reportId}); // Set the reportId
        try {
            // Replace [report_id] with the actual ID you want to query
            const response = await axios.get(`http://localhost:8000/reports/${this.props.match.params.reportId}`);
            this.setState({ 
                reportId: response.data.report_id, 
                vulnerabilities: response.data.vulnerabilities 
            });
        } catch (error) {
            this.setState({ error: 'Error fetching report data.' });
        }
    }

    render() {
        const { reportId, vulnerabilities, error } = this.state;

        return (
            <div> 
                <h2>Report ID: {reportId}</h2>
                
                {error ? (
                    <p>{error}</p>
                ) : (
                    <table>
                        <thead>
                            <tr>
                                <th>Vulnerability ID</th>
                                <th>Vulnerability Name</th>
                                <th>Impact</th>
                                <th>Description</th>
                                <th>Recommendations</th>
                            </tr>
                        </thead>
                        <tbody>
                            {vulnerabilities.map(v => (
                                <tr key={v.vulnerability_id}>
                                    <td>{v.vulnerability_id}</td>
                                    <td>{v.vulnerability_name}</td>
                                    <td>{v.impact}</td>
                                    <td>{v.description}</td>
                                    <td>{v.recomendations}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        );
    }
}

export default ReportPage;
