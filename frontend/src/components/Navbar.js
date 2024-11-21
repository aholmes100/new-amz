import React from 'react';
import './Navbar.css'; // Optional, add styles here or inline

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <a href="/" className="navbar-logo">Amazon Keywords</a>
        <ul className="navbar-links">
          <li><a href="/">Home</a></li>
          <li><a href="/login">Login</a></li>
          <li><a href="/register">Register</a></li>
          <li><a href="/dashboard">Dashboard</a></li>
          <li><a href="/reports">Reports</a></li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
