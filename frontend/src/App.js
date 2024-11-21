import './App.css';
import HomePage from './components/HomePage';
import Navbar from './components/Navbar';
import Footer from "./components/Footer";

function App() {
  return (
    <div className="App">
      <Navbar />
      <header className="App-header">
        <HomePage />
      </header>

        <Footer />
    </div>
  );
}

export default App;
