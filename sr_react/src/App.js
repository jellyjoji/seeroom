import React from "react";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Login from "./components/UserPage/loginPage";
import SignUp from "./components/UserPage/signupPage";
import Home from './components/Home';
import Create from "./components/Building/Create";
import BuildList from './components/Building/BuildList';
import BdDtail from "./components/Building/BdDtail";

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light fixed-top">
          <div className="container">
            <Link className="navbar-brand" to={"/"}>
              {/* this is logo  */}
            </Link>
            <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                  <Link className="nav-link" to={"/create"}>
                    건물등록
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to={"/list"}>
                    건물리스트
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to={"/sign-in"}>
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to={"/sign-up"}>
                    Sign up
                  </Link>
                </li>
                
              </ul>
            </div>
          </div>
        </nav>

        
            <Routes>
              <Route exact path="/" element={<Home />} />
              <Route path="/create" element={<Create/>}/>
              <Route path="/sign-in" element={<Login />} />
              <Route path="/sign-up" element={<SignUp />} />
              <Route path="/list" element={<BuildList />} />
              <Route path="/list/:ID" element={<BdDtail />} />
            </Routes>
          </div>
    </Router>
  );
}

export default App;
