import React from "react";
import { Link, withRouter } from "react-router-dom";

function Navigation(props) {
  return (
    <div className="navigation">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <Link class="navbar-brand" to="/">
            Navbar
          </Link>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li
                class={`nav-item ${
                  props.location.pathname === "/" ? "active" : ""
                }`}
              >
                <Link class="nav-link active" aria-current="page" to="/">
                  Home
                  <span class="sr-only">(current)</span>
                </Link>
              </li>
              <li class="nav-item">
                <Link class="nav-link" href="/">
                  Features
                </Link>
              </li>
              <li class="nav-item">
                <Link class="nav-link" href="#">
                  Pricing
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}
