import React from 'react';
import './HomePage.css'; // Add styles for this component if needed

function HomePage() {
  return (
    <div className="home-container">
      <h1>Generate Your Amazon Keywords Report</h1>
      <p>Use this tool to create detailed keyword reports for Amazon.</p>
      <form className="home-form">
        <label htmlFor="keywords">Enter Keywords:</label>
        <input type="text" id="keywords" name="keywords" placeholder="e.g., laptops, headphones" />
        <button type="submit">Generate Report</button>
      </form>
    </div>
  );
}

export default HomePage;
