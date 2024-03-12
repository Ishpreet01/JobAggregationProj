// const { PythonShell } = require('python-shell');

// const scrapeHandler = async (req,res) =>{
//     const options = {
//         scriptPath: '../server/WebScraping', // Path to the directory containing your Python script
//         timeout: 8000000, // Timeout in milliseconds
//         // args: ['arg1', 'arg2'], // Optional arguments to pass to the Python script
//     };

//      try {
//         const results = await new Promise((resolve, reject) => {
//             PythonShell.run('scraper.py', options, (err, results) => {
//                 if (err) reject(err);
//                 else resolve(results);
//             });
//         });
//         console.log('Python script output:', results);
//         res.status(200).json({ message: "Scrape successful", data: results });
//     } catch (err) {
//         res.status(500).json({ message: "Error during scraping", error: err.toString() });
//     }
// };

const scrapeHandler = async (req,res) =>{
    try {
        // Forward the request to the Flask server
        const response = await axios.post('http://localhost:5000/api/ml', req.body);
        // Send the response from the Flask server back to the client
        res.send(response.data);
      } catch (error) {
        res.status(500).send(error.message);
      }
}

module.exports = scrapeHandler;