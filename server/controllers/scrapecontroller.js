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