import React, { useState } from "react";

const sources = ["microsoft", "redhat", "mitre", "reddit"]; // Data sources

const Dashboard = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState("");

  // Function to fetch vulnerabilities for a specific source
  const fetchVulnerabilities = async (source) => {
    setLoading(source); // Show loading indicator for this source
    try {
      const response = await fetch(`http://localhost:5000/vulnerabilities?source=${source}`);
      if (!response.ok) throw new Error("Failed to fetch vulnerabilities");

      const result = await response.json();
      setData((prev) => ({ ...prev, [source]: result })); // Store in state
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    setLoading("");
  };

  return (
    <div className="dashboard">
      {sources.map((source) => (
        <div key={source} className="source-box">
          <button onClick={() => fetchVulnerabilities(source)}>
            {loading === source ? "Loading..." : `Show ${source.toUpperCase()} Vulnerabilities`}
          </button>

          {/* Display vulnerabilities if data is available */}
          {data[source] && (
            <ul>
              {data[source].map((vuln, index) => (
                <li key={index}>
                  <strong>{vuln.cve_id}</strong>: {vuln.description}
                </li>
              ))}
            </ul>
          )}
        </div>
      ))}
    </div>
  );
};

export default Dashboard;