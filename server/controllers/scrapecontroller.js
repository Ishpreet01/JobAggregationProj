const { PythonShell } = require('python-shell');

const scrapeHandler = (req,res) =>{
    const options = {
        scriptPath: '../server/WebScraping', // Path to the directory containing your Python script
        timeout: 2000000, // Timeout in milliseconds
        // args: ['arg1', 'arg2'], // Optional arguments to pass to the Python script
    };

    PythonShell.run('scraper.py', options, (err, results) => {
        if (err) {
            res.status(500).json({ message: "Error during scraping", error: err.toString() });
        } else {
            console.log('Python script output:', results);
            res.status(200).json({ message: "Scrape successful" });
        }
    });
};

module.exports = scrapeHandler;