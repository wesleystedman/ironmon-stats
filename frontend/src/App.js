import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [runs, setRuns] = useState([]);

  // get runs on load
  useEffect(() => {
    axios.get('/api/runs')
      .then(res => setRuns(res.data.results))
      .catch(err => console.log(err))
  }, [])

  return (
    <div className="App">
      {runs.map((run, index) => (
        <div key={index}>{run.user} {run.game} run {run.attempt}</div>
      ))}
    </div>
  );
}

export default App;
