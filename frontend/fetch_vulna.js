/*a function to fetch vulnerabilities */
import React, { useEffect, useState } from "react";
import axios from "axios";

const Vulnerabilities = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/vulnerabilities")
      .then(response => setData(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Vulnerability List</h1>
      <ul>
        {data.map((vuln, index) => (
          <li key={index}>
            <strong>{vuln.cve_id}</strong>: {vuln.description} ({vuln.severity})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Vulnerabilities;
