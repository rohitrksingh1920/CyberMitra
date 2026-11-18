
import React from "react";

export default function Footer() {
  return (
    <footer className="footer bg-gray-50 text-gray-700 py-6">
      {/* Main footer area */}
      <div className="footer-main max-w-5xl mx-auto px-4 grid md:grid-cols-2 gap-8">

        {/* Brand / description */}
        <div>
          <div className="footer-brand text-2xl font-bold mb-2">
            <span>CS</span> CyberSOS
          </div>
          <p className="text-sm">
            Digital safety awareness for everyday internet users.
          </p>
        </div>

        {/* Navigation links */}
        <div className="footer-links flex flex-col space-y-2">

          {/* Existing site navigation */}
          <a href="#cases" className="hover:underline">
            Case files
          </a>

          <a href="#rules" className="hover:underline">
            13 rules
          </a>

          <a href="#report" className="hover:underline">
            Report
          </a>

          <a href="#help" className="hover:underline">
            Emergency help
          </a>

          {/* Legal pages */}
          <a href="/terms.html" className="hover:underline mt-2">
            Terms &amp; Conditions
          </a>

          <a href="/privacy.html" className="hover:underline">
            Privacy Policy
          </a>

          <a href="/contact.html" className="hover:underline">
            Contact Us
          </a>

        </div>
      </div>

      {/* Bottom bar */}
      <div className="footer-bottom mt-6 border-t border-gray-200 pt-4 text-center text-sm">
        <span>
          © 2026 CyberSOS / CyberMitra – Cyber Security Solutions
        </span>
        <br />
        <span>Stay alert. Stay safe.</span>
      </div>
    </footer>
  );
}
